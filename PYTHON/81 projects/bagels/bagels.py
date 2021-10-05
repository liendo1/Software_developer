import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def getSecretNum():
    '''Return a string made of NUM_DIGITS unique random digits.'''
    numbers= list('0123456789') # create a list of digits 0 to 9
    random.shuffle(numbers) #shuffles them into random order

    # get the first NUM_DIGITS in the list for the secret number:
    secretNum= ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    '''returns  a string pico, fermi, bagels clues for a guess and a secret number pair'''
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit is in the correct place
            clues.append("Fermi")
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place
            clues.append('Pico')
    if len(clues) == 0:
        return "Bagels" #there is no corrects digit at all
    else:
        #sort the clues into alphabetical order so their original order does not give information away
        clues.sort()
        #make a single string from the list of string clues
        return ' '.join(clues)














def main():
    print(f"I am thinking of a {NUM_DIGITS} with no repeated digits")
    print("try to guess what it is. Here are some clues:")
    print('''
    when i say :    that means:
        pico            One digit is correct but in the wrong position.
        Fermi           One digit is correct and in the right position.
        Bagels          No digit is correct
        
for example if the secret number was 248 and your guess was 843 , the clues would be Fermi Pico''')

    #main code
    while True: # Main game loop
    #This stores  the secret number the player needs to guess:
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print(f'you have {MAX_GUESSES} guesses to get it.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            #keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}')
                guess = input("> ")
            clues = getClues(guess,secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # they are correct , so break out of this loop
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secretNum}")
        # ask the player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith('y'):
            break
    print("thanks for playing")



if __name__ == '__main__':
     main()





