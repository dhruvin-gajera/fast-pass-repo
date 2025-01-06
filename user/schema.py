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

