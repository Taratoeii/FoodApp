from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import Restaurant, Menu, Review, Typefood
from django.http import Http404

# Create your views here.

def index(request):
    return render(request, 'index.html')

def show_res(request):
    restaurant = Restaurant.objects.all()
    context = {
        'show_res' : restaurant
    }
    return render(request, 'all_res.html', context)

def show_typefood(request):
    typefood = Typefood.objects.all()
    context = {
        'typefood' : typefood
    }
    return render(request, 'typefood.html', context)

def show_menu(request, restaurant_id):
    try:
        menu = Restaurant.objects.get(pk=restaurant_id)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not menu.")
    context = {
        'menu' : menu
    }
    return render(request, 'menu.html', context)

