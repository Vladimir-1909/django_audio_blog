from django.urls import path

from . import views

urlpatterns = [
    path('', views.AudioView.as_view(), name='audio_list'),
    path('genre/', views.GenreView.as_view(), name='genre_list'),
    path('genre/<str:slug>/', views.GenreDetail.as_view(), name='genre_detail'),
    path('audio/add/', views.AudioCreate.as_view(), name='add_audio'),
]