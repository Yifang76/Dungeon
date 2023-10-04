from random import *
import sys
gold = 0
summonNumber = int(0)
inventory = []
eTotHea = int(1)
carry = True
summons = []
shopStock = []

adlist = ["common ","rare ","mythical ","legendary "]
ad = choice(adlist)
weaponlist = ["axe","sword","stick"]
weapon = choice(weaponlist)

resourcelist = ["leather"]
resource = choice(resourcelist)

valuablelist = ["iron"]
valuable = choice(valuablelist)


name = input("Name, please ").capitalize()
print("Knight: Honourable warriors of the Lennish empire, they are extremely strong and are representatives of the law. (Strength: 10, Agility: 3, Dexterity: 8, Health: 7, Perception: 4, Charisma: 6 (Within lawful lands) or 0 (in foreign lands), Intelligence: 5 )")
print("Merchant: (Strength: 1, Agility: 8, Dexterity: 1, Health: 3, Perception: 8, Charisma: 10, Intelligence: 6 )")
print("Summoner: (Strength: 1, Agility: 4, Dexterity: 1, Health: 2, Perception: 9, Charisma: 2, Intelligence: 8 )")
attriQuery = input("Would you like a guide on the attributes? ").capitalize()
if attriQuery == "Yes":
    print("Strength determines the base damage you do, Agility determines your evasion, Dexterity determines ______, Perception determines your critical chance, Charisma determines your barter rate and speech, Intelligence determines your spellcraft and Health determines your starting health.")

classn = input("Pick a class ").capitalize()
def classv(className, message, StrG, AgiG, DexG, HeaG, PerG, ChaG, IntG, TotHeaG, Sclass, SpeciaAbi, SpecialAbiNum):
    global classn
    global Str
    global Agi
    global Dex
    global Hea
    global Per
    global Cha
    global Int
    global TotHea
    global name
    if classn == className:
        print(message)
        Str = int(StrG)
        Agi = int(AgiG)
        Dex = int(DexG)
        Hea = int(HeaG)
        Per = int(PerG)
        Cha = int(ChaG)
        Int = int(IntG)
        TotHea = int(TotHeaG)
        if classn == Sclass:
            SpecialAbi = int(SpecialAbiNum)

classv("Knight", f"Welcome, knight {name}.", 10, 3, 8, 7, 4, 6, 5, 70, "0", "Pi", 0)
classv("Merchant", f"Welcome, merchant {name}.", 1, 8, 1, 3, 8, 10, 6, 30, "Merchant", "Banked Gold", 1000)
classv("Summoner", f"Welcome, summoner {name}.", 1, 4, 1, 2, 9, 2, 8, 20, "Summoner", summonNumber, 0)


items = {
#weapons
"common axe": 10,
"rare axe": 50,
"mythical axe": 1000,
"legendary axe": 500000,
"common stick": 1,
"rare stick": 2,
"mythical stick": 3,
"legendary stick": 5,
"common sword": 20,
"rare sword": 60,

#resources
"leather" : 2,

#valuables
"iron" : 20,
}

liteList = ["common axe",
"rare axe", "mythical axe", "legendary axe", 
"common stick", "rare stick", "mythical stick", 
"legendary stick", "common sword", "rare sword",
"leather", "iron" ]

def sell():
    global gold
    while True:
        print(f"You currently have {gold} gold.")
        print(inventory)
        sellWhich = input("What would you like to sell? ")
        if sellWhich in inventory:
            YN = input(f"Would you like to sell {sellWhich} for {str(items[sellWhich])} gold? ").capitalize()
            if YN == "Yes":
                inventory.remove(sellWhich)
                gold = int(gold) + items[sellWhich]
                again = input("Would you like to use the shop again? ").capitalize()
                if again == "No":
                    break
            elif YN == "No":
                esc = input("Would you like to stop selling? ").capitalize()
                if esc == "Yes":
                    break
        else:
            print("You do not have this item")
            esc = input("Would you like to stop selling? ").capitalize()
            if esc == "Yes":
                break

    print(f"You currently have {gold} gold.")

