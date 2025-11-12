from django.urls import path
from . import views

urlpatterns = [
    path('submit_rating/', views.submit_rating, name='submit_rating'),
    path('create_restaurant/', views.create_restaurant, name='create_restaurant'),
    path('', views.index, name='index'),
]