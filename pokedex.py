pokedex = {}


def poke():
    print()
    for key, value in pokedex.items():
        print(key, end=":")
        for subkey, subvalue in value.items():
            print(subkey, subvalue, end="|")
        print()


while True:
    name = input("Name of your pokemon: ")
    type = input("type of pokemon: ")
    hp = int(input("hp:"))
    mp = int(input("mp:"))
    pokedex[name] = {"type": type, "hp": hp, "mp": mp}
    poke()
