import random

name = input("Name, please ").capitalize()
print("Knight: Honourable warriors of the Lennish empire, they are extremely strong and are representatives of the law. (Strength: 10, Agility: 3, Dexterity: 8, Health: 7, Perception: 4, Charisma: 6 (Within lawful lands) or 0 (in foreign lands), Intelligence: 5 )")
print("Merchant: (Strength: 1, Agility: 8, Dexterity: 1, Health: 3, Perception: 8, Charisma: 10, Intelligence: 6 )")
print("Summoner: (Strength: 1, Agility: 4, Dexterity: 1, Health: 2, Perception: 9, Charisma: 2, Intelligence: 8 )")
attriQuery = input("Would you like a guide on the attributes? ").capitalize()
if attriQuery == "Yes":
    print("Strength determines the base damage you do, Agility determines your evasion, Dexterity determines ______, Perception determines your critical chance, Charisma determines your barter rate and speech, Intelligence determines your spellcraft and Health determines your starting health.")

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

if classn == "Summoner":
    print("Welcome, summoner "+name+".")
    Str = int(1)
    Agi = int(4)
    Dex = int(1)
    Hea = int(2)
    Per = int(9)
    Cha = int(2)
    Int = int(8)
    TotHea = int(20)
    summonNumber = int(0)
    


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
    ex = str("there")
t = str(" "+det+" "+n+" "+v+" "+ex+" ")

def fight(noun, StrReq, DexReq, eStr, eDex):
    global TotHea
    opo = int(input("As you "+pv+" down the path,"+t+"menacingly. What will you do? "))
    if opo == 1:
        if n == noun:
            if Str >= StrReq and Dex >= DexReq:
                TotHea == str(TotHea)
                #print("You have "+TotHea+".")
                #print("Minigame starting")
                print("Rules: you are given a number between 1 and 10. If you get within 1 digit of the original number, you deal a fatal wound (which does the highest damage). Three digits difference leads to a body hit (which does mediocre damage) and finally anything over a three number difference will be a miss")
                while TotHea > 0:
                    if eTotHea > 0:
                        guess = random.randint(1,10)
                        print(guess)
                        pguess = int(input("What do you believe the number is? "))
                        if pguess == int(guess) or pguess == int(guess) - int(1) or pguess == int(guess) + int(1):
                            td = int(Str) + int(Dex) + int(2)
                            td = str(td)
                            print("Critical hit! You deal "+td+" against your enemy.")
                        if pguess == int(guess) - int(2) or pguess == int(guess) + int(2):
                            td = int(Str) + int(Dex) - int(1)
                            td = str(td)
                            print("Mediocre hit. You deal "+td+" against your enemy.")
                        if pguess <= int(guess) - int(3) or pguess >= int(guess) + int(3):
                            td = int(Str) + int(Dex) - int(5)
                            td = str(td) 
                            print("Weak hit. You deal "+td+" against your enemy")
                            
                        eguess = random.randint(1,10)
                        if eguess == int(guess) or eguess == int(guess) - int(1) or eguess == int(guess) + int(1):
                            etd = int(eStr) + int(eDex) + int(2)
                            etd = str(etd)
                            TotHea = int(TotHea) - int(etd)
                            TotHea = str(TotHea)
                            print("Critical hit! Your enemy deals "+etd+" to you, leaving you with "+TotHea+" left.")
                        if eguess == int(guess) - int(2) or eguess == int(guess) + int(2):
                            etd = int(eStr) + int(eDex) - int(1)
                            etd = str(etd)
                            TotHea = int(TotHea) - int(etd)
                            TotHea = str(TotHea)
                            print("Mediocre hit. Your enemy deals "+etd+" to you, leaving you with "+TotHea+" left.")
                        if eguess <= int(guess) - int(3) or eguess >= int(guess) + int(3):
                            etd = int(eStr) + int(eDex) - int(5)
                            etd = str(etd)
                            TotHea = int(TotHea) - int(etd)
                            TotHea = str(TotHea)
                            print("Weak hit. Your enemy deals "+etd+" to you, leaving you with "+TotHea+" left.")
                        TotHea = int(TotHea)
                    else:
                        if classn == "Summoner":
                            summon = random.randint(1,2)
                            if summon == 1:
                                aq = input("You have defeated our enemy. Would you like to add this creature to your army?").capitalize()
                                if "Yes" or "Y":
                                    print("You gain a new summon.")
                                    summonNumber = summonNumber + 1
                                if summonNumber >= maxSummon:
                                    TotHea = int(TotHea) - int(2)
                                    TotHea = str(TotHea)
                                    print("Attempting to gain a new minion, you discover that the toll is too much. You are left with "+TotHea+ "health.")
                                    if TotHea <= 0:
                                        print("You died.")
                                else:
                                    print("The enemy dies")
                            else:
                                print("The enemy dies")
                        else:
                            print("You have vanquished your enemy.")
                            lootdrop = random.randint(1,2)
                            if lootdrop == 1:
                                lootRarity = ad
                                print("You obtained a "+ad+" "+item+".")
                            else:
                                print("You obtained nothing")
                
                
            else:
                nTotHea = int(TotHea) - random.randint(1,TotHea)
                nTotHea = str(nTotHea)
                TotHea = str(TotHea)
                print("You aren't strong enough to wield your weapon effectively.")
                print("You lost. HP falls from "+TotHea+" to "+nTotHea)
                
fight("imp",7, 5, 1, 1)
fight("warlord",7, 5, 7, 9)
fight("dictator",7, 5, 3, 3)


