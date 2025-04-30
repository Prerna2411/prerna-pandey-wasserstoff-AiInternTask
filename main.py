from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database, game_logic

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/start_game")
def start_game(db: Session = Depends(get_db)):
    game_session = game_logic.start_game(db)
    return {"game_session_id": game_session.id, "score": game_session.score}

@app.post("/make_guess")
async def make_guess(guess_word: str, seed_word: str, game_session_id: int, db: Session = Depends(get_db)):
    game_session = db.query(models.GameSession).filter(models.GameSession.id == game_session_id).first()
    if not game_session:
        return {"error": "Game session not found."}

    result = await game_logic.process_guess(db, game_session, guess_word, seed_word)
    return result





