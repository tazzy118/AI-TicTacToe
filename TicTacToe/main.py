# Random is used for random placement of marker for computer.
import random

# This is the board. It's going to print out a sequence of numbers making it 3x3.
# https://stackoverflow.com/questions/57973399/how-can-i-make-a-board-out-of-a-list
# https://stackoverflow.com/questions/74246738/how-to-make-my-number-board-start-at-1-end-at-9-and-arrange-itself-in-3-rows
board = [str(i + 1) for i in range(9)]
winner = None

# This function will present/show the board https://stackoverflow.com/questions/74799031/how-does-this-code-to-create-a-board-for-a-tic-tac-toe-game-work
def present_board():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))

# List of winning combinations needed to win the game: Horizontal, Vertical & Diagonal wins.
win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
              [0, 3, 6], [1, 4, 7], [2, 5, 8],
              [0, 4, 8], [2, 4, 6]]

# This function will play the player turn. Also this would make sure user input is valid (not a int or marker placed in a taken spot).
# If user does an invalid input it'll let them know its an invalid input and print out the board again.
# a little help from this https://stackoverflow.com/questions/54860229/python-print-at-a-given-position-from-the-left-of-the-screen
def play_turn(player):
    if player == "X":
        while True:
            move = input("Where do you want to place your marker (1-9)? ")
            if move not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                print("Input not recognised! Try again")
                continue
            elif board[int(move) - 1] in ("X", "O"):
                print("That position is already taken! Try again.")
                continue
            else:
                move = int(move) - 1
                board[move] = player
                break
    else:
        empty_cells = [i for i in range(9) if board[i].isdigit()]
        if not empty_cells:  # Check if there are no more empty cells left
            print("No more moves available. Game is tied.")
            stop_game()
        else:
            move = random.choice(empty_cells)
            print(f"Computer places 'O' at position {move + 1}")
            board[move] = "O"  # Update with the computers marker

# Updated the empty_cells list after each move https://stackoverflow.com/questions/66425508/what-is-the-meaning-of-for-in-range
        empty_cells = [i for i in range(9) if board[i] == "-"]

# This function changes turns/player.
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
            print("The game is a tie")
            stop_game()

# This function checks for a win.
# The loop is checking the list of win combos to see if the sequences and i,r,h are equal to eachother.
def check_win():
    global winner
    for i, h, r in win_combos:
        if board[i] == board[h] == board[r] != '-':
            winner = board[i]
            present_board()
            print(winner + " has won!")
            stop_game()
    check_tie()

# This function is going to stop the game if the player does not want to play anymore.
def stop_game():
    global winner
    while True:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            for i in range(len(board)):
                board[i] = str(i + 1)
            winner = None
            run_game()
            break
        elif play_again.lower() == "n":
            exit()
        else:
            print("Input not recognised")
            continue

# This function will loop the game constantly. If true is always true it will always display board and play turn.
def run_game():
    player = "X"  # Start the game with player X
    while True:
        present_board()
        play_turn(player)
        check_win()
        player = changes_player(player)  # Switch players

run_game()
