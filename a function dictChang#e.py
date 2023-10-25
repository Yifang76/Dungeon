from random import *
import sys
gold = 0
summonNumber = int(0)
totalSummonNumber = None
inventory = ["helmet", "sword"]
eTotHea = int(1)
carry = True
summons = []
shopStock = []
bankedGold = 0
bankedItems = []
n = None
hEqItem = None
cEqItem = None
lEqItem = None
gEqItem = None
bEqItem = None
rhEqItem = None
lhEqItem = None
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
def classv(LevelG, StrG, AgiG, DexG, HeaG, PerG, ChaG, IntG, TotHeaG):
    global Level
    global Str
    global Agi
    global Dex
    global Hea
    global Per
    global Cha
    global Int
    global TotHea
    print(f"Welcome, {classn} {name}.")
    Level = int(LevelG)
    Str = int(StrG)
    Agi = int(AgiG)
    Dex = int(DexG)
    Hea = int(HeaG)
    Per = int(PerG)
    Cha = int(ChaG)
    Int = int(IntG)
    TotHea = int(TotHeaG)

match classn:
    case "Knight":
        classv(15, 10, 3, 8, 7, 4, 6, 5, 70)
        inventory.append("King's Charter")
    case "Summoner":
        classv(5, 1, 4, 1, 2, 9, 2, 8, 20)
        totalSummonNumber = Int

    case "Merchant":
        classv(7, 1, 8, 1, 3, 8, 10, 6, 30)
        bankedGold = 1000
    case "Tom":
        if name == "Tom":
            classv()
    case "William":
        if name == "William":
            classv(120,3,3,3,5,3,0,10,50)
    case _:
        print("That is not an option")


weaponModifier = {

}

items = {
    #weapons
    "common axe": 10-Cha,
    "rare axe": 50-Cha,
    "mythical axe": 1000-Cha,
    "legendary axe": 500000-Cha,
    "common stick": 5-Cha,
    "rare stick": 25-Cha,
    "mythical stick": 50-Cha,
    "legendary stick": 100-Cha,
    "common sword": 20-Cha,
    "rare sword": 60-Cha,

    #resources
    "leather" : 15-Cha,

    #valuables
    "iron" : 40-Cha,
}

equipped_items = {
    "Head": None,
    "Chest": None,
    "Gloves": None,
    "Leggings": None,
    "Boots": None,
    "Right Hand": None,
    "Left Hand": None,
}

slot_mapping = {
    "H": "Head",
    "C": "Chest",
    "G": "Gloves",
    "L": "Leggings",
    "B": "Boots",
    "RH": "Right Hand",
    "LH": "Left Hand",
}

rarityValues = {
    "common": 5,
    "rare": 20,
    "mythical": 50,
    "legendary": 100,
}


places = {
    "Stormcrag" : 10,
    "Havoc's Rock" : 50,
    "Duskmire" : 25,
    "Ironhold" : 7,
    "Thornwood" : 5,
}

fenceDict = {
    "necronomicon" : 10,
    "demon heart" : 20,
    "dragon scale" : 50,
    "human flesh" : 5,
    "dragon tooth" : 50
}


pList = ["Stormcrag", "Havoc's Rock", "Duskmire", "Ironhold", "Thornwood"]

liteList = ["common axe",
"rare axe", "mythical axe", "legendary axe", 
"common stick", "rare stick", "mythical stick", 
"legendary stick", "common sword", "rare sword",
"leather", "iron" ]

invalidSell = ["King's Charter"]
illItems = ["necronomicon", "demon heart", "dragon scale", "human flesh"]
#cChangeItem are all items that perform a class change
cChangeItem = ["necronomicon", "demon heart", "dragon tooth"]
safe = ["Cetus","Ashborn"]

#NEED TO TEST
def classChange(newClass, itemUsing, lev, stre, agi, dex, hea, per, cha, inte, totHea, specialAbility, specialAbilityValue):
    global classn
    while True:
        q = input(f"Would you like to switch class? You will change from {classn} to {newClass}. You will be reset to level 1 and the {itemUsing} will be consumed.").capitalize()
        if q == "Yes" or q == "Y":
            inventory.remove(itemUsing)
            classn = newClass
            classv(lev,stre,agi,dex,hea,per,cha,inte,totHea)
            specialAbility = specialAbilityValue
            break
        elif q == "No" or q == "N":
            print(f"You reject the urge to use the {itemUsing} and remain as a {classn}.")
            break
        else:
            print("That is not an option.")
            
