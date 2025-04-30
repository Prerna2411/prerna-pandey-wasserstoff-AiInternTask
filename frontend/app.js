let currentGameId = null; // New variable to store game id

const startGame = async () => {
    try {
        const response = await fetch('http://localhost:8000/start_game', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data.message);
            currentGameId = data.game_id; // Store game_id here!
            document.getElementById('gameArea').style.display = 'block';
            document.getElementById('startGameBtn').style.display = 'none';
        } else {
            alert('Failed to start game!');
        }
    } catch (error) {
        console.error('Error starting the game:', error);
        alert('An error occurred while starting the game.');
    }
};

const makeMove = async (move) => {
    if (!currentGameId) {
        alert('Please start the game first.');
        return;
    }
    try {
        const response = await fetch(`http://localhost:8000/make_move/${currentGameId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({move: move})
        });

        if (response.ok) {
            const result = await response.json();
            displayResult(result);
        } else {
            alert('Error making the move!');
        }
    } catch (error) {
        console.error('Error during the move:', error);
        alert('An error occurred while making your move.');
    }
};

const displayResult = (result) => {
    document.getElementById('gameResult').textContent = `You chose ${result.move}, Computer chose ${result.computer_move}. Result: ${result.result}`;
    document.getElementById('result').style.display = 'block';
    document.getElementById('gameArea').style.display = 'none';
};
