from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ensure this line exists
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('properties/', views.properties, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('main/', views.main, name='main'),
]
