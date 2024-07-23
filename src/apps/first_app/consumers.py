from channels.generic.websocket import AsyncConsumer


class WebSocketConsumer(AsyncConsumer):
    async def connect(self, event) -> None:
        await self.send({"type": "websocket.accept"})

    async def close_connection(self, event) -> None:
        pass

    async def websocket_receive(self, data: str) -> None:
        await self.send(
            {
                "type": "websocket.send",
                "text": data,
            }
        )
