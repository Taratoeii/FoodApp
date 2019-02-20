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

def search_res(request):
    get_search = request.POST['search']
    try:
        check_search = Restaurant.objects.get(restaurant_text=get_search)
    except (KeyError, Restaurant.DoesNotExist):
        return render(request, 'search.html', {
            'error_message' : "No restaurants found"
        })
    else:
        get_id = check_search.id
        get_menu = Restaurant.objects.get(pk=get_id)
        return render(request, 'menu.html', {
        'get_res' : get_search,
        'get_menu' : get_menu
    })
    return render(request, 'index.html')

def add_review(request):
    # get_name = request.POST['get_res']
    # get_review = request.POST['get_review']
    # get_score = request.POST['get_point']
    # get_date = request.POST['get_date']
    # try :
    #     check_name = Restaurant.objects.get(restaurant_text=get_name)
    # except (KeyError, Restaurant.DoesNotExist):
    #     return render(request, 'add_review.html', {
    #         'error_message' : "No restaurants found"
    #     })
    # else:
    #     get_id = check_name.id
    #     get_pk = Restaurant.objects.get(pk=get_id)
    #     review = get_pk.review_set.create(review_text="get_review",score="get_score",review_date="get_date")
    #     review.save()
    return render(request, 'add_review.html')

