import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, TemplateView
from django.db.models import Sum
from Account.models import Shop
from Order.models import Order, OrderItem, Basket
from Product.models import Product, ShopProduct


class CartView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        order_item = OrderItem.objects.all()
        order = Order.objects.all()
        total_items = OrderItem.objects.aggregate(Sum("count"))
        total_price = OrderItem.objects.aggregate(Sum("price"))
        print(total_price)
        context['order_item'] = order_item
        context['total_items'] = total_items
        context['total_price'] = total_price

        return context


def add_to_cart(request):
    data = json.loads(request.body)
    shopProductID = data['shopProductID']
    action = data['action']
    print('shopProductID:', shopProductID)
    print('action:', action)
    print(request.user)
    print(request.user.first_name)

    user = request.user
    shop_product = ShopProduct.objects.get(id=shopProductID)
    print("first_name:" + user.first_name, "last_name: " + user.last_name, "product: " + shop_product.product.name,
          "shop: " + shop_product.shop.name)
    order, created = Order.objects.get_or_create(user=user,
                                                 description='first_name: ' + user.first_name +
                                                             ' - last_name: ' + user.last_name +
                                                             ' - product: ' + shop_product.product.name +
                                                             ' - shop: ' + shop_product.shop.name)
    order_item, created = OrderItem.objects.get_or_create(order=order, shop_product=shop_product)
    orderModel = Order.objects.all()
    print(shop_product.price)
    if action == 'add':
        order_item.count = (order_item.count + 1)
        order_item.price = (int(order_item.price) + int(shop_product.price))
    elif action == 'remove':
        order_item.count = (order_item.count - 1)
        order_item.price = (int(order_item.price) - int(shop_product.price))

    if action == 'delete':
        order_item.count = 0

    order_item.save()

    if order_item.count <= 0:
        order_item.delete()

    return JsonResponse('Item was added ', safe=False)
