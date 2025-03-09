import random

# Define Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Initial combat strength
m_combat_strength = random.randint(1, 3)  # Random initial value between 1 and 3
print(f"Monster's initial combat strength: {m_combat_strength}")

# Roll for Monster's Magic Power
input("Press Enter to roll for the monster's magic power...")
selected_power = random.choice(list(monster_powers.keys()))

# Update Monster's Combat Strength
m_combat_strength = min(m_combat_strength + monster_powers[selected_power], 6)
print(f"Monster used {selected_power}, updated combat strength: {m_combat_strength}")

# Define loot options and player's belt
loot_options = ["Health Potion", "Poison", "Magic Scroll", "Gold Coin", "Shield"]
belt = []


def collect_loot():
    print("You found a loot bag!")
    input("Press Enter to roll for loot...")
    if loot_options:
        loot_item = loot_options.pop(random.randint(0, len(loot_options) - 1))
        belt.append(loot_item)
        print(f"You obtained: {loot_item}")
        print(f"Current belt: {belt}")
    else:
        print("No more loot available.")


# Collect two loot items
collect_loot()
collect_loot()

# Organizing the Loot Belt
print("Organizing loot belt alphabetically...")
belt.sort()
print(f"Organized belt: {belt}")

# Using the first loot item
if belt:
    print("You see a monster in the distance!")
    used_item = belt.pop(0)
    print(f"You used {used_item}!")

    # Define good and bad loot
    good_loot = ["Health Potion", "Shield"]
    bad_loot = ["Poison"]

    # Player's health
    health_points = random.randint(3, 5)  # Random initial health between 3 and 5
    print(f"Initial health points: {health_points}")

    if used_item in good_loot:
        health_points = min(health_points + 2, 6)
        print(f"The item helped! New health points: {health_points}")
    elif used_item in bad_loot:
        health_points = max(health_points - 2, 0)
        print(f"The item was harmful! New health points: {health_points}")
    else:
        print("The item was not helpful.")
else:
    print("No items in belt to use.")
