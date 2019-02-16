from django.contrib import admin
from .models import Restaurant, Typefood
from .models import Menu
from .models import Review


admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Review)
admin.site.register(Typefood)
# Register your models here.
