from django.contrib import admin
from django.urls import path, include, re_path
from product import views


urlpatterns = [
    re_path(r"^AddProduct/$", views.insert_product, name='AddProduct'),
]
