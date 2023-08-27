import random
print("BINGO!!")
print()
bingo = []
a = []

for i in range(9):
    b = random.randint(0, 90)
    a.append(b)
a.sort()
bingo = [[a[0], a[1], a[2]],
         [a[3], "Bingo", a[4]],
         [a[5], a[6], a[7]]
         ]
for row in bingo:
    for item in row:
        print(str(item).center(10), end=" ")
        print()
