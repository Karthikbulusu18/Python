import random
a = ["hero", "Comedian", "valorant", "srm"]
rand = random.choice(a)
lives = 5
pick = []
print("-----------------------------------------Welcome to hangman!-----------------------------------------------")
while True:
    user = input("Guess a letter:")
    pick.append(user)
    if user in rand:
        print("woah! good one")
    else:
        print("oops guessed it wrong")
        lives -= 1

    all = True
    print()
    for i in rand:
        if i in pick:
            print(i, end="")
        else:
            print("_", end="")
            all = False
    print()

    if all:
        print("you won!")
        exit()

    if lives == 0:
        print("you lost")
        exit()
    else:
        print("you got", lives, "lives")
