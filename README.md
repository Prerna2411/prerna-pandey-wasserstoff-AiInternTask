# 🧠 GenAI Game: *What Beats Rock*

This is a creative AI-powered web game where the player submits a move like "rock", and the AI counters it with an imaginative, logical move that could beat it — e.g., “water drowns rock”. The game evaluates creativity, logic, and tracks wins/losses in real time.

## 🚀 Setup Instructions

### 📦 Requirements
- Docker & Docker Compose installed
- Internet connection (for Groq API)

### ⚙️ Clone the Repository

git clone https://github.com/Prerna2411/prerna-pandey-wasserstoff-AiInternTask/tree/main
cd gen_ai_game


📁 2. Configure Environment
Rename the .env.example file to .env and fill in your API keys:

GROQ_API_KEY=your_groq_api_key
🐳 3. Run the Game
bash
Copy
Edit
docker-compose up --build
The game will be available at: http://localhost:8000

🕹️ How to Play
Open the frontend page in your browser.

Type your move (e.g., “rock”, “fire”, or even “taxes”).

The AI will respond with a creative counter.

You'll see whether you won, lost, or drew — based on a logic evaluation.

Keep playing and see your global win stats update!

🧱 Architecture Overview
Frontend: A minimal HTML form with Bootstrap (or vanilla JS) that submits the player's move.

Backend: FastAPI app that handles player input, constructs prompts, queries Groq + Mistral, and determines game outcome.

AI Client: Sends structured prompts to the LLM using ai_client.py.

Game Logic: Validates results, prevents duplicates, and calculates win/draw/loss.

Caching: Redis is used to cache past moves and AI responses to reduce latency and cost.

Dockerized: Uses Dockerfile and docker-compose to simplify setup.

💡 Prompt Design
The prompt sent to the LLM is carefully structured for creativity, clarity, and determinism:

The player chose: "rock".
Think creatively — what object or concept could beat this in a clever, logical way?
Respond with one line: [Your counter-move] — [Explanation]
🧠 Example Prompt:
The player chose: "fire".
Think creatively — what object or concept could beat this in a clever, logical way?

🧠 Example Response:
"Water — It extinguishes fire."

🛡️ Duplicate Detection
The backend uses a hashed move+response cache in Redis to ensure the same move doesn’t generate reused responses unnecessarily.

📊 Stats & Logging
Redis tracks total games, unique moves, AI hits, and win/loss counts.

Move history is stored using a linked list per player (in memory).

Stats are available via API endpoints for future frontend dashboards.

🧪 Testing
API tested using curl and Postman.

Handles missing input, repeated moves, and LLM errors gracefully.

💡 Potential Improvements
Add “Combo Mode” (submit 3 moves at once).

Emoji feedback or animations on frontend.

User login and score history.

Save game sessions to database.

📄 License
This project is open-source under the MIT License.

🙌 Acknowledgments
Groq – for ultra-fast inference API.

Mistral AI – for the creative model.

FastAPI – for the backend framework.

Redis – for caching.







