import json
from pprint import pprint
from django.conf import settings
from django.db.models import Q, Sum
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView
from Account.models import Shop
from Order.models import Basket, Order, OrderItem
from .models import Category, Product, ProductMeta, Comment, ShopProduct


# Create your views here.
class CategoryDetailView(ListView):
    model = Product
    template_name = 'category_product.html'
    slug_url_kwarg = 'cat_slug'

    def get_queryset(self):
        queryset = super(CategoryDetailView, self).get_queryset()
        print(self.request.GET)
        category_s = get_object_or_404(Category, slug=self.kwargs["cat_slug"])
        queryset = queryset.filter(Q(category=category_s) | Q(category__parent=category_s))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDetailView, self).get_context_data()
        print(kwargs)
        context['categories'] = Category.objects.filter(slug=self.kwargs["cat_slug"])
        context['category_all'] = Category.objects.all()
        brand_list = set([product.brand.name for product in context['product_list']])
        context["brand_list"] = list(brand_list)
        print(brand_list)
        print(context)
        total_items = OrderItem.objects.aggregate(Sum("count"))
        context['total_items'] = total_items
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'products.html'
    slug_url_kwarg = 'pro_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context['product']
        context['shop_product'] = ShopProduct.objects.filter(product=context['object'])
        context['related_categories'] = Product.objects.filter(category=product.category)
        total_items = OrderItem.objects.aggregate(Sum("count"))
        context['total_items'] = total_items
        context['comments'] = product.comments.filter(is_confirmed=True)
        return context


class SearchResultsView(ListView):
    model = Product
    template_name = 'product_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(Q(category__name__icontains=query) | Q(category__parent__name=query))
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_items = OrderItem.objects.aggregate(Sum("count"))
        context['total_items'] = total_items
        return context


@csrf_exempt
def create_comment(request):
    data = json.loads(request.body)
    user = request.user
    try:
        comment = Comment.objects.create(product_id=data['product_id'], content=data['content'], author=user)
        response = {"comment_id": comment.id, "content": comment.content,'first_name': user.first_name, 'last_name': user.last_name}
        return HttpResponse(json.dumps(response), status=201)
    except:
        response = {"error": 'error'}
        return HttpResponse(json.dumps(response), status=400)
