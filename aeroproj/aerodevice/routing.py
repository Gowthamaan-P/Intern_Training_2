from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        path("ws/testpath/", consumers.test_consumer.as_asgi()),
    ),
})