from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('setup/', views.setup, name='setup'),
    path('creategame/', views.creategame, name='creategame'),
    path('game/<int:game_id>', views.game, name='game'),
]