from uuid import uuid4
from requestvars import g

# rooms = {}

g().rooms = {}

class Room:
    def __init__(self, type: str):
        self.id = uuid4()
        self.type = type
        self.players = {}

    @property
    def is_full(self):
        return len(self.players.values()) == 2

    async def add(self, player):
        print(f"Added {player} to room: {self.id}")

        if self.is_full:
            raise ValueError()

        self.players[player.id] = player

        await player.send(f"você entrou na sala {self.id}")


class Player:
    def __init__(self, ws):
        self.id = uuid4()
        self.ws = ws

    async def send(self, message):
        await self.ws.send_text(message)


async def get_or_create_room(type: str) -> Room:
    rooms = g().rooms
    print([f"{k}: {len(v.players.keys())}" for k, v in rooms])
    for room in rooms.values():
        if not room.is_full and room.type == type:
            return room

    return Room(type)


async def room_handler(client):
    print("room handler")
    found = False
    for room in rooms.values():
        if not room.is_full:
            print(f"room {room.id} is not full. Adding {client}")
            await room.add(client)
            found = True
            break

    if not found:
        room = Room()
        print(f"Creating new room {room.id}")
        rooms[room.id] = room
        await room.add(client)

    return room
