# Random is used for random placement of marker for computer.
import random

# This is the board. Its going to print out a sequence of numbers making it 5x5.
board = [str(i) for i in range(1, 26)]
player = "X"
winner = None

# This function will present/show the board
def present_board():
    # Print the board with numbers
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4])
    print(board[5] + ' | ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[10] + '| ' + board[11] + '| ' + board[12] + '| ' + board[13] + '| ' + board[14])
    print(board[15] + '| ' + board[16] + '| ' + board[17] + '| ' + board[18] + '| ' + board[19])
    print(board[20] + '| ' + board[21] + '| ' + board[22] + '| ' + board[23] + '| ' + board[24])

# semi pos is five positions in a row and 4/5 of those will be the iterations,
# that the computer runs over, to see if it has any of those 4 in the semi positions.
semi_pos = [[0, 1, 2, 3, 4], [0, 2, 1, 3, 4], [4, 3, 2, 1, 0],
            [5, 6, 7, 8, 9], [5, 7, 6, 8, 9], [9, 8, 7, 6, 5],
            [10, 11, 12, 13, 14], [10, 12, 11, 13, 14], [14, 13, 12, 11, 10],
            [15, 16, 17, 18, 19], [15, 17, 16, 18, 19], [19, 18, 17, 16, 15],
            [20, 21, 22, 23, 24], [20, 22, 21, 23, 24], [24, 23, 22, 21, 20],
            [0, 5, 10, 15, 20], [0, 10, 5, 15, 20], [20, 15, 10, 5, 0],
            [1, 6, 11, 16, 21], [1, 11, 6, 16, 21], [21, 16, 11, 6, 1],
            [2, 7, 12, 17, 22], [2, 12, 7, 17, 22], [22, 17, 12, 7, 2],
            [3, 8, 13, 18, 23], [3, 13, 8, 18, 23], [23, 18, 13, 8, 3],
            [4, 9, 14, 19, 24], [4, 14, 9, 19, 24], [24, 19, 14, 9, 4],
            [0, 6, 12, 18, 24], [0, 12, 6, 18, 24], [24, 18, 12, 6, 0],
            [4, 8, 12, 16, 20], [4, 12, 8, 16, 20], [20, 16, 12, 8, 4]]

# This will show all the winning combinations needed to win the game.
# Horizontal, Vertical & Diagonal wins.
win_combos = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14],
              [15, 16, 17, 18, 19], [20, 21, 22, 23, 24],
              [0, 5, 10, 15, 20], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22],
              [3, 8, 13, 18, 23], [4, 9, 14, 19, 24],
              [0, 6, 12, 18, 24], [4, 8, 12, 16, 20]]

# This function will play the player turn. Also this would make sure user input is valid (not a int or marker placed in a taken spot).
# If user does an invalid input it'll let them know its an invalid input and print out the board again
def play_turn():
    global player
    while True:
        move = input("Where do you want to place your marker (1-25)?")
        if move not in [str(i) for i in range(1, 26)]:
            print("Input not recognised! Try again")
            continue
        elif board[int(move) - 1] != str(move):
            print("Position already taken! Try again.")
            continue
        else:
            move = int(move) - 1
            board[move] = player
            change_player()  # Update player after the move
            break

# Evaluate the current state of the board. Returns: 10 if the computer wins, -10 if the player wins,
# 0 if it's a tie or the game is still ongoing
def evaluate(board):
    for row in win_combos:
        if all(board[i] == 'O' for i in row):
            return 10  # computer wins
        elif all(board[i] == 'X' for i in row):
            return -10  # Player wins
    if all(cell != str(i + 1) for i, cell in enumerate(board)):
        return 0  # its a Tie
    return None  # Game still ongoing

# This function implements the minimax algorithm with alpha-beta pruning
# https://tonypoer.io/2016/10/28/implementing-minimax-and-alpha-beta-pruning-using-python/
def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)
    if score is not None:
        return score
# Had some help from this https://stackoverflow.com/questions/34327622/alpha-beta-checkers-same-player-always-wins
    if is_maximizing:
        best_score = -float('inf')
        for i, cell in enumerate(board):
            if cell.isdigit():
                board[i] = 'O'
                best_score = max(best_score, minimax(board, depth + 1, False, alpha, beta))
                board[i] = str(i + 1)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float('inf')
        for i, cell in enumerate(board):
            if cell.isdigit():
                board[i] = 'X'
                best_score = min(best_score, minimax(board, depth + 1, True, alpha, beta))
                board[i] = str(i + 1)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

# This function finds the best move for the computer using the minimax algorithm with alpha-beta pruning
# https://stackoverflow.com/questions/67952011/minimax-works-fine-but-alpha-beta-prunning-doesnt
def find_best_move(board):
    best_move = -1
    best_score = -float('inf')
    alpha = -float('inf')
    beta = float('inf')
    for i, cell in enumerate(board):
        if cell.isdigit():
            board[i] = 'O'
            score = minimax(board, 0, False, alpha, beta)
            board[i] = str(i + 1)
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Update the computer's turn to use the minimax algorithm
def computers_go():
    print("Computer's turn")
    move = find_best_move(board)
    board[move] = "O"

# If I want to change my players varibale, I have to declare it as an global variable so it can change with no issues.
def change_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

# This function checks for a tie
# https://stackoverflow.com/questions/76911791/how-does-string-for-i-string-in-enumeratea-work-in-python
def check_tie():
    global winner
    if all(cell != str(i + 1) for i, cell in enumerate(board)):
        winner = " "
        print("The game is a tie")
        stop_game()

# This function checks for a win.
# The loop is checking the list of win combos to see if the sequences and that they are equal to eachother.
def check_win():
    global winner
    for row in win_combos:
        if all(board[i] == 'X' for i in row):
            winner = 'X'
            present_board()
            print("X has won!")
            stop_game()
        elif all(board[i] == 'O' for i in row):
            winner = 'O'
            present_board()
            print("O has won!")
            stop_game()
    check_tie()

# This function is going to stop the game if the player does not want to play anymore.
# User input is converted to lower and if y board is cleared or if n python exits game.
# https://www.codecademy.com/forum_questions/558ae27493767630000004f5
def stop_game():
    global winner
    while True:
        play_again = input("Do you want to play again? y/n:")
        if play_again.lower() == "y":
            for i in range(len(board)):
                board[i] = str(i + 1)  # Reset the board with numbers from 1 to 25
            break                       # had some help https://stackoverflow.com/questions/71070208/python-play-again
        elif play_again.lower() == "n":  # also had some help from https://www.reddit.com/r/learnpython/comments/q6igew/issue_with_yn_in_python_code/?rdt=62580
            exit()
        elif play_again not in ("y", "n"):
            print("Input not recognised")
            continue
    player = "X"
    winner = None
    run_game()

# This function will loop the game constantly.
# # If true is always true it will always display board and play turn.
# https://stackoverflow.com/questions/57980445/programming-tictactoe-error-when-trying-to-check-for-winner
def run_game():
    global winner
    player_1or2 = input("Do you want to play with 1 or 2 players? 1/2:")
    while player_1or2 not in ("1", "2"):
        player_1or2 = input("Try again please.")
    while winner is None:
        present_board()
        if player == "X":
            play_turn()
        elif player == "O":
            computers_go()
        check_win()
        change_player()
    # Print final board after game ends
    present_board()

# this function runs game
run_game()