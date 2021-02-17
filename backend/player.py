from typing import Any, Dict
from uuid import UUID, uuid4

from backend.rooms import Room
from fastapi import WebSocket
from pydantic.main import BaseModel


class PlayerSchema(BaseModel):
    id: UUID
    nickname: str
    registered: bool


class Player:
    ws: WebSocket = None

    def __init__(self, nickname: str) -> None:
        self.id = uuid4()
        self.nickname = nickname
        self.current_room = None

    def set_websocket(self, ws):
        self.ws = ws

    async def join_room(self, room: Room) -> None:
        self.current_room = room
        await self.current_room.join_player(self)
        await self.listener()

    def to_schema(self):
        return PlayerSchema(
            id=self.id, nickname=self.nickname, registered=bool(self.ws)
        )

    async def send(self, data: Dict[Any, Any]) -> None:
        await self.ws.send_json(data)

    async def listener(self):
        while True:
            data = await self.ws.receive_json()
            print('data received', data)
