
contact = {
    'Alice': {'home': '06 123 456 78'},
    'Bob': {'work': '06 321 654 87'},
    'Charlie': {'home': '06 876 543 21', 'work': '088 019 8888'}
}
finish = False

def menu():

    print("""Please select of the following options:
    1. Display contacts
    2. Add a contact
    3. Find a contact
    4. Remove a contact
    0. Exit application
    """)

def option_1():
    print("These are the contacts in the blackbook:")
    for i, (numSearch, phoneinfo) in enumerate(contact.items()):
        print(f"{i}: '{numSearch}'", end='')
        for type, number in phoneinfo.items():
            print(f", {type}: '{number}'", end='')
        print()
    print(f"You have {len(contact)} contacts in your blackbook.")


def option_2():
    contactName = input("what is the new contact name?:")
    typeNumber = input("what is the type of phone number?:")
    phone = input("what is the new contact number?:")
    contact[contactName] = {typeNumber: phone}


def option_3():
    print("How do you want to search for a contact? ")
    print("Please select of the following options: ")
    print("1. Search by name")
    print("2. Search by phone number")

    while True:
        choice = input("Please choose an option 1 or 2: ")
        if choice == '1':
            search_by_name()
            break
        elif choice == '2':
            search_by_number()
            break
        else:
            continue


def search_by_name():
    searching = input("Who are you looking for?:")
    if searching in contact:
        for numSearch, values in contact.items():
            if numSearch == searching:
                print(f"Found: '{numSearch}'", end='')
                for info, phNumber in values.items():
                    print(f", {info}: '{phNumber}'", end=' ')
                print()
    else:
        print(f"No contact found with name '{searching}'")


def search_by_number():
    number = input("Please enter a phone number:")
    lista = []
    for key in contact:
        for secondarykey in contact[key]:
            if contact[key][secondarykey].replace(' ', '') == number.replace(' ', ''):
                name = key
                type = secondarykey
                number = contact[key][secondarykey]
                print(f"Found: '{name}'", end='')
                lista.append(name)
    if len(lista) == 0:
        print(f"No contact found with number '{number}'.")
    else:
        for names in contact:
            if name == names:
                for info in contact[names]:
                    print(f", {info}: '{contact[names][info]}'", end=' ')
                print()



def option_4():
    deleteName = input("Who do you want to remove:")
    if deleteName in contact:
        for name, values in contact.items():
            if name == deleteName:
                print(f"Removed: '{name}'", end='')
                for info, phNumber in values.items():
                    print(f", {info}: '{phNumber}'", end=' ')
                print()
        del contact[deleteName]

    else:
        print(f"No contact found with name '{deleteName}'")



print("*** Welcome to your blackbook ***")
while finish == False:
    while True:
        menu()
        user = input("Please choose an option: ")
        if not user.isdigit():
            print('ERROR: Selection is not a number.')
        elif int(user) < 0 or int(user) >= 5:
            print("ERROR: Number is not between 0 and 4.")
        elif user == "1": #Display contact
            option_1()
        elif user == '2': #Add an contact
            option_2()
        elif user == '3': #Find an contact
            option_3()
        elif user == '4': #Delete an contact
            option_4()
        elif user == '0': #Stop the program
            finish = True
            break