def buy():
    global gold
    shopStock = []

    for i in range(randint(1,20)):
        shopStock.append(choice(liteList))
    print(f"You currently have {gold} gold.")
    print(f"You currently have {inventory}.")
    while True:
        print(f"The shop currently has {shopStock}")
        buyWhich = input("What would you like to buy? ")
        if buyWhich in shopStock:
            YN = input(f"Would you like to buy {buyWhich} for {str(items[buyWhich])} gold? ").capitalize()
            if YN == "Yes":
                phGold = int(gold) - items[buyWhich]
                if phGold > 0:
                    gold = phGold
                    shopStock.remove(buyWhich)
                    inventory.append(buyWhich)
                    print(f"You currently have {gold} gold.")
                    again = input("Would you like to use the shop again? ").capitalize()
                    if again == "No":
                        break
                else:
                    print(f"You do not have enough gold; you need {str(int(items[buyWhich]) - int(gold))} more gold.")
                    esc = input("Would you like to stop buying? ").capitalize()
                    if esc == "Yes":
                        break

            elif YN == "No":
                esc = input("Would you like to stop buying? ").capitalize()
                if esc == "Yes":
                    break
        else:
            print(f"The shop does not have {buyWhich} in stock")
            esc = input("Would you like to stop buying? ").capitalize()
            if esc == "Yes":
                break

    for i in range(randint(1,20)):
        shopStock.append(choice(liteList))
    print(f"You currently have {gold} gold.")
    print(f"You currently have {inventory}.")

def shop():
    IVLoop = True
    while IVLoop == True:
        BoS = input("Would you like to buy or sell? ").capitalize()
        if BoS == "Buy":
            IVLoop = False
            buy()
            
        if BoS == "Sell":
            if not inventory:
                print("You have nothing to sell.")
            else:
                IVLoop = False
                sell()

def encounter():
    global adlist
    global ad
    global itemlist
    global item
    global nlist
    global n
    global vlist
    global v
    global palist
    global pv
    global ex
    global eTotHea
    global weapon
    global weaponlist
    global resource
    global resourcelist
    global valuable
    global valuablelist
    adlist = ["common ","rare ","mythical ","legendary "]
    ad = choice(adlist)

    weaponlist = ["axe","sword","stick"]
    weapon = choice(weaponlist)

    resourcelist = ["leather"]
    resource = choice(resourcelist)

    valuablelist = ["iron"]
    valuable = choice(valuablelist)

    nlist = ["imp","warlord","dictator"]
    n = choice(nlist)

    vlist = ["stands","looks","glares"]
    v = choice(vlist)


    palist = ["saunter","walk","run"]
    pv = choice(palist)

    if n == "warlord" or n == "dictator":
        det = str("a")
    else:
        det = str("an")

    if v == "looks" or v == "glares":
        ex = str("at you")
    else:
        ex = str("there")

    if n == "imp":
        eTotHea = int(25)
    if n == "warlord":
        eTotHea = int(100)
    if n == "dictator":
        eTotHea = int(75)
    global opon
    opon = str(f"As you {pv} down the path, {det} {n} {v} {ex} menacingly. What will you do? (Fight (F) or Run (R))? ")

