from typing import List, Optional
from pydantic import BaseModel

class StudentCreate(BaseModel):
    id:int
    name: str
    email: str
    password:str
    enrollment_date: str

    

class GameCreate(BaseModel):
    id:int
    name: str
    game_type: str
    date_of_game: str
    max_participants: int
    stud_id: int

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    # scopes: list[str] = []