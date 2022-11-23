from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('setup/', views.setup, name='setup'),
    path('create_game/', views.create_game, name='create_game'),
    path('join_game/', views.join_game, name='join_game'),
    path('game/<int:game_id>', views.game, name='game'),
]