import math

player = 'X'
opponent = 'O'

def check_winner(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != ' ':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def is_board_full(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True

def minimax(board, depth, is_maximizing):
    score = check_winner(board)
    if score == player:
        return 10 - depth
    if score == opponent:
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = player
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[row][col] = ' '
        return best
    else:
        best = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = opponent
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[row][col] = ' '
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = player
                move_val = minimax(board, 0, False)
                board[row][col] = ' '
                if move_val > best_val:
                    best_move = (row, col)
                    best_val = move_val
    return best_move

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        if is_board_full(board):
            print("It's a tie!")
            break
        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        if sum(row.count(' ') for row in board) % 2 == 1:
            row, col = find_best_move(board)
            board[row][col] = player
        else:
            row, col = map(int, input("Enter your move (row col): ").split())
            if board[row][col] == ' ':
                board[row][col] = opponent
            else:
                print("Invalid move, try again.")

play_game()
