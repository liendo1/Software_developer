#objectives
PLAYER_LIST = []
MARKERS_LIST = ["X","O"]
GAME_BOARD = ["1","2","3","4","5","6","7","8","9"]
player_index = 1
markers = 0
finish = False


#print the menu
def board():
    lines = " ----------- "
    print(lines)
    for x in range(len(GAME_BOARD)):
        print(f"| {GAME_BOARD[x]} ", end='')
        if (x + 1) % 3 == 0:
            print("|")
            print(lines)


#print for the user to put input
print("*** Welcome to Tic Tac Toe ***")
player_1 = input("Fill the name of player 1:")
player_2 = input("Fill the name of player 2:")
PLAYER_LIST.append(player_1)
PLAYER_LIST.append(player_2)
print(f"These are the players:{PLAYER_LIST}")
print(f"These are their markers:{MARKERS_LIST}")
print("The gameboard looks like this:")
board()

#change players
while finish == False:
        for i in range(len(GAME_BOARD)):
            if (i + 1) % 2 == 0:
                selection = int(input(f"Player {player_index + 1} ('{PLAYER_LIST[player_index]}') please choose a number on the board:"))
            else:
                selection = int(input(f"PLayer {player_index} ('{PLAYER_LIST[player_index - 1]}') please choose a number on the board:"))

        print("ERROR: Selection is not a number.")



#check if there is a winner
#check if there is a draw
