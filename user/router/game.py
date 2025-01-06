
from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session

from .. import models, schema
from .. import database

router = APIRouter(
    prefix="/games",
    tags=['Game']
)

get_db = database.get_db


@router.post("/", tags=["Game"])
def create_game(game: schema.GameCreate, db: Session = Depends(get_db)):
    db_game = models.Game(
        name=game.name, 
        game_type=game.game_type,
        date_of_game=game.date_of_game,
        max_participants=game.max_participants,
        stud_id = game.stud_id
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

@router.get("/{game_id}",tags=["Game"])
def read_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@router.put("/{game_id}",tags=["Game"])
def update_game(game_id: int, game: schema.GameCreate, db: Session = Depends(get_db)):
    db_game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if not db_game:
        raise HTTPException(status_code=404, detail="Game not found")
    db_game.name = game.name
    db_game.game_type = game.game_type
    db_game.date_of_game = game.date_of_game
    db_game.max_participants = game.max_participants
    db_game.stud_id = game.stud_id
    db.commit()
    db.refresh(db_game)
    return db_game


@router.delete("/{game_id}",tags=["Game"])
def delete_game(game_id: int, db: Session = Depends(get_db)):
    db_game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if not db_game:
        raise HTTPException(status_code=404, detail="Game not found")
    db.delete(db_game)
    db.commit()
    return {"message": f"Game with id {game_id} deleted successfully"}