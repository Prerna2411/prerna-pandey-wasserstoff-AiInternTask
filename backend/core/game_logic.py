from backend.core import ai_clients,cache
from  db import models
from sqlalchemy.ext.asyncio import AsyncSession

import httpx
import os


# Function to handle guess processing using either Groq or Mistral
async def process_guess(db: AsyncSession, game_session, guess_word: str, seed_word: str, use_mistral: bool = False):
    cache_key = f"{guess_word}-{seed_word}"
    cached_result = cache.get_cache(cache_key)
    if cached_result:
        return cached_result

    if use_mistral:
        ai_response = await ai_clients.query_mistral(guess_word, seed_word)
    else:
        ai_response = await ai_clients.query_groq(guess_word, seed_word)

    if ai_response == "YES":
        last_guess = game_session.guesses[-1] if game_session.guesses else None
        if last_guess and last_guess.guess_word == guess_word:
            return {"game_over": True, "message": f"Game Over! {guess_word} has already been guessed."}

        new_guess = models.Guess(guess_word=guess_word, game_session_id=game_session.id)
        db.add(new_guess)
        await db.commit()
        await db.refresh(new_guess)

        global_counter = await db.get(models.GlobalCounter, guess_word)
        if global_counter:
            global_counter.total_guesses += 1
        else:
            global_counter = models.GlobalCounter(word=guess_word, total_guesses=1)
            db.add(global_counter)
        await db.commit()

        game_session.score += 1
        await db.commit()

        cache.set_cache(cache_key, {"result": ai_response, "score": game_session.score})
        return {"result": ai_response, "score": game_session.score}

    else:
        return {"game_over": True, "message": f"Game Over! {guess_word} does not beat {seed_word}."}


async def start_game(db):
    new_game = models.GameSession(score=0)
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return new_game



