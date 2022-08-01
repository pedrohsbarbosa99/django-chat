import os
import sys


import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochatexample.settings')
django.setup()

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter, ProtocolTypeRouter
import djangochatexample.room.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            djangochatexample.room.routing.websocket_urlpatterns
        )
    )
})
