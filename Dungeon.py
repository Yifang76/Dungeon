import random

name = input("Name, please ")

print("Knight: Honourable warriors of the Lennish empire, they are extremely strong and are representatives of the law. (Strength: 10, Agility: 3, Dexterity: 8, Health: 7, Perception: 4, Charisma: 6 (Within lawful lands) or 0 (in foreign lands), Intelligence: 5 )")
print("Merchant: (Strength: 1, Agility: 8, Dexterity: 1, Health: 3, Perception: 8, Charisma: 10, Intelligence: 10 )")

classn = input("Pick a class ").capitalize()

def classo(chosen, cl):
    if classn == input(chosen):
        print("Welcome to the game, "+cl+" "+name+".")

classo("Knight", "knight")
classo("Merchant", "merchant")


def noun(one, two, three):
    nlist = one, two, three
    n = random.choice(nlist)
    if n == "warlord" or n == "dictator":
        det = str("a")
    else:
        det = str("an")
    return n


noun("imp","warlord","dictator")

def verb(one, two, three):
    vlist = one, two, three
    v = random.choice(vlist)
    return v

verb("stands","looks","glares")

def playact(one, two, three):
    palist = one, two, three
    pv = random.choice(palist)
    return pv

playact("saunter","walk","run")

print("As you "+pv+" down the path, "+det+ " "+n+ " "+v+ " there menacingly. What will you do? ")





#return stops any instructions after it from working; it ends the specific area.
