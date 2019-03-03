from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import Restaurant, Menu, Review, Typefood
from django.http import Http404
import datetime
from django.utils import timezone

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

def show_menu(request,id):
    menu = get_object_or_404(Restaurant, pk=id)
    return render(request, 'menu.html', {'menu': menu})

def show_restype(request,id):
    typefood = get_object_or_404(Typefood, pk=id)
    return render(request, 'res_type.html', {'typefood': typefood})

def search_res(request):
    findres = (request.POST['search'])
    res_list = Restaurant.objects.values_list("id" , "restaurant_text").filter(restaurant_text__contains = findres)
    count = len(res_list)
    context = {
        'res_list':res_list,
        'count':count,
        'res':findres}
    return render(request, 'show_search.html',context)

def detailres(request,id):
    res = get_object_or_404(Restaurant, pk=id)
    review = Review.objects.values_list("review_res_id","name_text","review_text","review_date","score").filter(review_res_id=id)
    context = {
        'res' : res,
        'review' : review
    }
    return render(request, 'detailres.html',context)


def add_review(request):
    nameres = str(request.POST['res'])
    nameuser = str(request.POST['user'])
    review = str(request.POST['review'])
    score = int(request.POST['point'])
    reviewres = Review(review_res_id=nameres,name_text=nameuser,review_text=review,review_date=timezone.now(),score=score)
    reviewres.save()
    return redirect('foodapp:detail',nameres)


