import datetime
import os
import time

print("------------MyDiary------------")
date = datetime.date.today()
file_name = 'diary.txt'
name = input("Enter your name: ")
print("Welcome", name)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def view():
    print(date)
    with open(file_name, 'r', encoding='utf-8') as my_file:
        print(my_file.read())
    input("Press Enter to continue...")
    clear_screen()


def add():
    print(date)
    entry = input('Type here... ')
    with open(file_name, 'a', encoding='utf-8') as my_file:
        my_file.write(f'{date}\n{entry}\n\n')
    print("Entry added successfully!")
    time.sleep(1)
    clear_screen()


def note():
    print("1. Add")
    print("2. View")
    b = int(input("Select your choice: "))
    if b == 1:
        add()
    elif b == 2:
        view()
    else:
        print("Enter valid choice")
        time.sleep(1)
        clear_screen()
        note()


def diary():
    a = int(input("Please enter your password: "))
    password = 12345678
    if a == password:
        note()
    else:
        print("Wrong password, Try again")
        time.sleep(1)
        clear_screen()
        diary()


diary()
