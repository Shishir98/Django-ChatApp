# mysite/asgi.py
import os
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '/home/user/Desktop/Django/mysite/chat/')
# import routing

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from channels.http import AsgiHandler

import chat.routing as routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = ProtocolTypeRouter({
  # "http": AsgiHandler(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})