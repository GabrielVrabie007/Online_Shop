from django.shortcuts import render

from goods.models import Categories, Products

# Create your views here.
goods = Products.objects.all()


def catalog(request):

    # categories = Categories.objects.all()

    context = {"title": "Home-Catalog", "goods": goods}
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