def rarities(q):
    global weaponModifier
    factors = [" int", " faith", " strength", " dexterity", " health"]
    factor = choice(factors)
    f = q.split()
    print(f)
    if q in inventory:
        if f[0] in rarityValues:
            tFactor = str(rarityValues[f[0]]) + factor
            print(f"{q} has effect +{tFactor}.")
            weaponModifier.update({q : tFactor})

        else:
            print("NO")
    else:
        print("NO2")

def guard(statement, tim):
    q = input(f"You are charged with {statement}. You will be sentenced for {tim}. "
    "What will you do? (Resist Arrest (F), Evade Arrest (E) Bribe Guard (B), "
    "Persuade Guard (P) Intimidate Guard (I) or Accept Arrest (A)) ").capitalize()
    answer = False
    while answer == False:
        match q:
            case "Resist Arrest" | "Resist" | "Fight" |"F":
                guardF()
            case "Evade Arrest" | "Evade" |"E":

            case "Accept Arrest" | "Accept" | "A":

            case "Bribe Guard" | "Bribe" | "B":

            case "Persuade Guard" | "Persuade" | "P":

            case "Intimidate Guard" | "Intimidate" | "I":

            case _:
                print("Hey, stop trying to evade justice!")

def guardF(place, safe, danger):
    global summonNumber
    global summons
    global TotHea
    global classn
    global totalSummonNumber
    global tim
    while TotHea > 0:
        if eTotHea > 0:
            opt = input(opon).capitalize()
            match opt:
                case "Fight" | "F":
                    eTotHea = eTotHea - (int(Str) * int(Dex))
                    print(f"The {noun} currently has {eTotHea} health left.")
                    TotHea = TotHea - (int(eStr) * int(eDex))
                    print(f"You currently have {TotHea} health left.")
                case "Use Item" | "Use" | "Item" | "I":
                    print("")
                case "Retreat" | "R":
                    retreat = randint(1+Agi,100)
                    if retreat >= 50:
                        print("You successfully fled, coward.")
                        break
                    else:
                        print("You failed to escape.")
                case _:
                    print("That is not an option")
        if eTotHea <= 0:       
            tim = tim + 5
            if randint(1,2) == 1:
                print("Another guard arrives to stop you")
                guardF(place, safe, danger)
            else:
                print(f"Escaping, the knowledge that you cannot enter {place} again without "
                "being pursued by the guards sets in.")
                chois()


    if TotHea <= 0:
        if place in safe:
            #change to 20 years eventually; make it compatible with months, ect.
            tim = tim + 20
            print(f"Wounded, you are dragged to prison by the guards, sentence increasing to {tim}.")
        else:
            print("You died")
            sys.exit()

def sell():
    global gold
    while True:
        print(f"You currently have {gold} gold.")
        print(inventory)
        sellWhich = input("What would you like to sell? ")
        if sellWhich in fenceDict:
            q = input(f"{sellWhich.capitalize()}! Get that thing away from me; it's illegal. "
            "Of course, only if you don't have the gold. How about you give me 10,000 gold and I'll "
            "tell you where you can sell it. ").capitalize()
            if q == "Yes" or q == "Y":
                if int(gold)-int(10000) >= 0:
                    gold = gold - 10000
                    print("Thanks for the gold. As promised, if you go to the 'Fence', and say "
                    " then you can buy and sell less 'savoury' wares.")
                else:
                    print("Seems like you can't pay up. Well then, guards!")
                    guard("intention to sell an illegal item", "20 years")
                    break
            else:
                print("I see, I see. Well then, guards!")
                guard("intention to sell an illegal item", "20 years")
                break
        else:
            if sellWhich in inventory:
                if sellWhich not in invalidSell:
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
                    print("You can't sell that!")
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
                print("That is not an option")
        else:
            print(f"The shop does not have {buyWhich} in stock")
            esc = input("Would you like to stop buying? ").capitalize()
            if esc == "Yes":
                break

    for i in range(randint(1,20)):
        shopStock.append(choice(liteList))
    print(f"You currently have {gold} gold.")
    print(f"You currently have {inventory}.")

