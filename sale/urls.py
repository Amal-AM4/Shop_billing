from django.contrib import admin
from django.urls import path, include, re_path
from sale import views


urlpatterns = [
    path('get_product_price/<uuid:product_id>/', views.get_product_price, name='get_product_details'),
    re_path(r"^CreateSale/$", views.create_sale, name='CreateSale'),
    path('product_search/', views.product_search_view, name='product_search'),
]
