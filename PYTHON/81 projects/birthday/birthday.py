#birthday paradox simulation

import datetime, random

def getBirthdate(numberOfBirthdays):
    '''Returns a list of number random date objects for birthdays'''
    birthdays = []
    for i in range(numberOfBirthdays):
        #the year is unimportant for our simulation, as long as all
        #birthdays have the same year
        startOfYear = datetime.date(2001,1,1)
        #get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    '''Returns the date object of a birthday that occurs more than once in the birthday list'''
    if len(birthdays) == len(set(birthdays)):
        return None #all the birthday  are unique so return none

    #compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+ 1:]):
            if birthdayA == birthdayB:
                return birthdayA #return the matching birthday.

#Display the intro
print('''Birthday paradox
the birthday paradox shows that in a group n of poeple the odds that two of them have the same birthday is large''')
#set up a tuple of months names in order:
MONTHS = ('JAN','FEB','MAR','APRIL','MAY','JUNE','JULY','AUG','SEP','OKT','NOV','DEC')

while True: # keeps asking until the user enters a valid amount
    print("How many birthdate shall i generate ? (max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <=100):
        numBDays = int(response)
        break # user has entered a valid amount
print()

#generate and display the birthdays
print("Here are ",numBDays,'birthdays:')
birthdays = getBirthdate(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #display a comma for each birthday after the first birthday
        print(', ',end='')
        monthName = MONTHS[birthday.month - 1]
        dateText  = '{} {}'.format(monthName,birthday.day)
        print(dateText,end='')
print()
print()

#determine if there are two birthdays that match
match = getMatch(birthdays)

#display the results
print('in this simulation ',end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiply  poeple have a birthday on ',dateText)
else:
    print("there are no matching birthdays")
print()

#run 100,000 simulations
print('generating', numBDays, 'random birthdays 100,000 times')
input('press enter to begin')

print('lets run another 100,000 simulations')
simMatch = 0 # how many simulations had matching birtdays in them
for i in range(100_000):
    #report on the progresss every 10.000 simulations
    if i % 10_000 == 0:
        print(i, 'simulation run...')
    birthdays= getBirthdate(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100.000 simulations run')

#diplay simulation test
probability = round(simMatch / 100_000 * 100,2)
print('out of 100.000 simulation of ',numBDays,'poeple there was a ')
print('matching birthday in that group ',simMatch,'times this means')
print('that',numBDays, 'poeple have a probability of ',probability,'% chance of ')
print("having a marthing birthday in their group")
print('that is probabily more than you think')