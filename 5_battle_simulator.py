import random

# Define characters with simple dictionaries
hero = {
    "name": "Hero",
    "health": 100,
    "attack": 15,
    "companion": "Dragon",
    "companion_attack": 10
}

villain = {
    "name": "Villain",
    "health": 120,
    "attack": 20,
    "companion": "Minions",
    "companion_attack": 7
}

def get_total_attack(character):
    # Add base attack and companion attack
    return character["attack"] + character["companion_attack"]

def attack(attacker, defender):
    # Calculate damage with random variation
    total_attack = get_total_attack(attacker)
    damage = random.randint(total_attack - 5, total_attack + 5)
    defender["health"] = defender["health"] - damage
    if defender["health"] < 0:
        defender["health"] = 0
    print(attacker["name"], "and", attacker["companion"], "attack for", damage, "damage!")
    print(defender["name"], "health is now", defender["health"])

def battle():
    print("Battle begins!")
    while True:
        # Hero attacks first
        attack(hero, villain)
        if villain["health"] == 0:
            print("Villain is defeated! Hero wins!")
            break
        
        # Villain attacks next
        attack(villain, hero)
        if hero["health"] == 0:
            # Make sure Hero always survives
            hero["health"] = 1
            print("Hero is almost defeated but still alive!")

battle()
