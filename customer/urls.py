from django.contrib import admin
from django.urls import path, include, re_path
from customer import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    re_path(r"^AddCustomer/$", views.create_customer, name='AddCustomer'),
]
