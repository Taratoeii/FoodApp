from django.urls import path
from . import views

app_name = 'foodapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('Allrestaurant/', views.show_res, name='allres'),
    path('typefood/', views.show_typefood, name='typefood'),
    path('search/', views.search_res, name='search')
]


