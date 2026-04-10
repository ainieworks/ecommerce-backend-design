from django.urls import path
from . import views

# URL patterns for store app
# Each path connects a URL to a view function
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
]