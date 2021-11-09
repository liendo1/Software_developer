PAWN_COUNT = 4
MIN_PLAYERS = 2
MAX_PLAYERS = 4
COLORS = ["red", "green", "yellow", "black"]
BOARD_SIZE = 40

import random


def quantityPlayer():
    while True:
        try:
            how_many_players = int(input("With how many players would you like to play [2-4]: "))
            if how_many_players < MIN_PLAYERS or how_many_players > MAX_PLAYERS:
                print("Invalid input")
                continue
            else:
                return how_many_players
        except ValueError:
            print('Invalid input')
            continue


def givePlayerColor(COLORS, quantity):
    count = 0
    playersDictionary = {}
    while count != quantity:
        for color in COLORS:
            player_color = input(f"Choose a color for player #{count + 1} {COLORS}: ")
            if player_color in COLORS:
                playersDictionary[count] = {}
                playersDictionary[count]["color"] = player_color
                playersDictionary[count]["start_position"] = count * 10
                playersDictionary[count]["active_pawn_positions"] = []
                playersDictionary[count]["available_pawn_count"] = 4
                playersDictionary[count]["home_pawn_count"] = 0
                COLORS.remove(player_color)
                count += 1
            else:
                print("Invalid input")
                continue
    return playersDictionary


def gameState(gameDictionary):
    print("Players: ")
    for player in gameDictionary:
        print(
            f"{player}. {gameDictionary[player]['color']} (starting square: {gameDictionary[player]['start_position']}, pawns available: {gameDictionary[player]['available_pawn_count']}, pawns home: {gameDictionary[player]['home_pawn_count']})")
    print('Board')
    for key in gameDictionary:
        for secundary in gameDictionary[key]:
            if secundary == 'active_pawn_positions':
                for numbers in gameDictionary[key][secundary]:
                    print(numbers, ':', gameDictionary[key]['color'])

    if gameDictionary[player]["home_pawn_count"] == 4:
        return False


def check_hit(numberToCheck, gameDictionary):
    for player in gameDictionary:
        if numberToCheck in gameDictionary[player]['active_pawn_positions']:
            gameDictionary[player]['active_pawn_positions'].remove(numberToCheck)
            gameDictionary[player]['available_pawn_count'] = gameDictionary[player]['available_pawn_count'] + 1
            print("You eliminitate another pawn in this position")
        else:
            pass


