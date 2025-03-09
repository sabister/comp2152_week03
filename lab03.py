import random


def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 6:
                return value
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Dice options using list and range
diceOptions = list(range(1, 7))

# Weapons list
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Display available weapons
print("Available Weapons:")
for i, weapon in enumerate(weapons, start=1):
    print(f"{i}. {weapon}")

# Get player inputs
combatStrength = get_valid_input("Enter your combat strength (1-6): ")
mCombatStrength = get_valid_input("Enter monster's combat strength (1-6): ")

# Battle simulation
for j in range(1, 20, 2):
    hero_roll = random.choice(diceOptions)
    monster_roll = random.choice(diceOptions)

    hero_total = combatStrength + hero_roll
    monster_total = mCombatStrength + monster_roll

    hero_weapon = weapons[hero_roll - 1]
    monster_weapon = weapons[monster_roll - 1]

    print(f"\nRound {j}: Hero rolled {hero_roll}, Monster rolled {monster_roll}.")
    print(f"Hero selected: {hero_weapon}, Monster selected: {monster_weapon}.")
    print(f"Hero Total Strength: {hero_total}, Monster Total Strength: {monster_total}.")

    if hero_total > monster_total:
        print("Hero wins the round!")
    elif hero_total < monster_total:
        print("Monster wins the round!")
    else:
        print("It's a tie!")

    if j == 11:
        print("\nBattle Truce declared in Round 11. Game Over!")
        break
