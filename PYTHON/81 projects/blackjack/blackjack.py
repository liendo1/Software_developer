'''The classic card game also known as 21'''

import random, sys

# set up the constants

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'


def main():
    print("""Black jack
    
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens,  and jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        IN case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.""")
    money = 5000

    while True: #main game loop.
        # check if the player has run out of money:
        if money <= 0:
            print('You are broke')
            print("Good thing you were not playing with real money")
            print("Thansk for playing")
            sys.exit()
            #let the prayer enter their bet for this round:
        print('Money:',money)
        bet = getBet(money)

        #give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop(),deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        #handle player actions
        print('bet:',bet)
        while True: # keep looping until player stands or busts
            displayHands(playerHand,dealerHand,False)
            print()

            # check if the player has bust:
            if getHandValue(playerHand) > 21:
                break

            #get the players move either H,S, or D:
            move = getMove(playerHand, money-bet)

            # handle the player actions:
            if move == 'D':
                #player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet,(money-bet)))
                bet += additionalBet
                print(f'Bet increased to {bet}')
                print('bet',bet)
            if move in ('H','D'):
                #HIT /DOUBLING down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print(f'You drew a {rank} of {suit}')
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    #the player has busted:
                    continue
            if move in ("S",'D'):
                #stand /doubling down stops the playeds turn
                break
        #handle the deals actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # the dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand,dealerHand,False)

                if getHandValue(dealerHand) > 21:
                    break # the dealer has busted
                input('Press enter to continue...')
                print('\n\n')

        #show the final hands:
        displayHands(playerHand,dealerHand,True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        #handle whether the player won lost or tied
        if dealerValue > 21:
            print(f'Dealer busts you win ${bet}')
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("Your lost")
            money -= bet
        elif playerValue == dealerValue:
            print('it is a tie the bet is returned to you')
        input("Press enter to continue")
        print('\n\n')

def getBet(maxbet):
    '''ask the player how much they want to bet for this round'''
    while True: # keep asking until they enter a valid amount
        print(f"How much do you bet (1-{maxbet} or quit")
        bet = input('> ').upper().strip()
        if bet =='QUIT':
            print('thanks for playing')
            sys.exit()
        if not bet.isdecimal():
            continue #if then player did not enter a number ask again

        bet = int(bet)
        if 1 <= bet <= maxbet:
            return bet # player entered a valid bet

def getDeck():
    '''Return a list of (rank,suit) tuples for all 52 cards'''
    deck = []
    for suit in (HEARTS,DIAMONDS,SPADES,CLUBS):
        for rank in range(2,11):
            deck.append((str(rank),suit)) #> add the numbered cards
        for rank in ('J','Q','K','A'):
            deck.append((rank,suit)) #add the face and ace cards
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand,showDealerHand):
    '''show the player's and dealer's cards hid the dealers first card if showdealer hand is false'''
    print()
    if showDealerHand:
        print('Dealer:',getHandValue(dealerHand))
        displayHands(dealerHand)
    else:
        print('Dealer:')
        # hide the dealers first card:
        displayCards([BACKSIDE]+ dealerHand[1:])

    #show the players cards:
    print('player:',getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    '''return the value of the cards face cards are worth 10 axes are worth 11 or 1 this function picks the most suitable ace value
    '''
    value = 0
    numberOfAces = 0

    # add the value for the non-ace cards:
    for card in cards:
        rank = card[0] # card is a tuple like (rank,suit)
        if rank =='A':
            numberOfAces += 1
        elif rank in ('K','Q','J'): #face card are worth 10 points
            value += 10
        else:
            value += int(rank) #numbered cards are worth their number.

    # add the value ofr the aces
    value += numberOfAces #add 1 per ace
    for i in range(numberOfAces):
        #if another 10 can be addes with busting do so:
        if value + 10 <= 21:
            value += 10
    return value

def displayCards(cards):
    '''Display all the cards in the cards list'''
    rows = ['','','','',''] # the text to display on  each row
    for i, card in enumerate(cards):
        rows[0] += ' ___ '#print top line of th card
        if card == BACKSIDE:
            #print a cards back
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            #print the cards front:
            rank, suit = card # the card is a tuple data structure
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

        # Print each row on the screen.
    for row in rows:
        print(row)

def getMove(playerHand,money):
    '''Ask the player for their move and returns 'H' for hit, 'S' for stand and 'D' for double down'''
    while True: # keep looping until the player enters a coorec move
        # determine what moves the player can make:
        moves = ['(H)it','(S)tand']

        #the player can double down on their first move, which we can
        #tell because they will have exacley two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        #get the players move"
        movePromt = ', '.join(moves) + '> '
        move = input(movePromt).upper()
        if move in ('H','S'):
            return move # player has enterd a valid move
        if move == "D" and '(D)ouble down' in moves:
            return move # player entered a vlie move

#iof the program run
if __name__=='__main__':
    main()