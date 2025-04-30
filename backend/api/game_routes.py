# backend/api/game_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from backend.core import game_logic
from db  import models
from db.database import get_db  # <-- Assuming you have a database.py with get_db


router = APIRouter()

class Move(BaseModel):
    move: str


@router.get("/")
async def root():
    return {"message": "Game API is running"}


@router.post("/start_game")
async def start_game(db: AsyncSession = Depends(get_db)):
    # Start a new game session
    new_game = await game_logic.start_game(db)
    return {"message": "Game started!", "game_id": new_game.id}

@router.post("/make_move/{game_id}")
async def make_move(game_id: int, move: Move, db: AsyncSession = Depends(get_db)):
    game_session = await db.get(models.GameSession, game_id)
    if not game_session:
        return {"error": "Game session not found. Please start a new game."}

    # Determine the seed word
    if game_session.guesses:
        seed_word = game_session.guesses[-1].guess_word
    else:
        seed_word = "rock"

    result = await game_logic.process_guess(db, game_session, move.move, seed_word)

    return result

