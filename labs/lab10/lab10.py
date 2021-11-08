"""
Name: Tripp Modzelewski
lab10.py


Problem: This program will build a tic-tac-toe game

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def display_board(position_list):
    print("-" * 13)
    counter = 0
    for i in range(3):
        print("| ", end="")
        for j in range(3):
            print(position_list[counter], end=" | ")
            counter = counter + 1
        print("\n" + "-" * 13)


def fill_spot(board, spot, marker):
    board[int(spot) - 1] = marker


def legal_spot(board, spot):
    if (board[int(spot) - 1] == "x" or board[int(spot) - 1] == "o") or (int(spot) < 0 or int(spot) > 9):
        return False
    else:
        return True


def game_won(board):
    win_con = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for condition in win_con:
        counter = 0
        for spot in condition:
            if board[spot - 1] == "x":
                counter = counter + 1
            if counter == 3:
                return "x wins"
    for condition in win_con:
        counter = 0
        for spot in condition:
            if board[spot -1] == "o":
                counter = counter + 1
            if counter == 3:
                return "o wins"


def game_over(board, turn_count):
    if game_won(board) == "x wins" or game_won(board) == "o wins" or turn_count >= 10:
        return True
    else:
        return False


def play_game():
    board = build_board()
    display_board(board)
    turn_count = 1
    marker = ''
    while not game_over(board, turn_count):
        spot = input("type spot in which you'd like to play: ")

        if turn_count % 2 == 0:
            marker = 'x'
        else:
            marker = 'o'

        if legal_spot(board, spot) == True:
            fill_spot(board, spot, marker)
            display_board(board)
        elif legal_spot(board, spot) == False:
            print("you cant place there, penalty!")


        if game_won(board) == "x wins":
            print("x wins")
        if game_won(board) == "o wins":
            print("o wins")
        if turn_count == 9:
            print("tie")
        turn_count = turn_count + 1







def main():
    # add other function calls here
    play_game()
    pass


main()
