import math

# Constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'

# Initialize the board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Print the current state of the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check if the game is over
def is_game_over(board):
    return check_winner(board, PLAYER_X) or check_winner(board, PLAYER_O) or is_board_full(board)

# Check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Check for a winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_X):
        return -1
    if check_winner(board, PLAYER_O):
        return 1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Get the best move for the computer
def get_best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = PLAYER_O
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def play_game():
    board = initialize_board()
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not is_game_over(board):
        # User move
        user_move = input("Enter your move (row and column) separated by space (0, 1, 2): ")
        row, col = map(int, user_move.split())
        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        board[row][col] = PLAYER_X
        print_board(board)

        if is_game_over(board):
            break

        # Computer move
        print("Computer's turn:")
        row, col = get_best_move(board)
        board[row][col] = PLAYER_O
        print_board(board)

    # Display the result
    if check_winner(board, PLAYER_X):
        print("Congratulations! You win!")
    elif check_winner(board, PLAYER_O):
        print("Computer wins! Better luck next time.")
    else:
        print("It's a tie!")

# Start the game
if __name__ == "__main__":
    play_game()
