from django.contrib import admin
from django.urls import path, include

from app import views
from .models import Item
admin.site.register(Item)


# Register your models here.
