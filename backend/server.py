import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse

from room import room_handler, Player, get_or_create_room

app = FastAPI()

rooms = {}

from pydantic import BaseModel
from enum import Enum


class RoomTypeEnum(str, Enum):
    private = "private"
    public = "public"


class RoomSchema(BaseModel):
    type: RoomTypeEnum


@app.post("/room")
async def get(room: RoomSchema):
    room_ = await get_or_create_room(room.type)
    return JSONResponse({"room": str(room_.id)})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # breakpoint()
    me = Player(websocket)
    room = await room_handler(me)

    while True:
        print("waiting for message")
        data = await websocket.receive_text()
        # await .send_text(f"teste {data}")
