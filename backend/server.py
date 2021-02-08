from fastapi import FastAPI
from pydantic import BaseModel

from uuid import uuid4

app = FastAPI()


class RoomBody(BaseModel):
    nickname: str


@app.post("/rooms")
def get_rooms(body: RoomBody):
    return {
        "id": str(uuid4()),
        "nickname": body.nickname
    }
