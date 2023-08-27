print("To-Do list")
Mylist = ["hi", "hello"]

print("1. Add")
print("2 . Remove")
print("3. Edit")
print("4. view")
select = int(input("What do you want to do? Press between 1-4: "))
while True:
    if select == 1:
        adding = input("What do u want to add: ")
        Mylist.append(adding)
        print(Mylist)
        break
    if select == 2:
        print(Mylist)
        removed = int(
            input("What do you want to remove? (select index number): "))
        Mylist.pop(removed)
        print(Mylist)
        break
    if select == 3:
        print(Mylist)
        selected_index = int(input("What index do you want to edit: "))

        if selected_index < 0 or selected_index >= len(Mylist):
            print("Invalid index. The index is out of range.")
        else:
            added = input("What do you want to add: ")
            Mylist[selected_index] = added
            print("List after editing:", Mylist)

    if select == 4:
        print(Mylist)
        break
