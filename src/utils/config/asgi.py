import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from django.core.asgi import get_asgi_application


from apps.first_app.consumers import WebSocketConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.utils.config.settings.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [
                path('web_socket', WebSocketConsumer.as_asgi()),
            ]
        )
    )
})