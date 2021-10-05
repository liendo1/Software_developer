players_list = []
markers_list = ['X', 'O']
game_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
TURN = 0
TOTAL_PLAYER = 2
LINE_OF_X = False
LINE_OF_Y = False

def board():
    lines = "-----------"
    print(lines)
    for x in range(len(game_board)):
        print(f"| {game_board[x]} ", end='')
        if (x + 1) % 3 == 0:
            print("|")
            print(lines)


#def winning_combination():


print("*** Welcome to Tic Tac Toe ***")
player1 = input("Fill in the name of player 1:")
player2 = input("Fill in the name of player 2:")
players_list.append(player1)
players_list.append(player2)

print(f"These are the players: {players_list}")
print(f"These are their markers: {markers_list}")
print("The gameboard looks like this: ")
board()

while True:
    for players in range(len(players_list)):
        selection = input(f"Player {players+1} ('{players_list[players]}') please choose a number on the board:")
        try:
            selection = int(selection)
            if 1 <= selection <= 9:
                if not game_board[selection-1].isdigit():
                    while True:
                        if game_board[selection-1] == "X" :
                            print(f"ERROR: Number {selection} has already been selected (value = X)")
                            selection = input(f"Player {players} ('{players_list[players]}') please choose a number on the board:")
                        else:
                            print(f"ERROR: Number {selection} has already been selected (value = O)")
                            selection = input(f"Player {players} ('{players_list[players]}') please choose a number on the board:")


                else:
                    game_board[selection-1] = markers_list[players]
                    board()
            else:
                print("ERROR: Number is not between 1 and 10.")
        except ValueError:
            print("ERROR: Selection is not a number.")






