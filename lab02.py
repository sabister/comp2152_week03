import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

diceOptions = [1, 2, 3, 4, 5, 6]
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Get hero's combat strength
combatStrength = input("Enter your combat Strength (1-6): ")
if combatStrength.isdigit():
    combatStrength = int(combatStrength)
    if combatStrength < 1 or combatStrength > 6:
        print("Invalid input! Combat strength must be between 1 and 6.")
        exit()
else:
    print("Invalid input! Please enter a number between 1 and 6.")
    exit()

# Roll the dice for weapon selection
input("Roll the dice for your weapon (Press enter)")
weaponRoll = random.choice(diceOptions) - 1  # Adjusting index to 0-based
heroWeapon = weapons[weaponRoll]
combatStrength += weaponRoll + 1  # Adding weapon strength to combat strength

print(f"You rolled {weaponRoll + 1} and got {heroWeapon}")

# Evaluate weapon strength
if weaponRoll <= 1:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 3:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

if heroWeapon != "Fist":
    print("Thank goodness you didn't roll the Fist...")