def fight(noun, StrReq, DexReq, eStr, eDex):
    global TotHea
    global opon
    global carry
    commence = True
    while commence == True:
        opo = input(opon).capitalize()
        if opo == "Fight" or opo == "F":
            commence = False
            if n == noun:
                if Str >= StrReq and Dex >= DexReq:
                    TotHea == str(TotHea)
                    #print("You have "+TotHea+".")
                    #print("Minigame starting")
                    print("Rules: you are given a number between 1 and 10. If you get within 1 digit of the original number, you deal a fatal wound (which does the highest damage). Three digits difference leads to a body hit (which does mediocre damage) and finally anything over a three number difference will be a miss")
                    while TotHea > 0:
                        global eTotHea
                        print(eTotHea)
                        eTotHea = int(eTotHea)
                        if eTotHea > 0:
                            if TotHea > 0:
                                guess = randint(1,10)
                                print(guess)
                                pguess = int(input("What do you believe the number is? "))
                                if pguess == int(guess) or pguess == int(guess) - int(1) or pguess == int(guess) + int(1):
                                    td = int(Str) + int(Dex) + int(2)
                                    eTotHea = int(eTotHea) - int(td)
                                    td = str(td)
                                    eTotHea = str(eTotHea)
                                    print("Critical hit! You deal "+td+" against your enemy, leaving them with "+eTotHea+" health left.")
                                elif pguess == int(guess) - int(2) or pguess == int(guess) + int(2):
                                    td = int(Str) + int(Dex) - int(1)
                                    eTotHea = int(eTotHea) - int(td)
                                    td = str(td)
                                    eTotHea = str(eTotHea)
                                    print("Mediocre hit. You deal "+td+" against your enemy, leaving them with "+eTotHea+" health left.")
                                elif pguess <= int(guess) - int(3) or pguess >= int(guess) + int(3):
                                    td = int(Str) + int(Dex) - int(5) 
                                    eTotHea = int(eTotHea) - int(td)
                                    td = str(td)
                                    eTotHea = str(eTotHea)
                                    print("Weak hit. You deal "+td+" against your enemy, leaving them with "+eTotHea+" health left.")
                                        
                                eguess = randint(1,10)
                                if eguess == int(guess) or eguess == int(guess) - int(1) or eguess == int(guess) + int(1):
                                    etd = int(eStr) + int(eDex) + int(2)
                                    TotHea = int(TotHea) - int(etd)
                                    TotHea = str(TotHea)
                                    etd = str(etd)
                                    print("Critical hit! Your enemy deals "+etd+" to you, leaving you with "+TotHea+" left.")
                                elif eguess == int(guess) - int(2) or eguess == int(guess) + int(2):
                                    etd = int(eStr) + int(eDex) - int(1)
                                    TotHea = int(TotHea) - int(etd)
                                    TotHea = str(TotHea)
                                    etd = str(etd)
                                    print("Mediocre hit. Your enemy deals "+etd+" to you, leaving you with "+TotHea+" left.")
                                elif eguess <= int(guess) - int(3) or eguess >= int(guess) + int(3):
                                    etd = int(eStr) + int(eDex) - int(5)
                                    TotHea = int(TotHea) - int(etd)
                                    TotHea = str(TotHea)
                                    etd = str(etd)
                                    print("Weak hit. Your enemy deals "+etd+" to you, leaving you with "+TotHea+" left.")
                                TotHea = int(TotHea)
                                eTotHea = str(eTotHea)
                        else:
                            if classn == "Summoner":
                                summon = randint(1,2)
                                if summon == 1:
                                    aq = input("You have defeated your enemy. Would you like to add this creature to your army?").capitalize()
                                    if "Yes" or "Y":
                                        print("You gain a new summon.")
                                        summonNumber = summonNumber + 1
                                        summons = summons.append(n)
                                    elif summonNumber >= maxSummon:
                                        TotHea = int(TotHea) - int(2)
                                        TotHea = str(TotHea)
                                        print("Attempting to gain a new minion, you discover that the toll is too much. You are left with "+TotHea+ "health.")
                                        if TotHea <= 0:
                                            print("You died.")
                                            carry = False
                                            return()
                                    else:
                                        print("The enemy dies")
                                else:
                                    print("The enemy dies")
                            else:
                                print("You have vanquished your enemy.")
                                lootdrop = randint(1,2)
                                if lootdrop == 1:
                                    itemDrop = randint(1,3)
                                    if itemDrop == 1:
                                        loot = ad + weapon
                                    elif itemDrop == 2:
                                        loot = resource
                                    else:
                                        loot = valuable
                                    print("You obtained a "+loot+".")
                                    global inventory
                                    inventory.append(loot)
                                    print(inventory)
                                else:
                                    print("You obtained nothing")
                                
                    print("You died.")
                    sys.exit()
                    
                    
                else:
                    nTotHea = int(TotHea) - randint(1,TotHea)
                    nTotHea = str(nTotHea)
                    TotHea = str(TotHea)
                    print("You aren't strong enough to wield your weapon effectively.")
                    print("You lost. HP falls from "+TotHea+" to "+nTotHea)
        elif opo == "Run" or opo == "R":
            retreat = randint(1+Agi,100)
            if retreat >= 50:
                print("You successfully fled, coward.")
                break
            else:
                print("You failed to escape.")
        else:
            print("That is not an option")
    #commence = True