def fence():
    IVLoop = True
    passw = input("What is the passcode? ")
    if passw == "":
        print("You may enter, sinner.")
        if classn == "Knight":
            Char = -5
            print("Surrounded by sinners, miscreants, spies and traitors, the King's Charter has no"
            f" effect here. On the contrary, it enrages the inhabitants. Charisma drops to {Char}")
        while IVLoop == True:
            BoS = input("Would you like to buy or sell, sinful one? ").capitalize()
            if BoS == "Buy" or BoS == "B":
                IVLoop = False
                fenBuy()
            if BoS == "Sell" or BoS == "S":
                if not inventory:
                    print("You have nothing of value, devious one.")
                else:
                    IVLoop = False
                    fenSell()
                    
    else:
        print("You are not one of us. Leave.")
        chois()

def fenBuy():
    global gold
    shopStock = []

    for i in range(randint(1,20)):
        shopStock.append(choice(illItems))
    print(f"You currently have {gold} gold.")
    print(f"You currently have {inventory}.")
    while True:
        print(f"The shop currently has {shopStock}")
        buyWhich = input("What would you like to buy? ")
        if buyWhich in shopStock:
            YN = input(f"Would you like to buy {buyWhich} for {str(fenceDict[buyWhich])} gold? ").capitalize()
            if YN == "Yes":
                phGold = int(gold) - fenceDict[buyWhich]
                if phGold > 0:
                    gold = phGold
                    shopStock.remove(buyWhich)
                    inventory.append(buyWhich)
                    print(f"You currently have {gold} gold.")
                    again = input("Would you like to use the shop again? ").capitalize()
                    if again == "No":
                        break
                else:
                    print(f"You do not have enough gold; you need {str(int(fenceDict[buyWhich]) - int(gold))} more gold.")
                    esc = input("Would you like to stop buying? ").capitalize()
                    if esc == "Yes":
                        break

            elif YN == "No":
                esc = input("Would you like to stop buying? ").capitalize()
                if esc == "Yes":
                    break
            else:
                print("That is not an option")
        else:
            print(f"The shop does not have {buyWhich} in stock")
            esc = input("Would you like to stop buying? ").capitalize()
            if esc == "Yes":
                break

    for i in range(randint(1,20)):
        shopStock.append(choice(liteList))
    print(f"You currently have {gold} gold.")
    print(f"You currently have {inventory}.")

def fenSell():
    global gold
    while True:
        print(f"You currently have {gold} gold.")
        print(inventory)
        sellWhich = input("What would you like to sell? ")
        if sellWhich in fenceDict:
            if sellWhich in inventory:
                if sellWhich not in invalidSell:
                    YN = input(f"Would you like to sell {sellWhich} for {str(fenceDict[sellWhich])} gold? ").capitalize()
                    if YN == "Yes":
                        inventory.remove(sellWhich)
                        gold = int(gold) + fenceDict[sellWhich]
                        again = input("Would you like to use the shop again? ").capitalize()
                        if again == "No":
                            break
                    elif YN == "No":
                        esc = input("Would you like to stop selling? ").capitalize()
                        if esc == "Yes":
                            break
                else:
                    print("You can't sell that!")
            else:
                print("You do not have this item")
                esc = input("Would you like to stop selling? ").capitalize()
                if esc == "Yes":
                    break
        else:
            if sellWhich in inventory:
                print("Sorry, we don't accept common goods here.")
                break
            else:
                print("You do not have this item.")
                break

    print(f"You currently have {gold} gold.")

def shop():
    IVLoop = True
    while IVLoop == True:
        BoS = input("Would you like to buy or sell? ").capitalize()
        if BoS == "Buy" or BoS == "B":
            IVLoop = False
            buy()
            
        if BoS == "Sell" or BoS == "S":
            if not inventory:
                print("You have nothing to sell.")
            else:
                IVLoop = False
                sell()


def bank():
    global bankedGold
    purpose = input("Are you withrawing (W) or depositing (D)? ").capitalize()
    match purpose:
        case "W" | "Withdrawing" | "Withdraw":
            wth()       
        case "D" | "Depositing" | "Deposit":
            depo()
        case _:
            print("That is not an option.")

