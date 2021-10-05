#Variables
PLAYER_LIST = []
MARKER_LIST = ["X", "O"]
GAME_BOARD = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
finish = False
marker_in_index_list = 0
player_in_index_list = 1
X_WINNING_LIST = ["X","X","X"]
O_WINNING_LIST = ["O","O","O"]


def winning_combinatios():
    if X_WINNING_LIST[0:3] == GAME_BOARD[0:3] or X_WINNING_LIST[0:3] == GAME_BOARD[3:6] or X_WINNING_LIST[0:3] == GAME_BOARD[6:9]:
        return True
    elif X_WINNING_LIST[0:3] == GAME_BOARD[0:7:3] or X_WINNING_LIST[0:3] == GAME_BOARD[1:8:3] or X_WINNING_LIST[0:3] == GAME_BOARD[2:6:3]:
        return True
    elif X_WINNING_LIST[0:3] == GAME_BOARD[0:9:4] or X_WINNING_LIST[0:3] == GAME_BOARD[2:8:2]:
         return True
    elif O_WINNING_LIST[0:3] == GAME_BOARD[0:3] or O_WINNING_LIST[0:3] == GAME_BOARD[3:6] or O_WINNING_LIST[0:3] == GAME_BOARD[6:9]:
        return True
    elif O_WINNING_LIST[0:3] == GAME_BOARD[0:7:3] or O_WINNING_LIST[0:3] == GAME_BOARD[1:8:3] or O_WINNING_LIST[0:3] == GAME_BOARD[2:6:3]:
        return True
    elif O_WINNING_LIST[0:3] == GAME_BOARD[0:9:4] or O_WINNING_LIST[0:3] == GAME_BOARD[2:8:2]:
        return True
    else:
        return False

def draw():
    #count how many numbers are in the gameboard list if there is not number left it prints draw
    for i in GAME_BOARD:
        if i.isdigit():
            return False
    return True

def print_board():
    #print the gameboard
    lines = " ----------- "
    print(lines)
    for x in range(len(GAME_BOARD)):
        print(f"| {GAME_BOARD[x]} ", end='')
        if (x + 1) % 3 == 0:
            print("|")
            print(lines)




print("*** Welcome to Tic Tac Toe ***")
player_one = input("Fill the name of the player 1:")
player_two = input("Fill the name of the player 2:")
PLAYER_LIST.append(player_one)
PLAYER_LIST.append(player_two)
print(f"These are the players: {PLAYER_LIST}")
print(f"These are the markers: {MARKER_LIST}")
print_board()




while finish == False:
    try:
        selection = int(input(f"Player {player_in_index_list} ('{PLAYER_LIST[player_in_index_list - 1]}') please choose a number on the board: "))

        if not 1 <= selection <= 10:
            print("ERROR: Number is not between 1 and 10.")
        elif not GAME_BOARD[selection - 1].isdigit():
            print(f"ERROR: Number {selection} has already been selected (value = {GAME_BOARD[selection - 1]}).")
        else:
            game_board_selection = selection - 1
            GAME_BOARD[game_board_selection] = MARKER_LIST[marker_in_index_list]
            print_board()
            if winning_combinatios():
                print(f"We have a winner! Congratulations player {player_in_index_list} ('{PLAYER_LIST[player_in_index_list - 1]}')")
                finish = True
            if draw() == True:
                print("We have a draw! Thank you for playing.")
                finish = True
            player_in_index_list = (player_in_index_list % 2) + 1
            marker_in_index_list = (marker_in_index_list + 1) % 2

    except ValueError:
        print('ERROR: Selection is not a number.')




