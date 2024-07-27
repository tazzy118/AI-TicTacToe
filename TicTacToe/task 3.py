# Random is used for random placement of marker for computer.
import random

# This is the board. Its going to print out a sequence of numbers making it 3x3.
# https://stackoverflow.com/questions/57973399/how-can-i-make-a-board-out-of-a-list
# https://stackoverflow.com/questions/74246738/how-to-make-my-number-board-start-at-1-end-at-9-and-arrange-itself-in-3-rows
board = [str(i) for i in range(1, 10)]
player = "X"
winner = None

# This function will present/show the board
def present_board():
    # Print the board with numbers
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# semi pos is three positions in a row and 2/3 of those will be the iterations,
# that the computer runs over, to see if it has any of those 2 in the semi positions.
semi_pos = [[0, 1, 2], [0, 2, 1], [2, 1, 0],
            [3, 4, 5], [3, 5, 4], [4, 5, 3],
            [6, 7, 8], [6, 8, 7], [7, 8, 6],
            [0, 3, 6], [0, 6, 3], [3, 6, 0],
            [1, 4, 7], [1, 7, 4], [4, 7, 1],
            [2, 5, 8], [2, 8, 5], [5, 8, 2],
            [0, 4, 8], [0, 8, 4], [4, 8, 0],
            [2, 4, 6], [2, 6, 4], [6, 4, 2]]

# This will show all the winning combinations needed to win the game.
# Horizontal, Vertical & Diagonal wins.
win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
              [0, 3, 6], [1, 4, 7], [2, 5, 8],
              [0, 4, 8], [2, 4, 6]]

# This function will play the player turn. Also this would make sure user input is valid (not a int or marker placed in a taken spot).
# If user does an invalid input it'll let them know its an invalid input and print out the board again
def play_turn():
    while True:
        move = input("Where do you want to place your marker (1-9)?")
        if move not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            print("Input not recognised! Try again")
            continue
        elif board[int(move) - 1] != str(move):
            print("Position already taken! Try again.")
            continue
        else:
            move = int(move) - 1
            board[move] = player
            break

#Evaluate the current state of the board. Returns: 10 if the computer wins -10 if the player wins,
# 0 if it's a tie or the game is still ongoing.
def evaluate(board):
    for row in win_combos:
        if board[row[0]] == board[row[1]] == board[row[2]] == 'O':
            return 10  # computer wins
        elif board[row[0]] == board[row[1]] == board[row[2]] == 'X':
            return -10  # Player wins
    if all(cell != str(i + 1) for i, cell in enumerate(board)):
        return 0  # its a Tie
    return None  # Game still going on

# this function is the minmax algorithm.
# my cousin also helped me with this a little https://stackoverflow.com/questions/62222125/i-was-trying-to-implement-the-minimax-algorithm-to-tic-tac-toe-in-python-but-it
def minimax(board, depth, is_maximizing):
    # Base case: Check if the game is over or if maximum depth is reached
    score = evaluate(board)
    if score == 10:  # Computer wins
        return score - depth
    elif score == -10:  # Player wins
        return score + depth
    elif not any(cell.isdigit() for cell in board):  # its a Tie https://stackoverflow.com/questions/51007680/elif-function-error-in-code
        return 0
# I had a lot of help using https://stackoverflow.com/questions/77953482/minimax-function-for-board-game
    if is_maximizing:
        best_score = -float('inf')
        for i, cell in enumerate(board): # https://stackoverflow.com/questions/72047933/accessing-a-value-by-index-in-enumerate-for-loop
            if cell.isdigit():
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = str(i + 1)
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i, cell in enumerate(board):
            if cell.isdigit():
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = str(i + 1)
                best_score = min(best_score, score)
        return best_score
# Had some from cousin & also used this for help https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f
def find_best_move(board):
    best_move = -1
    best_score = -float('inf')
    for i, cell in enumerate(board):
        if cell.isdigit():
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = str(i + 1)
            if score > best_score:
                best_score = score
                best_move = i
    return best_move
# Update computers_go() to use the minimax algorithm.
def computers_go():
    move = find_best_move(board)
    board[move] = "O"

# This function will check for a tie in the game. Then the winner is empty which will stop the game.
# If I want to change my players varibale, I have to declare it as an global variable so it can change with no issues.
# https://forum.edu.cospaces.io/t/question-about-a-logic-in-python-code/7259
def changes_player():
    global player
    if player == "X":
        player = "O"
    else:
        if player == "O":
            player = "X"

# This function will check for a tie in the game.
# Then the winner is empty which will stop the game.
# https://stackoverflow.com/questions/76911791/how-does-string-for-i-string-in-enumeratea-work-in-python
def check_tie():
    global winner
    if all(cell != str(i + 1) for i, cell in enumerate(board)):
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

        if winner == "X" or winner == "O":
            present_board()
            print(winner + " has won!")
            stop_game()
        else:
            check_tie()

# This function is going to stop the game if the player does not want to play anymore.
# User input is converted to lower and if y board is cleared or if n python exits game.
# https://www.codecademy.com/forum_questions/558ae27493767630000004f5
def stop_game():
    global player, winner
    while True:
        play_again = input("Do you want to play again? y/n:")
        if play_again.lower() == "y":
            for i in range(len(board)):
                board[i] = str(i + 1)  # Reset the board with numbers from 1 to 9
            break                      # Browsed through https://stackoverflow.com/questions/71070208/python-play-again & https://www.reddit.com/r/learnpython/comments/q6igew/issue_with_yn_in_python_code/?rdt=62580
        elif play_again.lower() == "n":
            exit()
        elif play_again not in ("y", "n"):
            print("Input not recognised")
            continue
    player = "X"
    winner = None
    run_game()

# This function will loop the game constantly.
# If true is always true it will always display board and play turn.
# https://stackoverflow.com/questions/57980445/programming-tictactoe-error-when-trying-to-check-for-winner
def run_game():
    global winner
    player_1or2 = input("Do you want to play with 1 or 2 players? 1/2:")
    while player_1or2 not in ("1", "2"):
        player_1or2 = input("Try again please.")
    while winner is None:
        if player == "X":
            present_board()
            play_turn()
        elif int(player_1or2) == 1 and player == "O":
            computers_go()
        check_win()
        changes_player()

# this function runs game
run_game()











