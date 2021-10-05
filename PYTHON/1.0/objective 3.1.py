
print("*** Welcome to the programmer's cookbook ***")
print("We are going to create a recipe for omelettes.")
Name = input("Give your recipe a name (for example 'Awesome Omelette'): ")
print("Your recipe is named: ")
People = int(input("How many people: "))
Egg = input("For a " + str(People) + " person omelette, how many eggs do you need: ")
if Egg.isdigit() == False:
    print("Input " + Egg + " is not a valid number. We will set the number of eggs to 3.")
    Egg = 3
Egg = int(Egg)
TableSpoon = input("For a " + str(People) + " person omelette, how many tablespoons of milk do you need: ")
if TableSpoon.isdigit() == False:
    print("Input " + TableSpoon + " is not a valid number. We will set the number of tablespoons to 1.5.")
    TableSpoon = 1.5
TableSpoon = int(TableSpoon)
Butter = input("For a " + str(People) + " person omelette, how much butter do you need (grams): ")
if Butter.isdigit() == False:
    print("Input " + Butter + " is not a valid number. We will set the amount of butter to 20 grams.")
    Butter = 20
print("All done!")