def wth():
    global gold
    global bankedGold
    global bankedItems
    global inventory
    wthWhch = input("Would you like to withdraw Items (I) or Gold (G)? ").capitalize()
    match wthWhch:
        case "Items" | "Item" | "I":
            print(f"You currently have {inventory} and the bank currently contains {bankedItems}.")
            whichDraw = input("Which item would you like to withdraw? ")
            if whichDraw in bankedItems:
                inventory.append(whichDraw)
                bankedItems.remove(whichDraw)
                print(f"You currently have {inventory} and the bank currently contains {bankedItems}.")
            else:
                print("That is not an option.")    
        case "Gold" | "G":
            print(f"You currently have {bankedGold} gold banked and {gold} gold on your person.")
            amountDraw = int(input("How much would you like to withdraw? "))
            if bankedGold - amountDraw >= 0:
                bankedGold = bankedGold - amountDraw
                gold = gold + amountDraw
                print(f"You currently have {bankedGold} gold banked and {gold} gold on your person.")
            elif bankedGold - amountDraw < 0:
                print("You do not have enough gold in your bank.")
            else:
                print("That is not an option.")
        case _:
            print("That is not an option.")

def depo():
    global gold
    global bankedGold
    global bankedItems
    global inventory
    depWhch = input("Would you like to deposit Items (I) or Gold (G)? ").capitalize()
    match depWhch:
        case "Items" | "Item" | "I":
            print(f"You currently have {inventory} and the bank currently contains {bankedItems}.")
            whichDep = input("Which item would you like to deposit? ")
            if whichDep in inventory:
                inventory.remove(whichDep)
                bankedItems.append(whichDep)
                print(f"You currently have {inventory} and the bank currently contains {bankedItems}.")
            else:
                print("That is not an option.")    
        case "Gold" | "G":
            print(f"You currently have {bankedGold} gold banked and {gold} gold on your person.")
            amountDep = int(input("How much would you like to deposit? "))
            if gold - amountDep >= 0:
                bankedGold = bankedGold + amountDep
                gold = gold - amountDep
                print(f"You currently have {bankedGold} gold banked and {gold} gold on your person.")
            elif bankedGold - amountDep < 0:
                print("You do not have enough gold at hand.")
            else:
                print("That is not an option.")
        case _:
            print("That is not an option.")

def armory():
    WoR = input("Would you like to Equip (E) or Remove (R) equipment? ").capitalize()
    if WoR == "Equip" or WoR == "E":
        whereEq = input("Which slot would you like to equip: Head (H), Chest (C), Gloves (G), Leggings (L), Boots (B),"
                        " Right Hand (RH) or Left Hand (LH)? ").capitalize()
        if whereEq.upper() in slot_mapping:
            whereEq = slot_mapping[whereEq.upper()]
            equip(whereEq)
        else:
            print("That is not an option.")
    elif WoR == "Remove" or WoR == "R":
        remove()
    else:
        print("That is not an option.")
       
def equip(whereEq):
    if equipped_items[whereEq] is None:
        available_items = [item for item in inventory if item != equipped_items[whereEq]]
        if available_items:
            whichEq = input(f"Available items for {whereEq}: {available_items}\nWhat would you like to equip? ")
            if whichEq in available_items:
                equipped_items[whereEq] = whichEq
                inventory.remove(whichEq)
                print(f"You are now wearing {whichEq}.")
            else:
                print("Invalid item selection.")
        else:
            print(f"You don't have any available items to equip in {whereEq}.")
    else:
        print(f"You already have {equipped_items[whereEq]} in {whereEq}.")

def remove():
    whereRem = input("From which slot would you like to remove equipment? (Do NOT use abbreviations) ").capitalize()
    if whereRem in equipped_items:
        item = equipped_items[whereRem]
        if item is not None:
            inventory.append(item)
            equipped_items[whereRem] = None
            print(f"You have removed the {item} from {whereRem}.")
        else:
            print(f"There is no equipment in {whereRem} to remove.")
    else:
        print("Invalid slot selection.")


def lootIsDropped():
    lootdrop = randint(1,2)
    if lootdrop == 1:
        itemDrop = randint(1,3)
        if itemDrop == 1:
            loot = ad + weapon
        elif itemDrop == 2:
            loot = resource
        else:
            loot = valuable
        global inventory
        inventory.append(loot)
        print("You obtained a "+loot+".")
        rarities(loot)
        print(inventory)

    else:
        print("You obtained nothing")

