#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import messagebox
import numpy as np
import random
from time import sleep

# Creates an empty board
def create_board():
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

# Check for empty places on board
def possibilities(board):
    l = []
    
    for i in range(len(board)):
        for j in range(len(board)):
            
            if board[i][j] == 0:
                l.append((i, j))
    return l

# Select a random place for the player
def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return board

# Checks whether the player1ة2 has three
# of their marks in a horizontal row
def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                break
                
        if win == True:
            return win
    return win

# Checks whether the player has three
# of their marks in a vertical row
def col_win(board, player):
    for x in range(len(board)):
        win = True
        
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                break
                
        if win == True:
            return win
    return win

# Checks whether the player has three
# of their marks in a diagonal row
def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win

# Evaluates whether there is a winner or a tie
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if (row_win(board, player) or
            col_win(board, player) or
            diag_win(board, player)):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

# Main function to start the game
def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print("Board after " + str(counter) + " move")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


# root window
root = Tk()
root.title("Tic-Tac-Toe")
board = create_board()
current_player = 1

# Function to handle button click
def button_click(row, col):
    global current_player

    if board[row][col] == 0:
        board[row][col] = current_player
        buttons[row][col].config(text="X" if current_player == 1 else "O", state=DISABLED)
        winner = evaluate(board)
        if winner != 0:
            end_game(winner)
        else:
            current_player = 3 - current_player

# win or lose 
def end_game(winner):
    message = ""
    if winner == -1:
        message = "It's a draw!"
    else:
        message = f"Player {winner} wins!"
    messagebox.showinfo("Game Over", message)
    root.quit()

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(
            root, text="", font=("Helvetica", 24), width=5, height=2,
            command=lambda row=i, col=j: button_click(row, col)
        )
        buttons[i][j].grid(row=i, column=j)

root.mainloop()

print("Winner is: " + str(play_game()))


# In[ ]:





# In[ ]:




