import tkinter as tk
from tkinter import messagebox

# create window and board
window = tk.Tk()
window.title("Tic Tac Toe")
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = 0


def create_board():
    for i in range(3):
        for j in range(3):
            button = tk.Button(text="", font=("Arial", 50, "bold"), bg="grey",
                               command=lambda row=i, col=j: handle_click(row, col))
            button.grid(row=i, column=j, sticky="nsew")


create_board()


# handle click
def handle_click(row, col):
    global current_player
    if board[row][col] == 0:
        if current_player == 0:
            board[row][col] = "X"
            current_player = 1
        else:
            board[row][col] = "O"
            current_player = 0
        button = window.grid_slaves(row=row, column=col)[0]
        button.config(text=board[row][col])
        check_winner()


def check_winner():
    print("cheking")
    winner = None
    # horizantal
    for col in range(3):
        if board[0][col] == board[1][col] == board[2] and board[0][0] != 0:
            winner = board[0][0]
            break
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[0][0] != 0:
            winner = board[0][0]
            break
            # check diagonals
    if board[0][0] == board[1][1] == board[0][2] and board[0][0] != 0:
        winner = board[0][0]
    elif board[2][0] == board[1][1] == board[0][2] and board[2][0] != 0:
        winner = board[0][0]

    if all([all(row) for row in board]) and winner is None:
        winner = "tie"

    if winner:
        declare_winner(winner)


def declare_winner(winner):
    if winner == "tie":
        message = "its a tie"
    else:
        message = f"player {winner} wins"
        answer = messagebox.askyesno("Game Over", message + " Do you want to restart the game?")

        if answer:
            global board
            board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

            for i in range(3):
                for j in range(3):
                    button = window.grid_slaves(row=i, column=j)[0]
                    button.config(text="")

            global current_player
            current_player = 1
        else:
            window.quit()

window.mainloop()
