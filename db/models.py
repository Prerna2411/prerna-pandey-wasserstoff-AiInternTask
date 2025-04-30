# backend/db/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class GameSession(Base):
    __tablename__ = 'game_sessions'

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
    is_active = Column(Boolean, default=True)
    result = Column(String, nullable=True)  # "win", "lose", or None
    score = Column(Integer, default=0) 
    # Relationship to guesses
    guesses = relationship("Guess", back_populates="session", cascade="all, delete-orphan")

class Guess(Base):
    __tablename__ = 'guesses'

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('game_sessions.id'), nullable=False)
    text = Column(String, nullable=False)
    verdict = Column(String, nullable=False)  # "valid", "duplicate", "invalid"
    created_at = Column(DateTime, server_default=func.now())

    # Linked-list reference
    prev_guess_id = Column(Integer, ForeignKey('guesses.id'), nullable=True)
    prev_guess = relationship("Guess", remote_side=[id], post_update=True)

    session = relationship("GameSession", back_populates="guesses")

class GlobalCounter(Base):
    __tablename__ = 'global_counters'

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)  # e.g., "total_games", "wins", "losses", "total_guesses"
    value = Column(Integer, default=0)
