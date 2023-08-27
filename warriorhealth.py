import random
name = str(input("Enter your warrior name:"))


def game():
    SixDice = random.randint(1, 6)
    EightDice = random.randint(1, 8)
    health = (SixDice)*(EightDice)
    print("The great", name, "has", health, "HP")


game()
