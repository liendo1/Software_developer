print(" *** Welcome to the programmer's cookbook ***")
print(" We are going to create a recipe for omelettes.")
# User input for the omelette name
name = input(" Give your recipe a name (for example 'Awesome Omelette'): ")
print(" Your recipe is named: ", name)
######################################################
# User input and check if this input is a valid number.
NUM_OF_PERSONS =2
egg = input(" For a " + str(NUM_OF_PERSONS) + " person omelette, how many eggs do you need: ")
if not egg.isdigit():
    print("Input '" + egg + "' is not a valid number. We will set the number of eggs to 3")
    egg = 3
egg = int(egg)
table_spoon = input("For a " + str(NUM_OF_PERSONS) + " person omelette, how many tablespoons of milk do you need: ")
if not table_spoon.isdigit():
    print("Input '" + table_spoon + "' is not a valid number. We will set the number of tablespoons to 1.5.")
    TableSpoon = 1.5
table_spoon = float(table_spoon)
butter = input("For a " + str(NUM_OF_PERSONS) + " person omelette, how much butter do you need (grams): ")
if not butter.isdigit():
    print("Input '" + butter + "' is not a valid number. We will set the amount of butter to 20 grams.")
    butter = 20
butter = float(butter)
######################################################
print("All done!")
print("*** Let's get cooking ***")
print("How many omelettes do you want to make?")
######################################################
# User input and check if this input is a valid number.
poeple = input("Fill in the number of mouths to feed: ")
if not poeple.isdigit():
    print("Input '" + poeple + "' is not a valid number. We will set the number of people to 3.")
    poeple = 3
poeple = int(poeple)
######################################################
# Variable for arithmetic calculation.
egg_one_person = egg / NUM_OF_PERSONS
table_spoon_one_person =table_spoon / NUM_OF_PERSONS
butter_one_person = butter / NUM_OF_PERSONS
# Total for each item calculated with how many people need to be feed.
total_egg = egg_one_person * poeple
total_table_spoon = table_spoon_one_person * poeple
total_butter = butter_one_person * poeple

print("For " + str(poeple) + " people you need:")
print(" * ", total_egg, "eggs")
print(" * ", total_table_spoon, "tbsp of milk")
print(" * ", round(total_butter), "grams of butter")
print("""Instructions:
    1. Whisk the eggs with the milk, season with salt and pepper.
    2. Coat a pan with butter and heat over medium heat.
    3. Once the pan is hot, pour in the mixture.
    4. When the egg is cooked, fold the omelette in half with a spatula.
    5. Let the folded omelette brown slightly and serve it on a plate.
Enjoy!""")
