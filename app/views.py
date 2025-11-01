from django.http import HttpResponse
from app.models import Item
from django.shortcuts import render, get_object_or_404


def home(reqest):
    return render(reqest, "item.html")


def get_items(reqest):
    # if(Item.objects.all):
    objects = Item.objects.all()
    return render(reqest, "products_list.html", {"items": objects})


def get_item(reqest, item_id):
    item = get_object_or_404(Item, id = item_id)
    return render(reqest, "item.html", {"product": item})


def basket(reqest):
    return HttpResponse("<h1>турсэков пока нет :( </h1>")


def profile(reqest):
    return HttpResponse("<h1>турсэков пока нет :( </h1>")


def login(reqest):
    return HttpResponse("<h1>турсэков пока нет :( </h1>")


def logout(reqest):
    return HttpResponse("<h1>турсэков пока нет :( </h1>")
