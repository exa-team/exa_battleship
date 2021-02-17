from typing import Dict
from uuid import UUID, uuid4

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, parse_obj_as

from backend.player import Player, PlayerSchema
from backend.rooms import Room

origins = ["http://localhost:3000"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RoomBody(BaseModel):
    nickname: str
    type: str


class RoomResponse(BaseModel):
    room_id: str
    user: PlayerSchema


users = {}
rooms: Dict[UUID, Room] = {}


@app.post("/rooms")
async def get_rooms(body: RoomBody) -> RoomResponse:
    # TODO: load user_id from session
    player = Player(body.nickname)
    users[str(player.id)] = player

    room = None
    for _room in rooms.values():
        if _room.type == "public" and not _room.is_full:
            _room.register_player(player)
            room = _room
            break

    if not room:
        room = Room(body.type)
        room.register_player(player)
        rooms[str(room.id)] = room

    return {"room_id": room.id, "player": player.to_schema()}


@app.get("/stats")
def get_users():
    return {
        "users": [i.to_schema() for i in users.values()],
        "rooms": [r.id for r in rooms.values()],
    }


@app.websocket("/ws")
async def ws(websocket: WebSocket):
    await websocket.accept()

    # wait for register
    while True:
        data = await websocket.receive_json()

        if (
            data.get("type") == "register"
            and (user_id := data.get("user_id"))
            and (room_id := data.get("room_id"))
        ):
            room: Room = rooms.get(room_id)

            player = users[user_id]
            player.set_websocket(websocket)
            await player.join_room(room)

            break

    await player.listener()
