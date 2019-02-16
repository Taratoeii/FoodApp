from django.urls import path
from . import views

app_name = 'foodapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('Allrestaurant/', views.show_res, name='allres'),
    path('menu/', views.show_menu, name='allmenu'),
    path('typefood/', views.show_typefood, name='typefood')
]

