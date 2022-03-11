from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.movieList, name='list'),
    path('detail/<str:pk>/', views.movieDetail, name = 'detail'),
    path('create', views.movieAdd, name = 'create'),
    path('update/<str:pk>', views.movieUpdate, name = 'update'),
    path('delete/<str:pk>/', views.movieDelete, name='delete'),
]
