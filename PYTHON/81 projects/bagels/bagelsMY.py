#main variables
import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random numbers"""
    numbers= list('0123456789') # create a list of numbers between 0 and 9
    random.shuffle(numbers) #shuffels them intio random order

    #get the first num_digitsa in the list for the secret number:
    secretNum= ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    '''Return a string with the pico,fermi, bagels clues for a guess and secret number pair'''
    if guess == secretNum:
        return 'You got it'

    cluess=[]

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit is in the correct place
            cluess.append('Fermi')
        elif guess[i] in secretNum:
            # a correct digit is in the inclrrect place
            cluess.append("Pico")

    if len(cluess) == 0:
        return 'Bagels'

    else:
        cluess.sort()
        #make a single string from the list of string clues
        return ''.join(cluess)





def main():
    print("Bagels a deductive logic game.")
    print(f"I am thinking of a {NUM_DIGITS} number. Try to guess what it is.")
    print("Here are some clues:")
    print('''
When i say:   That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct but in the right position.
    Bagels      No digit is correct.''')
    while True:#main game loop
        #this stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print("I have thought up a number")
        print(f"You have {MAX_GUESSES} guesses to get it")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess=''
            #keep looping until the user enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}')
                guess = input('> ')

            clues = getClues(guess,secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("you ran out of guesses")
                print(f'the answer was {secretNum}')

        print("Do you want to play again yes or no")
        if not input("> ").lower().startswith('y'):
            break
    print("thanks for playing")





if __name__== '__main__':
    main()
