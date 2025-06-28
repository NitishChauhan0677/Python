import random

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_win(board, mark):
    win_combo = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]           
    ]
    return any(board[a] == board[b] == board[c] == mark for a, b, c in win_combo)

def is_draw(board):
    return " " not in board

def player_move(board):
    while True:
        try:
            move = int(input("Your move (1-9): ")) - 1
            if board[move] == " ":
                return move
            else:
                print("That spot is already taken!")
        except (IndexError, ValueError):
            print("Invalid move. Choose a number between 1 and 9.")

def computer_move(board):
    empty = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(empty)

def tic_tac_toe():
    board = [" "] * 9
    player_mark = "X"
    computer_mark = "O"

    print("🎮 Welcome to Tic Tac Toe!")
    print("You are X and Computer is O")
    print_board(board)

    while True:
        move = player_move(board)
        board[move] = player_mark
        print_board(board)

        if check_win(board, player_mark):
            print("🎉 Congratulations! You win!")
            break
        elif is_draw(board):
            print("🤝 It's a draw!")
            break

        print("Computer's turn...")
        move = computer_move(board)
        board[move] = computer_mark
        print_board(board)

        if check_win(board, computer_mark):
            print("💻 Computer wins! Better luck next time.")
            break
        elif is_draw(board):
            print("🤝 It's a draw!")
            break


tic_tac_toe()
