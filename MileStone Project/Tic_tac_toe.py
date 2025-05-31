def display_board(board):
    print()
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print()

def check_win(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))

def manual_input_game():
    board = [' '] * 10  
    display_board(board)

    while True:
        try:
            pos = int(input("Enter position (1-9): "))
            if pos < 1 or pos > 9:
                print("Position must be between 1 and 9.")
                continue

            if board[pos] != ' ':
                print("That position is already filled. Try another one.")
                continue

            mark = input("Enter mark (X or O): ").upper()
            if mark not in ['X', 'O']:
                print("Invalid mark. Enter X or O.")
                continue

            board[pos] = mark
            display_board(board)

            if check_win(board, mark):
                print("Won the Gamee")
                break

            if ' ' not in board[1:]:
                print("It's a draw!")
                break

        except ValueError:
            print("Invalid input. Enter numbers only.")

manual_input_game()
