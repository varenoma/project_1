from django.urls import path
from .views import show_products, product_detail

app_name = 'product'

urlpatterns = [
    path('', show_products, name='show_products'),
    path('product/<int:id>/', product_detail, name='product_detail'),
]