from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Products

# Create your views here.
goods = Products.objects.all()


def catalog(request, category_slug, page=1):
    if category_slug == "all":
        goods = Products.objects.all()
    else:
        # get_object_or_404 trebuie de folosit in randul de mai jos dar nu merge ceva
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)

    current_page = paginator.get_page(page)
    context = {
        "title": "Home-Catalog",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {"product": product}
    return render(request, "goods/product.html", context=context)
