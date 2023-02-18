import random

name = input("Name, please ").capitalize()
print("Knight: Honourable warriors of the Lennish empire, they are extremely strong and are representatives of the law. (Strength: 10, Agility: 3, Dexterity: 8, Health: 7, Perception: 4, Charisma: 6 (Within lawful lands) or 0 (in foreign lands), Intelligence: 5 )")
print("Merchant: (Strength: 1, Agility: 8, Dexterity: 1, Health: 3, Perception: 8, Charisma: 10, Intelligence: 6 )")

classn = input("Pick a class ").capitalize()

if classn == "Knight":
    print("Welcome, knight "+name+".")
    Str = int(10)
    Agi = int(3)
    Dex = int(8)
    Hea = int(7)
    Per = int(4)
    Cha = int(6)
    Int = int(5)
    TotHea = int(70)


if classn == "Merchant":
    print("Welcome, merchant "+name+".")
    Str = int(1)
    Agi = int(8)
    Dex = int(1)
    Hea = int(3)
    Per = int(8)
    Cha = int(10)
    Int = int(6)
    TotHea = int(30)


adlist = "common","rare","mythical","legendary"
ad = random.choice(adlist)

itemlist = "axe","sword","stick"
item = random.choice(itemlist)

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

if opo == 1:
    if n == "warlord" or n == "dictator" or n == "imp":
        if Str >= 7 and Dex >= 5:
            chance = random.randint(1,2)
            if chance == 1:
                print("You triumph over the "+n+". You gain nothing.")
            if chance == 2:
                print("You triumph over the "+n+". You gained a "+ad+" "+item+".")
        else:
            nTotHea = int(TotHea) - random.randint(1,TotHea)
            nTotHea = str(nTotHea)
            TotHea = str(TotHea)
            print("You lost. HP falls from "+TotHea+" to "+nTotHea)


#return stops any instructions after it from working; it ends the specific area.
