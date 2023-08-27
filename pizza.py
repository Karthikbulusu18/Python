print("|------------Welcome to pizza HUB!----------------|")
price = 0


def pizza():
    print("|-------------------------------------------------|")
    print("|---------Please Select your choice: -------------|")
    print("|--------------1. Veg pizza ----------------------|")
    print("|--------------2. Non-Veg pizza ------------------|")


def toppings():
    print("You can only choose one topping")
    print("1. Cheese")
    print("2. Tomato")
    print("3. Paneer")
    print("4. chill flakes")
    taken = int(input("Please Select:"))
    if taken == 1 and taken == 2 and taken == 3 and taken == 4:
        print("Good choice!")
    return bill()


def bill():
    print("-----------------Pizza HUB---------------------")
    print()
    print("------------your total bill is: Rs", price, "---------------")
    print()
    print("--------------Thank you!, please visit again---------------")
    print()
    global billContent
    billContent = str(price)


billContent = ""

pizza()
selected = int(input("Enter your choice here: "))
if selected == 1:
    print("1. paneer tikka pizza(extra spicy)")
    print("2. Mushroom pizza")
    print("3. Corn pizza")
    select = int(input("Enter your choice here: "))
    if select == 1:
        print("Great choice!")
        price = 240
        print("do you want to add any toppings to your pizza?")
        sel = input("Y/N: ")
        if sel == "Y":
            toppings()
        else:
            bill()
    elif select == 2:
        print("Good taste!")
        price = 260
        print("do you want to add any toppings to your pizza?")
        sel = input("Y/N: ")
        if sel == "Y":
            toppings()
        else:
            bill()
    elif select == 3:

        print("Great taste!")
        price = 245
        print("do you want to add any toppings to your pizza?")
        sel = input("Y/N: ")
        if sel == "Y":
            toppings()
        else:
            bill()

if selected == 2:
    print("1. chicken tikka pizza(extra spicy)")
    print("2. chicken crispy pizza")
    print("3. Chicken corn pizza")
    select = int(input("Enter your choice here: "))
    if select == 1:
        print("Great choice!")
        price = 340
        print("do you want to add any toppings to your pizza?")
        sel = input("Y/N: ")
        if sel == "Y":
            toppings()
        else:
            bill()
    elif select == 2:
        print("Wonderful")
        price = 440
        print("do you want to add any toppings? ")
        sel = input("Y/N: ")
        if sel == "Y":
            toppings()
        else:
            bill()
    elif select == 3:
        print("Amazing choice")
        price = 320
        print("do you want to add any toppings? ")
        sel = input("Y/N: ")
        if sel == "Y":
            toppings()
        else:
            bill()

with open("bills.txt", "w") as f:
    f.write(billContent)
