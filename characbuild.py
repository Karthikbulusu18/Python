import random
import os
import time


def rollDice(side):
    result = random.randint(1, side)
    return result


def health():
    healthStat = ((rollDice(6)*rollDice(12))/2)+10
    return healthStat


def strength():
    strengthStat = ((rollDice(6)*rollDice(8))/2)+12
    return strengthStat


print("⚔️ CHARACTER BUILDER ⚔️")
print()
name = input("Name your Legend:\n")
type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(name, type)
hero_health = health()
hero_strength = strength()
print("HEALTH:", hero_health)
print("STRENGTH:", hero_strength)
print()
print("May your name go down in Legend…")
print()
print("Whos your character battling with?")

enemy = input("Name of your enemy:")
enemychar = input("Character type (Human, Elf, Wizard,Orc):\n")
print()
print(enemy, enemychar)
enemy_health = health()
enemy_strength = strength()
print("health:", enemy_health)
print("strength:", enemy_strength)
while True:
    print("Let the battle begins...")
    print("Round 1!!!")
    print(name, "Vs", enemy)
    round1 = hero_health - enemy_strength
    round2 = enemy_health - hero_strength
    if round1 < round2:
        print(enemy, "Defeated hero very aggresively")
        break
    else:
        print(name, "defeated the villian and saved the city!!!")
        break

time.sleep(1)
os.system("clear")
