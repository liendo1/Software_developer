print("*** Welcome to the programmer's cookbook ***")
print("We are going to create a recipe for omelettes.")
name = input("Give your recipe a name (for example 'Awesome Omelette'): ")
print("Your recipe is named: ", name)

#Constant variables
NUM_OF_PERSON = 2
DEFAULT_EGG = 3
DEFAULT_TABLESPOON = 1.5
DEFAULT_BUTTER = 20
DEFAULT_MOUTHS = 3

#User inputs check if these are digits
egg = input(f"For a {NUM_OF_PERSON} person omelette, how many eggs do you need: ")
if not egg.replace('.', '').isdigit():
    print(f"Input '{egg}' is not a valid number. We will set the number of eggs to {DEFAULT_EGG}.")
    egg = DEFAULT_EGG
tableSpoon = input(f"For a {NUM_OF_PERSON} person omelette, how many tablespoons of milk do you need: ")
if not tableSpoon.replace('.', '').isdigit():
    print(f"Input '{tableSpoon}' is not a valid number. We will set the number of tablespoons to {DEFAULT_TABLESPOON}.")
    tableSpoon = DEFAULT_TABLESPOON
butter = input(f"For a {NUM_OF_PERSON} person omelette, how much butter do you need (grams): ")
if not butter.replace('.', '').isdigit():
    print(f"Input '{butter}' is not a valid number. We will set the amount of butter to {DEFAULT_BUTTER} grams.")
    butter = DEFAULT_BUTTER
print("All done!")

# Converting the type of a variable
egg = float(egg)
tableSpoon = float(tableSpoon)
butter = round(float(butter))

print("*** Let's get cooking ***")
print("How many omelettes do you want to make?")
mouths = input("Fill in the number of mouths to feed: ")

#User input to check if it is a digit
if not mouths.isdigit():
    print(f"Input '{mouths}' is not a valid number. We will set the number of people to {DEFAULT_MOUTHS}.")
    mouths = DEFAULT_MOUTHS
mouths = int(mouths)

#Variables for the arithmetics
print(f"For {mouths} poeple you need")
print(f" * {mouths * (egg / NUM_OF_PERSON)} eggs")
print(f" * {mouths * (tableSpoon / NUM_OF_PERSON)} tbsp of milk")
print(f" * {round(mouths * (butter / NUM_OF_PERSON))} grams of butter")

print("""Instructions:
 1. Whisk the eggs with the milk, season with salt and pepper.
 2. Coat a pan with butter and heat over medium heat.
 3. Once the pan is hot, pour in the mixture.
 4. When the egg is cooked, fold the omelette in half with a spatula.
 5. Let the folded omelette brown slightly and serve it on a plate.
Enjoy!""")







