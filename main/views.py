from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):

    categories = Categories.objects.all()
    context = {
        "title": "Home",
        "content": "Магазин мебели HOME",
        "categories": categories,
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "About",
        "content": "More Information",
        "text_on_page": "Goods for good price!",
    }
    return render(request, "main/about.html", context)
