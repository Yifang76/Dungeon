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





nlist = "imp","warlord","dictator"
n = random.choice(nlist)

vlist = "stands","looks","glares"
v = random.choice(vlist)


palist = "saunter","walk","run"
pv = random.choice(palist)

if n == "warlord" or n == "dictator":
    det = str("a")
else:
    det = str("an")

if v == "looks" or v == "glares":
    ex = str("at you")
else:
    ex = str("there ")
t = str(" "+det+" "+n+" "+v+" "+ex+" ")




opo = int(input("As you "+pv+" down the path,"+t+"menacingly. What will you do? "))




#return stops any instructions after it from working; it ends the specific area.
