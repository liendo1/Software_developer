print("*** Welcome to the programmer's cookbook ***")
print("We are going to create a recipe for omelettes.")
Name = input("Give your recipe a name (for example 'Awesome Omelette'): ")
print("Your recipe is named: ")
PersonOmelette = int(input("How many person omelette? "))
Egg = input("For a " + str(PersonOmelette) + " person omelette, how many eggs do you need: ")
if Egg.isdigit() == False:
    print("Input '" + Egg + "' is not a valid number. We will set the number of eggs to 3.")
    Egg = 3
Egg = int(Egg)
TableSpoon = input("For a " + str(PersonOmelette) + " person omelette, how many tablespoons of milk do you need: ")
if TableSpoon.isdigit() == False:
    print("Input '" + TableSpoon + "' is not a valid number. We will set the number of tablespoons to 1.5.")
    TableSpoon = 1.5
TableSpoon = float(TableSpoon)
Butter = input("For a " + str(PersonOmelette) + " person omelette, how much butter do you need (grams): ")
if Butter.isdigit() == False:
    print("Input '" + Butter + "' is not a valid number. We will set the amount of butter to 20 grams.")
    Butter = 20
Butter = float(Butter)
print("All done!")
print("*** Let's get cooking ***")
print("How many omelettes do you want to make?")
Poeple = input("Fill in the number of mouths to feed: ")
if Poeple.isdigit() == False:
    print("Input '" + Poeple + "' is not a valid number. We will set the number of people to 3.")
    Poeple = 3
Poeple = int(Poeple)

# Variable for arithmetic calculation
EggOnePerson = float(Egg / PersonOmelette)
TableSpoonOnePerson = float(TableSpoon / PersonOmelette)
ButterOnePerson = float(Butter / PersonOmelette)

TotalEgg = EggOnePerson * Poeple
TotalTableSpoon = TableSpoonOnePerson * Poeple
TotalButter = ButterOnePerson * Poeple

print("For " + str(Poeple) + " poeple you need:")
print(" * ", TotalEgg, "eggs")
print(" * ", TotalTableSpoon, "tbsp of milk")
print(" * ", round(TotalButter),"grams of butter")
print("""Instructions:
    1. Whisk the eggs with the milk, season with salt and pepper.
    2. Coat a pan with butter and heat over medium heat.
    3. Once the pan is hot, pour in the mixture.
    4. When the egg is cooked, fold the omelette in half with a spatula.
    5. Let the folded omelette brown slightly and serve it on a plate.
Enjoy!""")
