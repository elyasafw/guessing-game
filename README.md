
# Number Guessing Game 🎮

A professional, modular Python CLI game featuring secure user authentication, progress saving, and global leaderboards.

## ✨ Key Features
- **Secure Auth:** Integrated login/sign-up system with **MD5 password hashing**.
- **Progress Saving:** State-persistence allowing users to resume games via CSV storage.
- **Global Leaderboard:** Real-time high-score tracking stored in JSON format.
- **Modular Architecture:** Clean separation between game logic (`code_files`) and data (`game_files`).

## 📂 Project Structure
- `code_files/`: Core logic, user procedures, and game engine.
- `game_files/`: Persistent storage for users, saves, and records.

## 🚀 Getting Started
1. **Clone the repository**:
   ```bash
   git clone https://github.com/elyasafw/guessing-game.git

2. **Run the application:**
   ```bash
   python code_files/main.py

🎮 How to Play
* **Login:** Enter your username to authenticate or register.
* **Select Mode:** Choose between starting a New Game or Continuing a saved session.
* **Guess:** Find the secret number (0-500). Type exit at any time to save and quit.
