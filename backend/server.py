from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4

origins = ['http://localhost:3000']

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

@app.post("/rooms")
def get_rooms(body: RoomBody):
    return {
        "id": str(uuid4()),
        "nickname": body.nickname
    }
