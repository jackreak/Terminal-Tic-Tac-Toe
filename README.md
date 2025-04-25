# 🧠 Terminal Tic Tac Toe

A classic game of Tic Tac Toe played in the terminal!  
You play as **Player 1 (X)** while the computer plays as **Player 2 (O)** with a basic AI that:
- ✅ Wins when it can
- 🚫 Blocks you from winning
- 🎯 Prioritizes center > corners > sides

---

## 🎮 How to Play

1. Run the game:
   ```bash
   python TTTT.py
   ```

2. On your turn, enter the **column letter (A, B, C)** and **row number (1, 2, 3)** when prompted.

Example input:
```
Enter column (A, B, or C): B
Enter row (1, 2, or 3): 2
```

---

## 🧠 AI Behavior

The computer will:
- Check if it can **win** in one move.
- Try to **block you** from winning.
- Choose the **center** if it’s available.
- Pick a **corner** if the center is taken.
- Settle for a **side** if nothing else is left.

The AI uses simple decision-making logic — not unbeatable, but definitely clever!

---

## 📁 Files

- `TTTT.py` – Main game file (run this).
- `readme.md` – This file.

---

## 🛠️ Requirements

- Python 3.6 or higher

No external libraries are needed. It's pure Python.

---

## 📜 License

MIT License

---

Enjoy the game! Feel free to fork, hack, and improve it. 😄