def menu():
    cChangeDict = {
        "necronomicon" : "Necromancer",
        "demon heart" : "Demon",
        "dragon tooth" : "Dragonkin",
    }
    descDict = {
        "sword" : "A common sword, favoured by scavengers lucky enough to find one.",
    }
    q = input("What would you like to do. View Stats (S), View Inventory (I), Use Item (U) or Check Level (L). ").capitalize()
    match q:
        case "View Stats" | "S":
            print(f"Without modifiers, you have:\nHealth: {TotHea}\nStrength: {Str}\nDexterity: {Dex}\n"
            f"Perception: {Per}\nCharisma: {Cha}\nIntelligence: {Int} ")
            print(f"With modifiers, you have:\nHealth: {nTotHea}\nStrength: {nStr}\n Dexterity: {nDex}"
            f"Perception: {nPer}\nCharisma: {nCha}\nIntelligence: {nInt} ")
        case "View Inventory" | "I":
            print(f"You currently carry {inventory}.")
            checkDesc = input("Would you like to check an item description? ").capitalize()
            if checkDesc == "Yes" or checkDesc == "Y":
                whichDesc = input("Which item would you like check? ")
                if whichDesc in inventory:
                    print(f"{whichDesc.capitalize()} : {str(descDict[whichDesc])}")
                else:
                    print(f"You do not have {whichDesc}.")
            elif checkDesc == "No" or checkDesc == "N":
                print("You conclude your check.")
            else:
                print("That is not an option")

        case "Use Item" | "U":
            print(inventory)
            whichItem = input("Which item would you like to use? ")
            if whichItem in inventory:
                sure = input(f"Are you sure you want to use {whichItem}? ").capitalize()
                if sure == "Yes" or sure == "Y":
                    if whichItem in cChangeItem:
                        match whichItem:
                            case "necronomicon":
                            #check for adverwse affects using an integer instead of inte*2 for specialAbilityValue
                                classChange(str(cChangeDict[whichItem]),whichItem, 1, 2, 6, 2, 1, 10, 0, 15, 10, totalSummonNumber, 30)

                else:
                    print(f"You have decided to not use {whichItem}.")

            else:
                print("That is not an option")
               # chois() 
        case "Check Level" | "L":
            print(f"You are currently level {Level}.")



#Possibly Uneeded
def nounList(firstV, secondV, thirdV, fourthV, fifthV, sixthV, seventhV, eighthV, ninthV, tenthV):
    global n
    global modNlist
    nlist = [firstV, secondV, thirdV, fourthV, fifthV, sixthV, seventhV, eighthV, ninthV, tenthV]
    modNlist = [item for item in nlist if item is not None]
    print(modNlist)
    n = choice(modNlist)

#Works
def where():
    global whr
    whr = input(f"Where would you like to go? {pList} ").capitalize()
    if whr in pList:
        if int(places[whr]) > int(Level):
            con = input(f"Are you sure you want to go to {whr}? At your current level, it is quite dangerous.").capitalize()
            if con == "Yes" or con == "Y":
                car()
            elif con == "No" or con == "N":
                print("Returning to the city.")
                chois()
            else:
                print("That is not an option")
                chois()
                
        else:
            print(f"You are going to {whr}.")
            car()

#Works
def enemyInPlace():
    global whr
    match whr:
        case "Thornwood":
            nounList("bandit", "wolf", "insect", "ent", None, None, None, None, None, None)
        case "Stormcrag":
            nounList(None, None, None, None, None, None, None, None, None, None)
        case "Ironhold":
            nounList(None, None, None, None, None, None, None, None, None, None)
        case "Duskmire":
            nounList(None, None, None, None, None, None, None, None, None, None)
        case "Havoc's Rock":
            nounList(None, None, None, None, None, None, None, None, None, None)


def encounter(noun):
    global ad
    global itemlist
    global item
    global n
    global v
    global pv
    global ex
    global eTotHea
    global weapon
    global resource
    global valuable
    adlist = ["common ","rare ","mythical ","legendary "]
    ad = choice(adlist)

    weaponlist = ["axe","sword","stick"]
    weapon = choice(weaponlist)

    resourcelist = ["leather"]
    resource = choice(resourcelist)

    valuablelist = ["iron"]
    valuable = choice(valuablelist)

    vlist = ["stands","looks","glares"]
    v = choice(vlist)


    palist = ["saunter","walk","run"]
    pv = choice(palist)

    match n:
        case "warlord" | "dictator" | "bandit" | "wolf":
            det = str("a")
        case _:
            det = str("an")

    if v == "looks" or v == "glares":
        ex = str("at you")
    else:
        ex = str("there")
    global opon
    opon = str(f"As you {pv} down the path, {det} {noun} {v} {ex} menacingly. Would you like to Fight (F), Use Item (I) or Retreat (R)? ")


