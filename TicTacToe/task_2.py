# Random is used for random placement of marker for computer.
import random

# This will show the board with numbers representing each cell.
# https://stackoverflow.com/questions/57973399/how-can-i-make-a-board-out-of-a-list
# https://stackoverflow.com/questions/74246738/how-to-make-my-number-board-start-at-1-end-at-9-and-arrange-itself-in-3-rows
board = [str(i + 1) for i in range(9)]
winner = None

# This will show all the winning combinations needed to win the game. Horizontal, Vertical & Diagonal wins.
win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
              [0, 3, 6], [1, 4, 7], [2, 5, 8],
              [0, 4, 8], [2, 4, 6]]

# This function will present/show the board
def present_board():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))

# This function will play the player turn. Also this would make sure user input is valid (not a int or marker placed in a taken spot).
# If user does an invalid input it'll let them know its an invalid input and print out the board again.
def play_turn(player):
    if player == "X":  # (Your) Player's turn
        while True:
            move = input("Where do you wish to place your marker (1-9)? ")
            if move not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                print("Input not recognised! Please try again.")
                continue
            elif board[int(move) - 1] in ("X", "O"):
                print("That position is already taken! Please try again.")
                continue
            else:
                move = int(move) - 1
                board[move] = player
                break
    else:  # Computer player's turn
        empty_cells = [i for i in range(9) if board[i].isdigit()]
        if not empty_cells:
            print("No more moves available. The game is tied.")
            stop_game()
        else:
            move = computer_move()
            print(f"The computer places 'O' at position {move + 1}")
            board[move] = "O"

# This function is to determine computer's move based on rules for task 2. I also had some help from my cousin with this.
def computer_move():
    # Rule 1 = Check if there's a move to win the game
    for i, h, r in win_combos:
        if board[i] == board[h] == "O" and board[r].isdigit():
            return r
        elif board[h] == board[r] == "O" and board[i].isdigit():
            return i
        elif board[i] == board[r] == "O" and board[h].isdigit():
            return h
    # Rule 2 = Check if there's a move to block the opponent's game
    for i, h, r in win_combos:
        if board[i] == board[h] == "X" and board[r].isdigit():
            return r
        elif board[h] == board[r] == "X" and board[i].isdigit():
            return i
        elif board[i] == board[r] == "X" and board[h].isdigit():
            return h
    # Rule 3 = Claim the central space if it's unoccupied
    if board[4].isdigit():
        return 4
    # Rule 4: Otherwise, place the marker on any empty cell
    return random.choice([cell for cell in range(9) if board[cell].isdigit()])

# This function changes turns/player. https://forum.edu.cospaces.io/t/question-about-a-logic-in-python-code/7259
def changes_player(player):
    if player == "X":
        return "O"
    else:
        return "X"

# This function will check for a tie in the game. Then the winner is empty which will stop the game.
def check_tie():
    global winner
    if "-" not in board:
        if not any(cell.isdigit() for cell in board):
            winner = " "
            print("The game is tied.")
            stop_game()

# This function checks for a win.
# The loop is checking the list of win combos to see if the sequences and i,r,h are equal to eachother.
def check_win():
    global winner
    for i, h, r in win_combos:
        if board[i] == board[h] == board[r] != '-':
            winner = board[i]
            present_board()
            print(f"{winner} has won!")
            stop_game()
    check_tie()

# This function is going to stop the game if the player does not want to play anymore.
# User input is converted to lower and if y board is cleared or if n python exits game.
# https://www.codecademy.com/forum_questions/558ae27493767630000004f5
def stop_game():
    global winner
    while True:
        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() == "y":
            for i in range(len(board)):
                board[i] = str(i + 1)
            winner = None
            run_game()
            break
        elif play_again.lower() == "n":
            exit()
        else:
            print("Input not recognised.")
            continue

# This function will loop the game constantly. If true is always true it will always display board and play turn.
def run_game():
    player = "X"  # start the game with player X
    while True:
        present_board()
        play_turn(player)
        check_win()
        player = changes_player(player)  # Switches players

# This function runs game
run_game()
