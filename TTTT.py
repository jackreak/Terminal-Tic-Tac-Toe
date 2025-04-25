#Terminal Tic Tac Toe v1.1
def print_board(board):
    print("    A   B   C")
    for idx, row in enumerate(board):
        print(f"{idx + 1}  " + " | ".join(row))
        if idx < 2:
            print("   ---+---+---")

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_positions(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def try_move(board, player, r, c):
    board[r][c] = player
    win = check_winner(board) == player
    board[r][c] = " "
    return win

def get_computer_move(board):
    empty_positions = get_empty_positions(board)

    # 1. Can win this turn?
    for r, c in empty_positions:
        if try_move(board, "O", r, c):
            return r, c

    # 2. Can block player from winning?
    for r, c in empty_positions:
        if try_move(board, "X", r, c):
            return r, c

    # 3. Pick center if available
    if board[1][1] == " ":
        return 1, 1

    # 4. Pick a corner if available
    for r, c in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[r][c] == " ":
            return r, c

    # 5. Pick a side if available
    for r, c in [(0, 1), (1, 0), (1, 2), (2, 1)]:
        if board[r][c] == " ":
            return r, c

    # Fallback (shouldn't happen)
    return empty_positions[0]

def main():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]

        print("Welcome to Terminal Tic Tac Toe!")
        print("You are Player 1 (X). The computer is Player 2 (O).")
        print_board(board)

        turn = 0
        while True:
            current_player = "X" if turn % 2 == 0 else "O"

            if current_player == "X":
                print("Your turn.")
                try:
                    col = input("Enter column (A, B, or C): ").upper()
                    row = int(input("Enter row (1, 2, or 3): "))
                    col_dict = {'A': 0, 'B': 1, 'C': 2}
                    if col not in col_dict or row not in [1, 2, 3]:
                        print("Invalid input.")
                        continue
                    col_idx = col_dict[col]
                    row_idx = row - 1
                    if board[row_idx][col_idx] != " ":
                        print("That spot is taken.")
                        continue
                except (ValueError, KeyError):
                    print("Invalid input.")
                    continue
            else:
                print("Computer's turn...")
                row_idx, col_idx = get_computer_move(board)

            board[row_idx][col_idx] = current_player
            print_board(board)

            winner = check_winner(board)
            if winner:
                if winner == "X":
                    print("You win!")
                else:
                    print("The computer wins!")
                break

            if is_draw(board):
                print("It's a draw!")
                break

            turn += 1

        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
