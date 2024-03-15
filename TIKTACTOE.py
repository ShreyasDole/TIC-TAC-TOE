import tkinter as tk

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def on_click(row, col):
    global current_player_idx
    current_player = players[current_player_idx]
    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state=tk.DISABLED)  # Disable button after click
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            for row in buttons:
                for button in row:
                    button.config(state=tk.DISABLED)  # Disable all buttons
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
        else:
            current_player_idx = 1 - current_player_idx
    else:
        print("Cell is already occupied. Try again.")

def create_board_buttons():
    buttons = []
    for i in range(3):
        row_buttons = []
        for j in range(3):
            btn = tk.Button(window, text=" ", font=('Helvetica', 20), width=6, height=3,
                            command=lambda row=i, col=j: on_click(row, col))
            btn.grid(row=i, column=j, padx=5, pady=5)
            row_buttons.append(btn)
        buttons.append(row_buttons)
    return buttons

def main():
    global window, board, players, current_player_idx, buttons
    window = tk.Tk()
    window.title("Tic Tac Toe")
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_idx = 0
    buttons = create_board_buttons()
    window.mainloop()

if __name__ == "__main__":
    main()
