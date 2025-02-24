from django.urls import path
from .views import movies_list, movie_detail

urlpatterns = [
    path('', movies_list, name='movies_list'),  
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),
]