def main():
    print("*** Mens Erger Je Niet ***")
    quantity = quantityPlayer()
    players = givePlayerColor(COLORS, quantity)
    dice = [5, 6]
    start = True
    while start:
        for player in players:
            choice = random.choice(dice)
            print(f"Player {players[player]['color']}")
            print("You rolled: ", choice, '!')
            # the first to have all four home win
            if gameState(players) == False:
                print(players[player]['color'], 'You won')
                start = False
                break
            # add pieze if the dice is six and available pawn count is not 0 and there is no pieze for this player
            elif choice == 6 and players[player]['available_pawn_count'] != 0 and len(
                    players[player]["active_pawn_positions"]) == 0:
                check_hit(players[player]['start_position'], players)
                players[player]['available_pawn_count'] = players[player]['available_pawn_count'] - 1
                players[player]['active_pawn_positions'].append(players[player]['start_position'])
                print("Placing a pawn on the starting square!")
                break
            elif choice == 6 and players[player]['available_pawn_count'] != 0 and \
                    players[player]["active_pawn_positions"][-1] != players[player]["start_position"]:
                check_hit(players[player]['start_position'], players)
                players[player]['available_pawn_count'] = players[player]['available_pawn_count'] - 1
                players[player]['active_pawn_positions'].append(players[player]['start_position'])
                print("Placing a pawn on the starting square!")
                break
            # Si tin mas ku un pawn den e player let the player choose which one to move
            elif len(players[player]["active_pawn_positions"]) > 1:
                while True:
                    print("The pawn at which square would you like to move? (", end='')
                    for number in players[player]["active_pawn_positions"]:
                        print(number, end=',')
                    print("):", end='')
                    numberChoice = input()
                    if not numberChoice.isdigit() or int(numberChoice) not in players[player]["active_pawn_positions"]:
                        print("Invalid input")
                        continue
                    numberChoice = int(numberChoice)
                    new_number_to_list = numberChoice + choice
                    if new_number_to_list > BOARD_SIZE:
                        how_many_step = new_number_to_list - BOARD_SIZE
                        if how_many_step >= players[player]['start_position']:
                            players[player]['active_pawn_positions'].remove(numberChoice)
                            players[player]['home_pawn_count'] = players[player]['home_pawn_count'] + 1
                            print("One pawn arrived home")
                            break
                        else:
                            check_hit(how_many_step, players)
                            index_to_change = players[player]['active_pawn_positions'].index(numberChoice)
                            players[player]['active_pawn_positions'][index_to_change] = how_many_step
                            print(f"Moving from {numberChoice} to {how_many_step}")
                            break

                    elif numberChoice < players[player]['start_position'] and new_number_to_list >= players[player][
                        'start_position']:
                        players[player]['active_pawn_positions'].remove(numberChoice)
                        players[player]['home_pawn_count'] = players[player]['home_pawn_count'] + 1
                        print("One pawn arrived home")
                        break
                    else:
                        check_hit(new_number_to_list, players)
                        index_to_change = players[player]['active_pawn_positions'].index(numberChoice)
                        players[player]['active_pawn_positions'][index_to_change] = new_number_to_list
                        print(f"Pawn moving from {numberChoice} to {new_number_to_list}")
                        break

            # if dice is no ta 6 anto tin un pieza so  move automatisc esei
            elif len(players[player]['active_pawn_positions']) == 1:
                old_number = players[player]['active_pawn_positions'][0]
                new_number_to_add = old_number + choice
                check_hit(new_number_to_add, players)
                if new_number_to_add > BOARD_SIZE:
                    how_many_step = new_number_to_add - BOARD_SIZE
                    if how_many_step >= players[player]['start_position']:
                        players[player]['active_pawn_positions'].remove(old_number)
                        players[player]['home_pawn_count'] = players[player]['home_pawn_count'] + 1
                        print("One pawn arrived home")
                        break
                    else:
                        check_hit(how_many_step, players)
                        index_to_change = players[player]['active_pawn_positions'].index(old_number)
                        players[player]['active_pawn_positions'][index_to_change] = how_many_step
                        print(f"Moving from {old_number} to {how_many_step}")
                        break
                elif old_number < players[player]['start_position'] and new_number_to_list >= players[player][
                    'start_position']:
                    players[player]['active_pawn_positions'].remove(old_number)
                    players[player]['home_pawn_count'] = players[player]['home_pawn_count'] + 1
                    print("One pawn arrived home")
                    break
                else:
                    players[player]['active_pawn_positions'][0] = new_number_to_add
                    print(f"Moving from {old_number} to {new_number_to_add}")
                    break
            # skip un turn si active pawn ta 0 and choice not 6 or si e lastu index ta meskos ku e start position
            elif (len(players[player]['active_pawn_positions']) == 0 and choice != 6) or (
                    players[player]["active_pawn_positions"][-1] == players[player]["start_position"]):
                print("Turn Skipped")
                break


main()

'''
def main():
    print('*** Mens Erger Je Niet ***')

    players = read_players()

    print('** Players **')
    # TODO: show player numbers and colors

    # TODO: play the game! Don't forget to split up your code into some
    # functions that make sense.

    # TODO: Game finished? Show who's won!


def read_players():
    """Ask the user how many players want to participate, and what colors they want to play. Returns the list of players."""


    # TODO: implement!

    # Each player could be a dictionary similar to this:
    # {
    #     "color": "red",
    #     "start_position": 10,
    #     "active_pawn_positions": [], # no pawns are on the board yet
    #     "available_pawn_count": 4, # all pawns still need a 6 to be thrown to start
    #     "home_pawn_count": 0, # no pawns are home yet
    # }
    # Midway in the game, the dictionary could look like this.
    # {
    #     "color": "red",
    #     "start_position": 10,
    #     "active_pawn_positions": [10, 3], # position 10 is red's start square, position 3 is 7 squares before red's finish
    #     "available_pawn_count": 1, # one pawn still needs a 6 to start
    #     "home_pawn_count": 1, # one pawn is already home safe
    # }
    # Of course, you're also free to organize the game state in some other way.

    #return []


#main()
'''