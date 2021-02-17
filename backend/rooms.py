from __future__ import annotations

from uuid import uuid4
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.player import Player


class Room:

    def __init__(self, type: str) -> None:
        self.id = uuid4()
        self.players = []
        self.type = type
        self.registered = 0

    def register_player(self, player: Player) -> None:
        if not self.is_full:
            self.players.append(player)

    async def join_player(self, player: Player) -> None:
        if self.registered < 2 and player in self.players:
            self.registered += 1
        else:
            raise ValueError("Full")

        if self.is_ready:
            await self.send_all({"type": "gg"})

    async def send_all(self, data):
        for player in self.players:
            await player.send(data)

    @property
    def is_ready(self):
        return self.registered == 2

    @property
    def is_full(self):
        return len(self.players) >= 2
