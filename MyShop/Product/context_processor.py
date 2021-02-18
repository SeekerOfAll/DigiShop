from Product.models import Category, Brand


def categories_processor(request):
    brands = Brand.objects.all()
    return {'brands': brands}
