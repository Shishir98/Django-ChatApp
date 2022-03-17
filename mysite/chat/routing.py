# chat/routing.py
from django.urls import re_path
import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '/home/user/Desktop/Django/mysite/chat/')
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]