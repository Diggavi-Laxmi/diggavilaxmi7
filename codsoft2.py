import math
board = [' '] * 9
AI = 'O'
YOU = 'X'
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i] + ' | ' + board[i+1] + ' | ' + board[i+2])
    print()
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False
def is_board_full(board):
    return all(cell != ' ' for cell in board)
def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, AI):
        return 1
    elif check_winner(board, YOU):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = AI
                eval = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = YOU
                eval = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval


def best_move(board):
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            move_val = minimax_alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move


def play_game():
    print("Tic Tac Toe - You (X) vs AI (O)")
    print_board(board)

    while True:
        
        user_move = int(input("Enter your move (0-8): "))
        if board[user_move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[user_move] = YOU

        print_board(board)

        if check_winner(board, YOU):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        
        ai_move = best_move(board)
        board[ai_move] = AI
        print("AI chooses:", ai_move)
        print_board(board)

        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
play_game()