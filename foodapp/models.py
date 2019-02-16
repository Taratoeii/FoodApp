import datetime
from django.db import models
from django.utils import timezone

class Restaurant(models.Model):
    restaurant_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.restaurant_text

class Typefood(models.Model):
    typefood_text = models.CharField(max_length=200)

    def __str__(self):
        return self.typefood_text

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='restaurant',on_delete=models.CASCADE)
    typefood = models.ForeignKey(Typefood, null=True, related_name='typefood',on_delete=models.CASCADE)
    menu_text = models.CharField(max_length=200)
    price_text = models.IntegerField()
    image = models.ImageField(upload_to='order_image', blank=False)
    
    def __str__(self):
        return self.menu_text

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='reviewres',on_delete=models.CASCADE)
    review_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.review_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

        