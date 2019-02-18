import datetime
from django.db import models
from django.utils import timezone


class Typefood(models.Model):
    typefood_text = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.typefood_text

class Restaurant(models.Model):
    restaurant_text = models.CharField(max_length=200,default="")
    typefood = models.ForeignKey(Typefood,default="",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.restaurant_text


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant,default="",on_delete=models.CASCADE)
    menu_text = models.CharField(max_length=200,default="")
    price_text = models.IntegerField()
    
    def __str__(self):
        return self.menu_text

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant,default="",on_delete=models.CASCADE)
    review_text = models.CharField(max_length=1000,default="")
    review_date = models.DateTimeField('date published')
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.review_text
    

        