def blacksmith():
    global inventory
    global ad
    global adlist
    CraftorUpgrade = input("Would you like to craft or upgrade? ").capitalize()
    if CraftorUpgrade == "Craft":
        craft = input("What would you like to craft: charm or weapon? ").capitalize()
        if craft == "Charm":
            if "gem" in inventory:
                if "leather" in inventory:
                    inventory.remove("gem")
                    inventory.remove("leather")
                    newCharm = ad + "charm"
                    inventory.append(newCharm)
                    print("s")
        elif craft == "Weapon":
            if "leather" in inventory:
                if "iron" in inventory:
                    inventory.remove("leather")
                    inventory.remove("iron")
                    inventory.append("weapon")


    elif CraftorUpgrade == "Upgrade":
        if not inventory:
            print("You have nothing to upgrade.")
        else:
            print(inventory)
            whichUp = input("What would you like to upgrade? ")
            if whichUp in inventory:
                correct = input(f"Do you want to upgrade {whichUp}? ").capitalize()
                if correct == "Yes" or correct == "Y":
                    if "iron" in inventory:
                        inventory.remove("iron")
                        inventory.remove(whichUp)
                        ad = choice(adlist)
                        inventory.append(ad + whichUp)
                        print(inventory)
                    else:
                        print(f"You do not meet the requirements to upgrade {whichUp}.")
            else:
                print("You do not have this item.")    

    else:
        print("That is not an option.")

def chance():
    global n
    chanceEn = randint(1,3)
    if chanceEn == 1:
        encounter()
        if n == "imp":
            fight("imp",7, 5, 1, 1)
        elif n == "warlord":
            fight("warlord",7, 5, 7, 9)
        elif n == "dictator":
            fight("dictator",7, 5, 3, 3)
    elif chanceEn == 2:
        print("Placeholder")

def chois():
    global carry
    while True:
        townQuestion = input("Where would you like to go? You may go to the Alchemist (P), the Blacksmith (B), the Market (M) or back Out (O). ").capitalize()
        if townQuestion == "Market" or townQuestion == "M":
            print("Going to the Market")
            shop()
            chois()
        elif townQuestion == "Blacksmith" or townQuestion == "B":
            print("Going to the Blacksmith")
            blacksmith()
            #NOTE: The function can be used within its definition, as shown below
            chois()
        elif townQuestion == "Alchemist" or townQuestion == "P":
            print("Going to the Alchemist")
            chois()
        elif townQuestion == "Armory" or townQuestion == "A":
            #armory()
        elif townQuestion == "Out" or townQuestion == "O":
            car()
        else:
            print("That is not an option.") 

def car():
    global carry
    while carry == True:
        chance()
        carryOn = input("Would you like to carry on? ").capitalize()
        if carryOn == "No" or carryOn == "N":
            print("You are returning to the city of Celkis.")
            chois()
        elif carryOn == "Yes" or carryOn == "Y":
            print("You are resuming with your journey. ")
            
        else:
            print("That is not an option.")

car()

#problem with fleeing; whether success or fail it repeats fight or flight response.
#after exiting shop immediately thrown out into the Outer Lands.