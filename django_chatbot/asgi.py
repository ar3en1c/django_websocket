import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import chat.routing  # 👈 مسیر اپلیکیشن خودت

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_chatbot.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns  # 👈 می‌سازیمش الان
        )
    ),
})
