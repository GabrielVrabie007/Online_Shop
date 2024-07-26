from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"title": "Home", "content": "Магазин мебели HOME"}

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "About",
        "content": "More Information",
        "text_on_page": "Goods for good price!",
    }
    return render(request, "main/about.html", context)
