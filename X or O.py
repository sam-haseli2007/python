# tictactoe.py

from board import create_board, display_board, is_valid_move, make_move, check_winner

def main():
    board = create_board()
    current_player = 'X'

    while True:
        display_board(board)
        row = int(input(f"Player {current_player}, enter the row (0-2): "))
        col = int(input(f"Player {current_player}, enter the column (0-2): "))

        if is_valid_move(board, row, col):
            make_move(board, row, col, current_player)
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            else:
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()