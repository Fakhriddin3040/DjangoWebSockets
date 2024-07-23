import json
from channels.generic.websocket import AsyncWebsocketConsumer


class WebSocketConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def connect(self) -> None:
        # Принятие подключения
        await self.accept()

    async def disconnect(self, close_code: int) -> None:
        # Обработка отключения
        pass

    async def receive(self, text_data: str) -> None:
        # Принятие данных от клиента
        # Отправка ответа клиенту
        data = {"message": "I've got u baby!"}
        print(text_data)
        await self.send(text_data=json.dumps(data))
