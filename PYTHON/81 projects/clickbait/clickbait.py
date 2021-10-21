'''Clickbait headline generator'''
import random
#set up the constants:
OBJECT_PRONOUNS = ['Her','Him','Them']
POSSESIVE_PRONOUNS = ['Her','His','Their']
PERSONAL_PRONOUNS = ['She','He','They']
STATES = [
        'California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan'
        ]
NOUNS = [
        'Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw', 'Serial Killer', 'Telephone Psychic'
         ]
PLACES = [
            'House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
            'Workplace', 'Donut Shop', 'Apocalypse Bunker'
        ]
WHEN = [
            'Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week'
        ]
def main():
    print('Clickbait Headline Generator')
    print('Created by michael liendo')
    print()

    print('Our website needs to trick poeple into looking at ads!')
    while True:
        print('ENter the number of clickbait headlines to generate')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadlines = int(response)
            break # Exit the loop once a valid number is entered

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1,8)

        if clickbaitType == 1:
            headline = generateAreMillennialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType == 8:
            headline = generateJobAutomatedHeadline()

        print(headline)
    print()
    website = random.choice(['wobsite','blag','facebuuk','googles','facebook','tweedie','pastagram'])

    when = random.choice(WHEN).lower()
    print('Post these to our',website,when,'or you\'re fired!')

#each of these funtions return a different type of headline:
def generateAreMillennialsKillingHeadline():
    noun = random.choice(NOUNS)
    return f'Are Millennials killing the {noun} Industry'


def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return f'Without this {noun}, {pluralNoun} Could kill you {when}'


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f'Big companies hate {pronoun} See how this {state} {noun1} invented a cheaper {noun2}'

def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f'You won not belive what  this {state} {noun} found in {pronoun} {place}'

def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return f'What {pluralNoun1} do not want you to know about {pluralNoun2}'

def generateGiftIdeaHeadline():
    number = random.randint(7,15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return f'{number} gift ideas to give your {noun} from {state}'

def generateReasonsWhyHeadline():
    number1 = random.randint(3,19)
    pluralNoun = random.choice(NOUNS) + 's'
    #number 2 should be no larger than numer1
    number2 = random.randint(1,number1)
    return f'{number1} Reason why {pluralNoun} are more interesting than you think (number {number2} will surprise you)'


def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0,2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return f'this {state} {noun} did not think robot would take {pronoun1} job. {pronoun2} were wrong'
    else:
        return f'this {state} {noun} Did not think robots would take {pronoun1} job {pronoun2} was wrong'


if __name__ == '__main__':
    main()