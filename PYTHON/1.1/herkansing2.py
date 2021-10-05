
def print_menu():
    print("""
    *** Welcome to Santa's Woodshop ***
    Which one of the following trees would you like to see?
    1. A right-sided tree
    2. A left-sided tree
    3. A normal tree
    0. Make like a tree and leave (exit the application)
    """)
    selection = input("Please enter your selection:")
    while True:
        try:
            if selection == '1':
                right_side_tree(height())
                see_another_tree()
            elif selection == '2':
                left_side_tree(height())
                see_another_tree()
            elif selection == '3':
                normal_tree(height())
                see_another_tree()
            elif selection == '0':
                print("Ho ho ho. See you next time!")
                exit()
            else:
                selection = input("Please select a valid option (0, 1, 2 or 3):")
                continue
        except ValueError:
            selection = input('Please select a valid option (0, 1, 2 or 3):')
            continue




def height():
    return int(input("Please enter the desired height of the tree:"))


def right_side_tree(height):
    print("The right-sided tree looks like this:")
    for i in range(0, height):
        for j in range(0, i + 1):
            print("*", end="")
        print("\r")

def left_side_tree(height):
    print("The left-sided tree looks like this:")
    for i in range(height):
        print(" " * (height - i) + "*" * (i + 1))

def normal_tree(height):
    print("The normal tree looks like this:")
    for i in range(height):
        print(" " * (height - i) + "*" * (i * 2 + 1))


def see_another_tree():
    print("Would you like to see another tree?")
    another_tree = input("Please enter 'yes' or 'no':")
    while True:
        if another_tree.lower() == 'yes':
            print_menu()
        elif another_tree.lower() == 'no':
            exit()
        else:
            another_tree = input("Please select a valid option ('yes' or 'no'):")
            continue
        return another_tree

print_menu()






