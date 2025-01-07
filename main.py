from fastapi import FastAPI, HTTPException, Depends,status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Annotated
from user import models 
from user.database import SessionLocal, engine
from user.router import student, game,authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(authentication.router)

app.include_router(student.router)
app.include_router(game.router)


