from random import *
import sys
gold = 0
summonNumber = int(0)
inventory = ["helmet", "sword"]
eTotHea = int(1)
carry = True
summons = []
shopStock = []
bankedGold = 0
bankedItems = []
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
    case "Summoner":
        classv(5, 1, 4, 1, 2, 9, 2, 8, 20)
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
    "common": "5",
    "rare": "20",
    "mythical": "50",
    "legendary": "100",
}


places = {
    "Stormcrag" : 10,
    "Havoc's Rock" : 50,
    "Duskmire" : 25,
    "Ironhold" : 7,
    "Thornwood" : 5,
}


pList = ["Stormcrag", "Havoc's Rock", "Duskmire", "Ironhold", "Thornwood"]

liteList = ["common axe",
"rare axe", "mythical axe", "legendary axe", 
"common stick", "rare stick", "mythical stick", 
"legendary stick", "common sword", "rare sword",
"leather", "iron" ]


def rarities(q):
    factors = [" int", " faith", " strength", " dexterity", " health"]
    factor = choice(factors)
    f = q.split()
    print(f)
    if q in inventory:
        if f[0] in rarityValues:
            tFactor = str(rarityValues[f[0]]) + factor
            print(f"{q} has effect +{tFactor}.")
        else:
            print("NO")
    else:
        print("NO2")

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
    global opon
    opon = str(f"As you {pv} down the path, {det} {n} {v} {ex} menacingly. Would you like to Fight (F), Use Item (I) or Retreat (R)? ")

def fight(noun, eTotHea, eStr, eDex):
    global TotHea
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
            if classn != "Summoner" or classn != "Necromancer":
                print("ENEMY VANQUISHED")
                lootIsDropped()
                break
            else:
                print("")

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

def where():
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


def chance():
    global n
    chanceEn = randint(1,3)
    if chanceEn == 1:
        encounter()
        if n == "imp":
            fight("imp", 25, 1, 1)
        elif n == "warlord":
            fight("warlord", 100, 7, 9)
        elif n == "dictator":
            fight("dictator", 75, 3, 3)
    elif chanceEn == 2:
        print("Placeholder")

def chois():
    global carry
    while True:
        townQuestion = input("Where would you like to go?"
                    " You may go to the Alchemist (P),"
                    " the Blacksmith (W), the Armory (A), the Bank (B)"
                    " the Market (M), or back Out (O). ").capitalize()
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