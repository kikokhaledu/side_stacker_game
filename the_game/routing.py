# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/(?P<game_id>\w+)/$', consumers.Connect4Consumer.as_asgi()),
]