# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api import game_routes


app = FastAPI()
print("✅ game_routes imported") 
# Allow requests from frontend (localhost:5500 or wherever it's hosted)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with actual domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include the game routes
app.include_router(game_routes.router)


@app.get("/health")
async def health():
    return {"status": "ok"}



