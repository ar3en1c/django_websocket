import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # وصل شدن موفق
        await self.accept()
        print("🔵 WebSocket connected")

    async def disconnect(self, close_code):
        # قطع شدن اتصال
        print("🔴 WebSocket disconnected")

    async def receive(self, text_data):
        # دریافت پیام از کلاینت
        print(f"پیام دریافتی: {text_data}")

        # ارسال دوباره همون پیام به کلاینت (Echo)
        await self.send(text_data=json.dumps({
            'message': text_data
        }))