def fight(noun, eTotHea, eStr, eDex):
    global summonNumber
    global summons
    global TotHea
    global classn
    global totalSummonNumber
    while TotHea > 0:
        if eTotHea > 0:
            opt = input(opon).capitalize()
            match opt:
                case "Fight" | "F":
                    eTotHea = eTotHea - (int(Str) * int(Dex))
                    print(f"The {noun} currently has {eTotHea} health left.")
                    TotHea = TotHea - (int(eStr) * int(eDex))
                    print(f"You currently have {TotHea} health left.")
                case "Use Item" | "Use" | "Item" | "I":
                    print("")
                case "Retreat" | "R":
                    retreat = randint(1+Agi,100)
                    if retreat >= 50:
                        print("You successfully fled, coward.")
                        break
                    else:
                        print("You failed to escape.")
                case _:
                    print("That is not an option")
        if eTotHea <= 0:
            if classn == "Summoner" or classn == "Necromancer":
                lootIsDropped()
                print(f"You currently have {summons} under your control.\nYou can only convert {totalSummonNumber - summonNumber} more.")
                q = input(f"Would you like to summon {noun}? ").capitalize()
                if q == "Yes" or q == "Y":
                    summonS = randint(1,2)
                    if summonS == 1:
                        if totalSummonNumber > summonNumber:
                            summons.append(noun)
                            totalSummonNumber = totalSummonNumber - 1
                            print(f"Congratulations, you gained {noun}.")
                            break
                    else:
                        print("NO")
                        break
                elif q == "No" or q == "N":
                    print(f"You give up on converting the {noun}.")
                    break
                else:
                    print("That is not an option")
            else:
                print("ENEMY VANQUISHED")
                lootIsDropped()
                break


                

    if TotHea <= 0:
        print("You died.")
        sys.exit()

    
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
                        splinch = whichUp.split()
                        if splinch[0] not in rarityValues:
                            inventory.remove("iron")
                            inventory.remove(whichUp)
                            ad = choice(adlist)
                            inventory.append(ad + whichUp)
                            print(inventory)
                        else:
                            q = input(f"{whichUp} has modifier {splinch[0]}. Would you like to change this? ").capitalize()
                            if q == "Yes" or q == "Y":
                                inventory.remove("iron")
                                inventory.remove(whichUp)
                                ad = choice(adlist)
                                inventory.append(ad + splinch[1])
                                print(inventory)
                            else:
                                print("Cancelling process")

                    else:
                        print(f"You do not meet the requirements to upgrade {whichUp}.")
            else:
                print("You do not have this item.")    

    else:
        print("That is not an option.")




def chance():
    global modNlist
    chanceEn = randint(1,3)
    actions = {
    1: ("imp", 25, 1, 1),
    2: ("warlord", 100, 7, 9),
    3: ("dictator", 75, 3, 3),
    4: ("bandit", 10, 2, 2),
    5: ("wolf", 7, 4, 4),
    6: ("insect", 2, 1, 1),
    7: ("ent", 50, 7, 7),
    8: ("insect", 2, 1, 1),
    9: ("insect", 2, 1, 1),
    10: ("insect", 2, 1, 1),
    11: ("insect", 2, 1, 1),
    }
    if chanceEn == 1:
        no, health, attack, defense = actions[randint(1,11)]
        encounter(no)
        fight(no, health, attack, defense)
    elif chanceEn == 2:
        print("Placeholder")

def chois():
    global carry
    while True:
        townQuestion = input("Where would you like to go?"
                    " You may go to the Alchemist (P),"
                    " the Blacksmith (W), the Armory (A), the Bank (B)"
                    " the Market (M), the Menu or back Out (O). ").capitalize()
        match townQuestion:
            case "Market" | "M":
                print("Going to the Market")
                shop()
                chois()
            case "Blacksmith" | "W":
                print("Going to the Blacksmith")
                blacksmith()
                #NOTE: The function can be used within its definition, as shown below
                chois()
            case "Alchemist" | "P":
                print("Going to the Alchemist")
                chois()
            case "Armory" | "A":
                armory()
                chois()
            case "Bank" | "B":
                bank()
                chois()
            case "Menu":
                menu()
                chois()
            case "Fence" | "BM":
                fence()
                chois()
            case "Out" | "O":
                where()
            case _:
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
chois()
car()

#ctrl + k, ctrl + 0 = collapse all
#ctrl + k, ctrl + j = expand all
