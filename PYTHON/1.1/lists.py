playersList = []
markersList = ['X', 'O']
gameBoard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
playerTurn = 0
drawn = 0
WINNING = False
playerNumber = 1

def board():
    lines = "-----------"
    print(lines)
    for x in range(len(gameBoard)):
        print(f"| {gameBoard[x]} ", end='')
        if (x + 1) % 3 == 0:
            print("|")
            print(lines)

    #print("-----------")
    #print(f"| {gameBoard[0]} | {gameBoard[1]} | {gameBoard[2]} |")
    #print("-----------")
    #print(f"| {gameBoard[3]} | {gameBoard[4]} | {gameBoard[5]} |")
    #print("-----------")
    #print(f"| {gameBoard[6]} | {gameBoard[7]} | {gameBoard[8]} |")
    #print("-----------")


def winning_arrangment(gameBoard):
        x_line = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        o_line = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        playerNumber = playerTurn + 1
        #winning possibilities x in row direction
        if gameBoard[0] == x_line[0] and gameBoard[1] == x_line[1] and gameBoard[2] == x_line[2]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        elif gameBoard[3] == x_line[3] and gameBoard[4] == x_line[4] and gameBoard[5] == x_line[5]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        elif gameBoard[6] == x_line[6] and gameBoard[7] == x_line[7] and gameBoard[8] == x_line[8]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        #winning possibilities x in column direction
        elif gameBoard[0] == x_line[0] and gameBoard[3] == x_line[3] and gameBoard[6] == x_line[6]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        elif gameBoard[1] == x_line[1] and gameBoard[4] == x_line[4] and gameBoard[7] == x_line[7]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        elif gameBoard[2] == x_line[2] and gameBoard[5] == x_line[5] and gameBoard[7] == x_line[7]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        #winning possibilities x in diagonal direction
        elif gameBoard[0] == x_line[0] and gameBoard[4] == x_line[4] and gameBoard[8] == x_line[6]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        elif gameBoard[6] == x_line[6] and gameBoard[4] == x_line[4] and gameBoard[2] == x_line[2]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        #winning possibilities y in row direction
        elif gameBoard[0] == o_line[0] and gameBoard[1] ==  o_line[1] and gameBoard[2] == o_line[2]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        elif gameBoard[3] == o_line[3] and gameBoard[4] == o_line[4] and gameBoard[5] == o_line[5]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        elif gameBoard[6] == o_line[6] and gameBoard[7] == o_line[7] and gameBoard[8] == o_line[8]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        #winning possibilties y in column
        elif gameBoard[0] == o_line[0] and gameBoard[3] ==  o_line[3] and gameBoard[6] == o_line[6]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        elif gameBoard[1] == o_line[1] and gameBoard[4] == o_line[4] and gameBoard[7] == o_line[7]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        elif gameBoard[2] == o_line[2] and gameBoard[5] == o_line[5] and gameBoard[7] == o_line[7]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        #winning possibilities y in diagonal
        elif gameBoard[0] == o_line[0] and gameBoard[4] ==  o_line[4] and gameBoard[6] == o_line[6]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()
        elif gameBoard[6] == o_line[6] and gameBoard[4] == o_line[4] and gameBoard[2] == o_line[2]:
            print(f"We have a winner! Congratulations player {playerNumber} ('{playersList[playerTurn]}')")
            WINNING = True
            exit()





print("*** Welcome to Tic Tac Toe ***")
player1 = input("Fill in the name of player 1:")
player2 = input("Fill in the name of player 2:")
playersList.append(player1)
playersList.append(player2)
    print(f"These are the players: {playersList}")
    print(f"These are their markers: {markersList}")
    print("The gameboard looks like this: ")
board()



while True:
    selection = input(f"Player {playerNumber} ('{playersList[playerTurn]}') please choose a number on the board:")
    try:
        selection = int(selection)
        if not 1 < selection > 10:
            list_index = selection - 1
            if gameBoard[list_index] == "X":
                print(f"ERROR: Number {selection} has already been selected (value = X).")
                playerTurn = 1
                playerNumber = 2
                continue
            elif gameBoard[list_index] == "O":
                print(f"ERROR: Number {selection} has already been selected (value = O).")
                playerTurn = 0
                playerNumber = 1
                continue
            else:
                gameBoard[list_index] = markersList[playerTurn]
                print("The gameboard looks like this: ")
                board()
                winning_arrangment(gameBoard)
                drawn = drawn + 1
                if drawn == 9 and WINNING == False:
                    print("We have a draw! Thank you for playing.")
                    exit()
                else:
                    if playerTurn == 0:
                        playerTurn = playerTurn + 1
                        playerNumber = 2
                    else:
                        playerTurn = playerTurn - 1
                        playerNumber = 1
        else:
            print("ERROR: Number is not between 1 and 10.")
    except ValueError:
        print("ERROR: Selection is not a number.")
        continue
