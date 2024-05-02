board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print(' | '.join(board[i*3:(i+1)*3]))

def check_win():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Draw'
    return False

current_player = 'X'
while True:
    print_board()
    move = input(f"Player {current_player}, enter your move (1-9): ")
    if board[int(move) - 1] == ' ':
        board[int(move) - 1] = current_player
        result = check_win()
        if result:
            print_board()
            if result == 'Draw':
                print("It's a draw!")
            else:
                print(f"Player {result} wins!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("Invalid move, try again.")