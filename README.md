# Tic Tac Toe 🎲

A Python implementation of the classic two-player game, **Tic Tac Toe**. Take turns with another player marking spaces on a 3x3 grid and compete to get three in a row before your opponent!

---

## How It Works

### Objective
- Be the first player to align three of your marks (X or O) horizontally, vertically, or diagonally on the 3x3 grid.
- If all spaces are filled without a winner, the game ends in a tie.

### Features
- Interactive board display for clear gameplay.
- Input validation to avoid errors or invalid moves.
- Replay option to keep the fun going!

---

## How to Play
1. Clone this repository:
    ```bash
    git clone https://github.com/DoctorPingu/tic-tac-toe.git
    ```
2. Navigate to the project directory:
    ```bash
    cd tic-tac-toe
    ```
3. Start the game:
    ```bash
    python Tic_Tac_Toe.py
    ```

---

## Game Walkthrough
1. **Introduction**  
   Upon starting, you're welcomed and prompted to view the rules if needed.

2. **Choosing Markers**  
   Player 1 selects their marker (`X` or `O`). Player 2 is automatically assigned the other marker.

3. **Gameplay**  
   - Players take turns selecting positions (1–9) on the grid to place their marker.
   - The game checks for a winner or if the board is full after every turn.

4. **Game End**  
   - A winner is declared if a player gets three in a row.
   - If the board is full with no winner, the game ends in a tie.

5. **Replay**  
   After the game ends, players can choose to replay or exit.

---

## Project Structure
- **`Tic_Tac_Toe.py`**: Main script to run the game.
- **`Components.py`**: Contains all logic, functions, and helper utilities.

---

## Requirements
- Python 3.x installed on your system.

---

## Contributions
This is one of my early projects, and I'd love to improve it! Feel free to:
- Fork this repository and enhance it.
- Submit a pull request for new features or bug fixes.
- Provide feedback or suggest improvements.

---

Enjoy playing **Tic Tac Toe**! 🕹️
