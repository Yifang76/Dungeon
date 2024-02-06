from random import *
import sys
gold, bankedGold, statUpgrade, experience, summonNumber, totalSummonNumber, renown = 0, 0, 0, 0, 0, 0, 0
activeBounties, gameFinish = [[],[],[],[],[]], False
bestiar, achievements, inventory = ["None"], ["None"], ["helmet", "sword", "Potter's Heart"]
faith, eTotHea, carry, summons, spells, shopStock, bankedItems = "None", int(1), True, ["None"], ["None"], [""], ["None", "Potter's Heart"]
hEqItem, cEqItem, lEqItem, gEqItem, bEqItem, rhEqItem, lhEqItem = "None", "None", "None", "None", "None", "None", "None" #Changed from None to "None" for saveFile
adlist = ["common ","rare ","mythical ","legendary "]
weaponlist = ["axe","sword","stick"]
resourcelist = ["leather"]
valuablelist = ["iron"]
ad, weapon, resource, valuable = choice(adlist), choice(weaponlist), choice(resourcelist), choice(valuablelist)
baseSpellsDict = {
    "Elemental" : "Fireball",
    "Chaos" : "Confusion",
    "Occult" : "Curse",
    "Divine" : "Bless",
    "Nature" : "Bind",
    "Aether" : "Barrage",
}
complete = False
name = input("Name, please ").title()
try:
    name.split().remove("Yifang")
    con = 1
except:
    con = 2
finally:
    if con == 1:
        print("Fuck you")
print("Knight: (Strength: 10, Agility: 3, Dexterity: 8,\nHealth: 7, Perception: 4, Charisma: 6 (Within lawful lands) or 0 (in foreign lands),\nIntelligence: 5)\n")
print("Merchant: (Strength: 1, Agility: 8, Dexterity: 1,\nHealth: 3, Perception: 8, Charisma: 10,\nIntelligence: 6)\n")
print("Summoner: (Strength: 1, Agility: 4, Dexterity: 1,\nHealth: 2, Perception: 9, Charisma: 2,\nIntelligence: 8)\n")
print("Mage: (Strength: 2, Agility: 4, Dexterity: 4,\nHealth: 5, Perception: 7, Charisma: 3,\nIntelligence: 10)\n")
attriQuery = input("Would you like a guide on the attributes? ").capitalize()
if attriQuery == "Yes":
    print("Strength determines the base damage you do, Agility determines your evasion, Dexterity determines base damage,\nPerception determines your critical chance, Charisma determines your barter rate and speech, Intelligence determines your spellcraft\nand Health determines your HP.\n")
def classv(LevelG, StrG, AgiG, DexG, HeaG, PerG, ChaG, IntG, TotHeaG):
    global Level, Str, Agi, Dex, Hea, Per, Cha, Int, TotHea, trueStr, trueAgi, trueDex, trueHea, truePer, trueCha, trueInt, trueTotHea
    print(f"Welcome, {classn} {name}.\n")
    Level = int(LevelG)
    trueStr, Str = int(StrG), int(StrG)
    trueAgi, Agi = int(AgiG), int(AgiG)
    trueDex, Dex = int(DexG), int(DexG)
    trueHea, Hea = int(HeaG), int(HeaG)
    truePer, Per = int(PerG), int(PerG)
    trueCha, Cha = int(ChaG), int(ChaG)
    trueInt, Int = int(IntG), int(IntG)
    trueTotHea, TotHea = int(TotHeaG), int(TotHeaG)

while True:
    classn = input("Pick a class ").capitalize()
    match classn:
        case "Knight":
            classv(43, 10, 3, 8, 7, 4, 6, 5, 70)
            inventory.append("King's Charter")
            renown = 50
            break
        case "Summoner":
            classv(26, 1, 4, 1, 2, 9, 2, 8, 20)
            totalSummonNumber = Int
            while True:
                print("Wotter")
                whichSummo = input("Which summon would you like to start with? ").capitalize()
                if whichSummo == "Wotter":
                    summons.append("wotter")
                    break
                else:
                    print("That is not an option")
            break
        case "Merchant":
            classv(37, 1, 8, 1, 3, 8, 10, 6, 30)
            bankedGold = 1000
            break
        case "Mage":
            classv(33, 2, 4, 4, 5, 7, 3, 10, 50)
            print("Elemental, Chaos, Occult, Divine, Nature, Aether")
            while True:
                whichCat = input("What sorcery will you dabble in? ").capitalize()
                if whichCat in baseSpellsDict:
                    spells.append(baseSpellsDict[whichCat])
                    print(f"Spell List: {spells}")
                    break
                else:
                    print("That is not an option")
            break
            LevelG, StrG, AgiG, DexG, HeaG, PerG, ChaG, IntG, TotHeaG
        case "Tom":
            if name == "Tom":
                classv(100, 5, 7, 4, 8, 3, 0, 4, 80)
                break
        case "Bradley":
            if name == "Bradley":
                classv(90, 1, 1, 1, 4, 1000000000, 0, 53, 40)
        case "William":
            if name == "William":
                classv(120,3,3,3,5,3,0,10,50)
                break
        case _:
            print("That is not an option")
#Meant To be Empty to store Values
weaponModifier = {

}

equipmentMapping = {
    "helmet" : "Head",
    "sword" : "Right Hand",
    "training sword": "Right Hand",
    "": 50,
    "half life": "N/A",
    "terra blade": "Right Hand",
    "stick": "Right Hand",
    "axe": "Right Hand",
    "scimitar": "Right Hand",
    "war axe": "Right Hand",
    "hatchets": "Right Hand",
    "King's Charter": "Accessory",
    "tommy gun": "Right Hand",
    "iron" : "N/A",
    "leather" : "N/A"
}


items = {
    #weapons
    "training sword": 10,
    "": 50,
    "half life": 1000,
    "terra blade": 500000,
    "stick": 5,
    "axe": 25,
    "scimitar": 50,
    "war axe": 100,
    "sword": 20,
    "hatchets": 60,

    #resources
    "leather" : 15-Cha,

    #valuables
    "iron" : 40-Cha,
}

equipped_items = {
    "Head": "None",
    "Chest": "None",
    "Gloves": "None",
    "Leggings": "None",
    "Boots": "None",
    "Right Hand": "None",
    "Left Hand": "None",
}
equipped_itemsList = ["Head", "None", "Chest", "None", "Gloves", "None", "Leggings", "None", "Boots", "None", "Right Hand", "None", "Left Hand", "None"]

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
    "womp potter, womp, the wompotous potter" : 4360,
    "Tomtress" : 4361,
    "Whitley World" : 4362,
    "Domain of the Death Star" : 10000
}

fenceDict = {
    "necronomicon" : 10,
    "demon heart" : 20,
    "dragon scale" : 50,
    "human flesh" : 5,
    "dragon tooth" : 50
}
livingBosses = ["None", "Tom", "Bradley", "William", "Windbreaker"]
#totalSummonNumber, 
listsConfig = [activeBounties, bestiar, spells, summons, bankedItems, livingBosses, achievements]
pList = ["womp potter, womp, the wompotous potter", "Tomtress", "Whitley World"]
liteList = ["leather", "iron" ]
enemyList = ["botter", "wotter"]
originClass = ["None"]
ascensionItems = [""]
invalidSell = ["King's Charter", "Taco", "Diabetes Type 3", "tommy gun"]
illItems = ["necronomicon", "demon heart", "dragon scale", "human flesh"]
#cChangeItem are all items that perform a class change
cChangeItem = ["necronomicon", "demon heart", "dragon tooth"]
safe = ["Cetus","Ashborn"]
bosses = ["Tom", "Bradley", "William"]
legalSpells = ["Elemental", "E", "Divine", "D", "Nature", "N", "Aether", "A"]
illegalSpells = ["Chaos", "C", "Occult", "O"]
elementalList = ["Fireball", "Freeze"]
chaosList = ["Confusion",]
occultList = ["Curse",]
divineList = ["Bless",]
natureList = ["Bind",]
aetherList = ["Barrage",]
spellDict = {
    "Elemental" : elementalList,
    "E" : elementalList,
    "Chaos" : chaosList,
    "C" : chaosList,
    "Occult" : occultList,
    "O" : occultList,
    "Divine" : divineList,
    "D" : divineList,
    "Nature" : natureList,
    "N" : natureList,
    "Aether" : aetherList,
    "A" : aetherList,
 }


summonStats = {
    "timp": (25, 1, 1, 2, 10,),
    "tapybara": (100, 7, 9, 5, 1,),
    "terodactyl": (125, 7, 7, 4, 10),
    "turtom": (1000, 1, 1, 1, 0),
    "wom": (7, 4, 4, 10, 3,),
    "tomsect": (2, 1, 1, 1, 1,),
    "tont": (50, 7, 7, 3, 1),
    "tomilla": (60, 6, 2, 1, 6),
    "hippotomamus": (150, 10, 2, 3, 4),
    "tombra": (30, 2, 3, 2, 5),
    "tomala": (50, 5, 5, 3, 1),
    "itley": (2, 1, 1, 1, 1),
    "bitley": (100, 1, 1, 7, 9),
    "witley": (25, 2, 2, 4, 5),
    "hitley": (10, 2, 2, 10, 10),
    "ditley": (7, 4, 4, 10, 3),
    "citley": (50, 7, 7, 3, 1),
    "kitley": (20, 1, 1, 1, 8),
    "litley": (40, 6, 5, 7, 7),
    "pterodactyley": (200, 8, 8, 5, 15),
    "ritley": (2, 1, 1, 1, 1),
    "wotter": (25, 3, 3, 2, 6),
    "botter": (75, 9, 9, 1, 9),
    "otter-otter": (40, 2, 2, 6, 7),
    "capy-otter": (10, 2, 2, 4, 4),
    "totter": (10, 2, 2, 5, 6),
    "kotter": (20, 4, 4, 1, 0),
    "gotter": (25, 1, 4, 3, 4),
    "cotter": (2, 1, 1, 1, 1),
    "hapotter": (2, 1, 1, 4, 5),
    "None": (0,0,0,0,0)
}
nTotHea = TotHea
#NEED TO TEST
def classChange(newClass, itemUsing, lev, stre, agi, dex, hea, per, cha, inte, TotHea, specialAbility, specialAbilityValue):
    global classn
    while True:
        q = input(f"Would you like to switch class? You will change from {classn} to {newClass}. You will be reset to level 1 and the {itemUsing} will be consumed. ").capitalize()
        if q == "Yes" or q == "Y":
            inventory.remove(itemUsing)
            if classn not in originClass:
                originClass.append(classn)
            classn = newClass
            if newClass not in originClass:
                originClass.append(classn)
            classv(lev,stre,agi,dex,hea,per,cha,inte,totHea)
            specialAbility = specialAbilityValue
            break
        elif q == "No" or q == "N":
            print(f"You reject the urge to use the {itemUsing} and remain as a {classn}.")
            break
        else:
            print("That is not an option.")
            
def sell():
    global gold
    while True:
        print(f"You currently have {gold} gold.")
        print(inventory)
        sellWhich = input("What would you like to sell? ")
        if sellWhich in inventory:
            if sellWhich not in invalidSell:
                if sellWhich not in ascensionItems:
                    YN = input(f"Would you like to sell {sellWhich} for {str(items[sellWhich]+Cha)} gold? ").capitalize()
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
                    print("Sorry; that's useless.")
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
            YN = input(f"Would you like to buy {buyWhich} for {str(items[buyWhich]-Cha)} gold? ").capitalize()
            if YN == "Yes":
                phGold = int(gold) - (items[buyWhich]-Cha)
                if phGold > 0:
                    gold = phGold
                    shopStock.remove(buyWhich)
                    inventory.append(buyWhich)
                    print(f"You currently have {gold} gold.")
                    again = input("Would you like to use the shop again? ").capitalize()
                    if again == "No":
                        break
                else:
                    print(f"You do not have enough gold; you need {str(int(items[buyWhich]-Cha) - int(gold))} more gold.")
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
    global gold, bankedGold, bankedItems, inventory
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
    global gold, bankedGold, bankedItems, inventory
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

def statBoosts(equipment):
    global Str, Agi, Dex, Hea, Per, Int
    eList = equipment.split(" ")
    try:
        upLevel = int(eList[len(eList)-1].replace("+",""))
        eList.pop(len(eList)-1)
        " ".join(eList)
    except:
        upLevel = 0.5
    finally:
        equipmentBuff = {
            "helmet" : [2*upLevel, "Health"],
            "sword" : [1*upLevel, "Strength"],
            "training sword": [0*upLevel, "Strength"],
            "": ["N/A"],
            "half life": ["N/A"],
            "terra blade": [20*upLevel, "Strength"],
            "stick": ["0", "N/A", -1*upLevel, "Strength"],
            "axe": [1*upLevel, "Strength"],
            "scimitar": [2*upLevel, "Dexterity"],
            "war axe": [5*upLevel, "Strength"],
            "hatchets": [2*upLevel, "Strength"],
            "King's Charter": ["N/A"],
            "tommy gun": [1000*upLevel, "Strength"],
            "None" : [0, "Strength"]
        }
        count, count1 = 1, 0
        for i in range(int(len(equipmentBuff[" ".join(eList)])/2)):
            match equipmentBuff[" ".join(eList)][count]:
                case "Strength":
                    Str += equipmentBuff[" ".join(eList)][count1]
                case "Agility":
                    Agi += equipmentBuff[" ".join(eList)][count1]
                case "Dexterity":
                    Dex += equipmentBuff[" ".join(eList)][count1]
                case "Health":
                    Hea += equipmentBuff[" ".join(eList)][count1]
                case "Perception":
                    Per += equipmentBuff[" ".join(eList)][count1]
                case "Intelligence":
                    Int += equipmentBuff[" ".join(eList)][count1]
                case "N/A":
                    print("")
            count += 2
            count1 += 2


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
    if equipped_items[whereEq] == "None":
        available_items = [item for item in inventory if item != equipped_items[whereEq]]
        if available_items:
            whichEq = input(f"Available items for {whereEq}: {available_items}\nWhat would you like to equip? ")
            if whichEq in available_items and equipmentMapping["".join([i for i in whichEq if not i.isdigit()]).replace("+","").strip()] == whereEq:
                equipped_items[whereEq] = whichEq
                count = 0
                for x in equipped_itemsList:
                    if x != whereEq:
                        count += 1
                    else:
                        equipped_itemsList[count+1] = whichEq
                inventory.remove(whichEq)
                print(f"You are now wearing {whichEq}.")
                statBoosts(whichEq)
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
            count = 0
            for x in equipped_itemsList:
                if x != whereRem:
                    count += 1
                else:
                    equipped_itemsList[count+1] = None
                    print(equipped_itemsList)
            equipped_items[whereRem] = "None"
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
            loot = weapon
        elif itemDrop == 2:
            loot = resource
        else:
            loot = valuable
        global inventory
        inventory.append(loot)
        print("You obtained a "+loot+".")
        print(inventory)

    else:
        print("You obtained nothing")

def menu():
    cChangeDict = {
    }

    spellDescDict = {
        "fireball" : "Basic sorcery for Elemental mages.\nFire was once deemed as taboo before its uses were brought to light.\nDeals 5 base fire damage multiplied by upgrade level.",
        "curse" : "Basic sorcery for Occult mages.\n Once upon a time, occult magic was accepted in society, acting as a parallel to faith; after the First Tragedy, it's hideous visage was truly revealed to the world",
        "barrage": "Basic sorcery for Aether mages.\n First came into existence after Will-Meister got his ass beat by Bradely.",
        "freeze": "Basic sorcery for Ice mages.\n First incepted by a freezing Tommy.",
        "None" : "Nothing"
    }
    weaponDescDict = {
        "sword" : "A common sword",
        "axe" : "A common axe",
        "stick" : "Useless",
        "Potter's Heart" : "Could have a use",
        "None" : "Nothing"
        #Need to edit to account for '

    }
    q = input("What would you like to do. View Stats (S), View Inventory (I), View Journal (J),"
    " View Spells (T), Use Item (U), Save/Load (C) or Check Level (L). ").capitalize()
    match q:
        case "View Stats" | "Stats" | "S":
            print(f"Without modifiers, you have:\nHealth: {trueTotHea}\nStrength: {trueStr}\nDexterity: {trueDex}\n"
            f"Perception: {truePer}\nCharisma: {trueCha}\nIntelligence: {trueInt} ")
        #    print(f"With modifiers, you have:\nHealth: {nTotHea}\nStrength: {nStr}\n Dexterity: {nDex}"
        #    f"Perception: {nPer}\nCharisma: {nCha}\nIntelligence: {nInt} ")
        case "View Inventory" | "Inventory" | "I":
            print(f"You currently carry {inventory}.")
            checkDesc = input("Would you like to check an item description? ").capitalize()
            if checkDesc == "Yes" or checkDesc == "Y":
                whichDesc = input("Which item would you like check? ")
                if whichDesc in inventory:
                    try:
                        print(f"{whichDesc.capitalize()}: {str(weaponDescDict[whichDesc])}")
                    except:
                        print("Invalid Item")
                else:
                    print(f"You do not have {whichDesc}.")
            elif checkDesc == "No" or checkDesc == "N":
                print("You conclude your check.")
            else:
                print("That is not an option")
        case "View Spells" | "Spells" | "T":
            print(spells)
            whichSpellDesc = input("Which spell would you like to view? ").replace("'","").lower()
            if whichSpellDesc in [x.lower().replace("'", "") for x in spells]:
                print(f"{whichSpellDesc.capitalize()}: {spellDescDict[whichSpellDesc]}")
            else:
                print("You do not have that spell")
        case "View Journal" | "Journal" | "J":
            journal()
        case "Use Item" | "U":
            print(inventory)
            whichItem = input("Which item would you like to use? ")
            if whichItem in inventory:
                sure = input(f"Are you sure you want to use {whichItem}? ").capitalize()
                if sure == "Yes" or sure == "Y":
                    if whichItem in cChangeItem:
                        match whichItem:
                            case "necronomicon":
                            #check for adverse affects using an integer instead of inte*2 for specialAbilityValue
                                classChange(str(cChangeDict[whichItem]),whichItem, 1, 2, 6, 2, 1, 10, 0, 15, 10, totalSummonNumber, 30)
                    if whichItem in useList:
                        match whichItem:
                            case "Diabetes Type 3":
                                trueHea = trueHea - (trueHea - 1)
                                inventory.remove(whichItem)
                                print("Item used")
                    else:
                        print("Invalid")
                else:
                    print(f"You have decided to not use {whichItem}.")

            else:
                print("That is not an option")
               # chois() 
        case "Save" | "Load" | "SL" | "C":
            save()
        case "Check Level" | "L":
            print(f"You are currently level {Level}.")
            print(f"You have {experience} EXP and you will need {experienceRequired-experience} EXP to level up.")
        case _:
            print("That is not an option.")


def where():
    global whr
    if len(livingBosses) == 1 and complete == False:
        pList.append("Domain of the Death Star")
    whr = input(f"Where would you like to go? {pList} ").replace("'","").lower()
    if whr in [x.lower().replace("'", "") for x in pList]:
        location = [x for x in pList if whr == x.lower().replace("'", "")][0] #x is the number of elems in the list
        if int(places[location]) > int(Level):
            con = input(f"Are you sure you want to go to {location}? At your current level, it is quite dangerous.").capitalize()
            if con == "Yes" or con == "Y":
                car()
            elif con == "No" or con == "N":
                print("Returning to the city.")
                chois()
            else:
                print("That is not an option")
        else:
            print(f"You are going to {location}.")
            car()
    else:
        print("That is not an option")

def encounter(noun, opening):
    global ad, itemlist, item, n, v, pv, ex, eTotHea, weapon, resource, valuable
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
    
    
    match list(noun)[0]:
        case "a" | "e" | "i" | "o" | "u":
            det = str("an")
        case _:
            det = str("a")

    if v == "looks" or v == "glares":
        ex = str("at you")
    else:
        ex = str("there")
    global opon
    if noun not in bosses:
        opon = str(f"As you {pv} down the path, {det} {noun} {v} {ex} menacingly.")
    else:
        opon = str(opening)


def fight(noun, eTotHea, eStr, eDex, ePer, eAgi, exp, bossDrop):
    spellDamage = {
        "fireball" : "5 fire damage",
        "freeze" : "5 frost damage",
        "bless" : "5 holy damage",
        "bind" : "5 damage",
        "barrage" : "10 damage",
        "curse" : "7 dark damage",
        "confusion" : "5 damage",
        "None" : "0 damage",
    }
    global summonNumber, summons, TotHea, classn, totalSummonNumber, bestiary, experience, livingBosses, usingSummon, health, nTotHea
    health = nTotHea
    strength = Str
    dexterity = Dex
    perception = Per
    agility = Agi
    if noun not in bosses:
        determiner = str("The ")
    else:
        determiner = ""
    while health > 0:
        if eTotHea > 0:
            print(opon)
            opt = input("Would you like to Fight (F), Use Item (I) or Retreat (R)? ").capitalize()
            match opt:
                case "Fight" | "F":
                    q = input("Physical (P), Spell (S) or Summon (R)? ").capitalize()
                    match q:
                        case "Physical" | "P":
                            usingSummon = False
                        case "Spell" | "S":
                            usingSummon = False
                            print(spells)
                            whichSpell = input("Which spell would you like to cast? ").replace("'","").lower()
                            if whichSpell in [x.lower().replace("'", "") for x in spells]:
                                if whichSpell.split()[0] in [x.lower().replace("'", "") for x in spellDamage]:
                                    #Works but SHOULD BE CHANGED!!
                                    #PROBLEM MAY OCCUR IF SPELL TAKES UP MORE THEN 1 LIST SPOT (IS LONGER THEN 1 WORD)
                                    #TYPE OF DAMAGE DOESN'T MATTER YET
                                    strength = int(spellDamage[whichSpell.split()[0]].split()[0])
                                    dexterity = int(whichSpell.split()[len(whichSpell.split())-1])
                                else:
                                    print("Invalid spell")
                            else:
                                print("You do not have this spell")
                        case "Summon" | "R":
                            while True:
                                print(summons)
                                whichSummon = input("Which summon would you like to use? ")
                                if whichSummon in summons:
                                    usingSummon = True
                                    health, strength, dexterity, perception, agility = summonStats[whichSummon]
                                    print(f"{health},{strength},{dexterity},{perception},{agility}")
                                else:
                                    print("Not a summon")
                                    usingSummon == False
                    repeat = str(input("How many times would you like to repeat this action? "))
                    try:
                        if repeat.isdigit() == True:
                            repeat = int(repeat)
                        else:
                            repeat = 1
                    except:
                        repeat = 1
                    finally:
                        for i in range(repeat):
                            if health <= 0:
                                break
                            else:
                                print("S")
                                NeTotHea = eTotHea
                                nTotHea = health
                                if perception+1 >= 100:
                                    eTotHea -= (strength*dexterity)*2
                                    print("You perform a Critical Hit.")
                                else:
                                    if randint(1+perception, 100) >= 90:
                                        eTotHea -= (strength*dexterity)*2
                                        print("You perform a Critical Hit.")
                                    else:
                                        eTotHea -= (int(strength) * int(dexterity))
                                        print("You perform a normal attack.")
                                if eAgi+1 >= 100:
                                    eTotHea = NeTotHea
                                    print("The attack misses the enemy.")
                                else:
                                    if randint(1+eAgi, 100) >= 90:
                                        eTotHea = NeTotHea
                                        print("The attack misses the enemy.")
                                    else:
                                        print("The attack hits the enemy.")
                                if eTotHea <= 0:
                                    eTotHea = 0
                                print(f"{determiner}{noun} currently has {eTotHea} health left.")
                                if ePer+1 >= 100:
                                    health -= (eStr*eDex)*2
                                    print("The enemy performs a Critical Hit.")
                                else:
                                    if randint(1+ePer, 100) >= 90:
                                        health -= (eStr*eDex)*2
                                        print("The enemy performs a Critical Hit.")
                                    else:
                                        health -= (int(eStr) * int(eDex))
                                        print("The enemy performs a normal attack.")
                                if agility+1 >= 100:
                                    #health = nTotHea
                                    print("The attack misses you.")
                                else:
                                    if randint(1+agility, 100) >= 90:
                                        #health = nTotHea
                                        print("The attack misses you.")
                                    else:
                                        print("The attack hits you.")
                                if health <= 0:
                                    health = 0
                                print(f"You currently have {health} health left.")
                            #break
                            
                case "Use Item" | "Use" | "Item" | "I":
                    itemUse()
                    health = health - (int(eStr) * int(eDex))
                    if health - (int(eStr) * int(eDex)) <= 0:
                        health = 0
                    print(f"You currently have {health} health left.")
                case "Retreat" | "R":
                    retreat = randint(1+agility,100)
                    if retreat >= 50:
                        print("You successfully fled, coward.")
                        nTotHea = health
                        break
                    else:
                        print("You failed to escape.")
                case "IWantToInstaKillEverything" | "IwTIsKE":
                    strength += 1000000000000000000000000000000000000000000000000000000000
                    dexterity += 1000000000000000000000000000000000000000000000000000000000000000
                    print("CHEAT ENTERED")
                case _:
                    print("That is not an option")
        if eTotHea <= 0:
            if noun not in bestiar:
                bestiar.append(noun)
                print(f"{noun.capitalize()} has been added to the bestiary.")
            else:
                print(f"{noun.capitalize()} is already in the bestiary.")
            if noun in bosses:
                inventory.append(bossDrop)
            if noun in livingBosses:
                livingBosses.remove(noun)
            if classn == "Summoner" or classn == "Necromancer":
                lootIsDropped()
                print(f"You currently have {summons} under your control.\nYou can only convert {totalSummonNumber - summonNumber} more. You will not gain experience.")
                q = input(f"Would you like to summon {noun}? ").capitalize()
                if q == "Yes" or q == "Y":
                    summonS = randint(1,2)
                    if summonS == 1:
                        if totalSummonNumber > summonNumber:
                            summons.append(noun)
                            totalSummonNumber = totalSummonNumber - 1
                            print(f"Congratulations, you gained {noun}.")
                            nTotHea = health
                            break
                    else:
                        print(f"You fail to convert the {noun}.")
                        nTotHea = health
                        break
                elif q == "No" or q == "N":
                    print(f"You give up on converting the {noun}.")
                    experience = experience + exp
                    nTotHea = health
                    break
                else:
                    print("That is not an option")
            else:
                print("ENEMY VANQUISHED")
                lootIsDropped()
                experience = experience + exp
                nTotHea = health
                break
    if health <= 0:
        if usingSummon == True:
            summons.remove(whichSummon)
            print("Your summon dies")
            usingSummon = False
        else:
            if "Potter's Heart" in inventory:
                while True:
                    q = input("Would you like to use Potter's Heart? ").title()
                    if q == "Y" or q == "Yes":
                        nTotHea = 999999999999999999999999999999999999999999999999999999999999999999
                        inventory.remove("Potter's Heart")
                        fight(noun, eTotHea, eStr, eDex, ePer, eAgi, exp, bossDrop)
                        break
                    elif q == "N" or q == "No":
                        print("You died.")
                        sys.exit()                        
                    else:
                        print("That is not an option")
            else:
                print("You died.")
                sys.exit()

def itemUse():
    global TotHea, inventory, despair, usingSummon
    healthHeal = {
        "apple" : 5,
        "Taco" : 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
    }
    despairHeal = {
        "Bradley's Blood": 10,
        "Tom's Plasma": 5,
        "William's H2O": 1,
    }
    if usingSummon == True:
        health, strength, dexterity, perception, agility = summonStats[whichSummon]
        tHea = health
    else:
        health = TotHea
        tHea = Hea*10
    print(inventory)
    q = input("Which item would you like to use? ")
    if q in inventory:
        if q in healthHeal:
            inventory.remove(q)
            if health + healthHeal[q] <= tHea:
                health += healthHeal[q]
                print(f"You currently have {health} health.")
            else:
                health = tHea
                print("Your health is maxed out")
        elif q in despairHeal:
            inventory.remove(q)
            if despair - despairHeal[q] < 0:
                despair -= despairHeal[q]
                print(f"Your despair is currently at {despair}.")
            else:
                despair = 0
                print("Your despair completely subsides")
        else:
            print("Invalid item")

def blacksmith():
    global inventory, ad, adlist, weaponModifier, new
    CraftorUpgrade = input("Would you like to craft or upgrade? ").capitalize()
    if CraftorUpgrade == "Craft":
        craft = input("What would you like to craft: sword? ").capitalize()
        if craft == "Weapon":
            if "leather" in inventory:
                if "iron" in inventory:
                    inventory.remove("leather")
                    inventory.remove("iron")
                    inventory.append("sword")
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
                        if len(splinch) == 1:
                            new = 1
                            inventory.remove(whichUp)
                            inventory.remove("iron")
                            splinch.append("+1")
                            print(splinch)
                            inventory.append(" ".join(splinch))
                            print(inventory)
                            weaponModifier.update({" ".join(splinch) : int(new)})

                    else:
                        print(f"You do not meet the requirements to upgrade {whichUp}.")
            else:
                print("You do not have this item.")    

    else:
        print("That is not an option.")

def journal():
    global honor, renown
    q = input("What would you like to view? Honor (H) or Bestiary (B). ").capitalize()
    match q:
        case "Honor" | "H":
            print(f"Title: {honor}")
            print(f"You have {renown} renown.")
        case "Bestiary" | "B":
            bestiary()
        case _:
            print("That is not an option.")

def bestiary():
    global bestiar
    bestiaryDict = {
        "botter" : "unholy blend of bear and William, the botter attacks with an impossible speed. Under its paw, the words 'William Potter is a bot at Mario Kart 8 Deluxe' are inscribed.",
        "wotter" : "unholy blend of wolf and William, the wotter terrifies others with rude slurs.",

        "otter-otter" : "unholy blend of otter and William, the otter-otter is a moron.",
        "capy-otter" : "unholy blend of capybara and William, the capy-otter is a moron.",
        "totter" : "unholy blend of toad and William, the totter is a moron.",
        "kotter" : "unholy blend of kangaroo and William, the kotter is a moron.",
        "gotter" : "unholy blend of goat and William, the gotter is a moron.",
        "cotter" : "unholy blend of cot and William, the cotter is very nice to children, specifically children (On every pedophile list).",
        "hapotter" : "unholy blend of hare and William, the hapotter is racist to monkeys.",
        "wompcrates-potter" : "blend of a Greek philosopher and William, it once said 'i think therefore i hate monkeys'."

        "bitley" : "unholy machination of beetle and Bradley, the bitley rains destruction with co-ordinated aerial strikes.",
        "itley" : "unholy machination of insect and Bradley, the itley gives malaria to children.",
        "witley" : "unholy machination of wolf and Bradley, the witley eats babies.",
        "hitley" : "unholy machination of horse and Bradley, the hitley chases babies.",
        "ditley" : "unholy machination of deer and Bradley, the ditley gets hit by cars (very poor situational awareness).",
        "citley" : "unholy machination of crocodile and Bradley, the citley bites babies but doesn't swallow (on a list).",
        "kitley" : "unholy machination of kangaroo and Bradley, the kitley kidnaps children in its pouch (on a list). ",
        "litley" : "unholy machination of lion and Bradley, the litley roars at babies (is a child itself).",
        "ritley" : "unholy machination of rat and Bradley, the ritley scurries after weak people (usually found in womp potter, womp, the wompotous potter).",
        "pterodactyley" : "unholy machination of pterodactyl and Bradley, the pterodactyley hunts after other itleys, savaging their corpses.",

        "timp" : "unholy combination of imp and Tom, the timp can't spell.",
        "tapybara" : "unholy combination of capybara and Tom, the tapybara can't spell.",
        "terodactyl" : "unholy combination of pterodactyl and Tom, the terodactyl suffers from a severe case of polydactyl.",
        "turtom" : "unholy combination of turtle and Tom, the turtom can't spell.",
        "wom" : "unholy combination of wolf and Tom, the wom can't spell.",
        "tomsect" : "unholy combination of insect and Tom, the tomsect can't spel.",
        "tont" : "unholy combination of ant and Tom, the tont can't spel.",
        "tomilla" : "unholy combination of gorilla and Tom, the tomilla can't spel.",
        "hippotomamus" : "unholy combination of hippo and Tom, the hippotomamus can't spel.",
        "tombra" : "unholy combination of cobra and Tom, the tombra can't spel.",
        "tomala" : "unholy combination of koala and Tom, the tomala can't spel.",

        "None" : "None",




        "william" : "most dumb-ass thing in existence",
        "bradley" : "most racist, bringer of polygon Jesus; bomber of a foreign country beginning with F and ending with e.",
        "tom" : "tommy gun",
        "windbreaker" : "incontrovertibly the most intelligent existence ever",
    }
    print(f"Your bestiary currently contains: {bestiar}.")
    print("DISCLAIMER: All descriptions provided by Bradley Whitley and William Potter. In no part conceptualised by Lord Windbreaker.")
    q = input("Would you like to view a certain creature? ").capitalize()
    if q == "Yes" or q == "Y":
        while True:
            which = input("Which creature would you like to view? ")
            if which in bestiar:
                print(f"{which.capitalize()}: {str(bestiaryDict[which])}")
                more = input("Would you like to view a new creature? ").capitalize()
                if more == "No" or more == "N":
                    break
                else:
                    print("You continue browsing the contents of the bestiary.")
    else:
        print("You close the bestiary.")

def renownCheck():
    global honor, renown
    if renown <= -100:
        honor = "Michael"
    elif renown <=-50 and renown > -100:
        honor = "Jeff"
    elif renown == 0:
        honor = "Neutral"
    elif renown <= 50 and renown > 100:
        honor = "Loser"
    elif renown <= 100:
        honor = "Bitch"
    else:
        honor = "Unidentified"
def experienceCheck():
    global experience, Level, experienceRequired, statUpgrade
    while True:
        experienceRequired = Level*100
        if experience >= experienceRequired:
            Level = int(Level) + 1
            statUpgrade = statUpgrade + 1
            experience = experience-experienceRequired
            if experience < experienceRequired:
                break
        else:
            break
def chooseStat():
    global statUpgrade, Cha, Str, Dex, TotHea, Per, Int, Hea, trueCha, trueStr, trueDex, trueTotHea, truePer, trueInt, trueHea
    print(f"You have:\nHealth: {TotHea}\nStrength: {Str}\nDexterity: {Dex}\n"
    f"Perception: {Per}\nCharisma: {Cha}\nIntelligence: {Int}\nYou have {str(statUpgrade)} unspent stat points.")

    if statUpgrade > 1:
        while True:
            if statUpgrade != 0:
                q = input("Where would you like to allocate your stat points? ").capitalize()
                match q:
                    case "Health" | "Hea" | "H":
                        number = int(input("How many points would you like to allocate? "))
                        if statUpgrade - number >= 0:
                            statUpgrade -= number
                            trueHea += number
                            trueTotHea = trueHea*10
                            print(f"Stat points allocated. You have {statUpgrade} stat points remaining.")
                    case "Strength" | "Str" | "S":
                        number = int(input("How many points would you like to allocate? "))
                        if statUpgrade - number >= 0:
                            statUpgrade -= number
                            trueStr += number
                            print(f"Stat points allocated. You have {statUpgrade} stat points remaining.")
                    case "Dexterity" | "Dex" | "D":
                        number = int(input("How many points would you like to allocate? "))
                        if statUpgrade - number >= 0:
                            statUpgrade -= number
                            trueDex += number
                            print(f"Stat points allocated. You have {statUpgrade} stat points remaining.")
                    case "Perception" | "Per" | "P":
                        number = int(input("How many points would you like to allocate? "))
                        if statUpgrade - number >= 0:
                            statUpgrade -= number
                            truePer += number
                            print(f"Stat points allocated. You have {statUpgrade} stat points remaining.")
                    case "Charisma" | "Cha" | "C":
                        number = int(input("How many points would you like to allocate? "))
                        if statUpgrade - number >= 0:
                            statUpgrade -= number
                            trueCha += number
                            print(f"Stat points allocated. You have {statUpgrade} stat points remaining.")
                    case "Intelligence" | "Int" | "I":
                        number = int(input("How many points would you like to allocate? "))
                        if statUpgrade - number >= 0:
                            statUpgrade -= number
                            trueInt += number
                            print(f"Stat points allocated. You have {statUpgrade} stat points remaining.")
                    case _:
                        confirm = input("Would you like to carry on allocating? ").capitalize()
                        if confirm == "No" or confirm == "N":
                            break
                        else:
                            print("You proceed to allocate stat points.")
    print(f"You have {statUpgrade} stat points left.")
    print(f"You have:\nHealth: {trueTotHea}\nStrength: {trueStr}\nDexterity: {trueDex}\n"
    f"Perception: {truePer}\nCharisma: {trueCha}\nIntelligence: {trueInt}\nYou have {str(statUpgrade)} unspent stat points.") 
    
            
def tavern():
    global gold
    drinksPrice = {
        "William's H2O": 0,
        "Bradley's Blood": 10,
        "Tom's Plasma": 25,
    }
    drinks = ["William's H2O", "Bradley's Blood", "Tom's Plasma"]
    food = {
        "apple": 5,
    }
    q = input("What would you like to do? (Buy a drink (D), Buy food (F) or Sleep (S).) ").capitalize()
    match q:
        case "Sleep" | "S":
            chooseStat()
        case "Drink" | "D":
            print(drinks)
            whichDrink = input("Which drink would you like to buy? ").replace("'","").lower()
            whichDrink = [drink for drink in drinks if drink.replace("'","").lower() in whichDrink.replace("'","").lower()]
            if whichDrink:
                whichDrink = whichDrink[0]
                if gold - drinksPrice[whichDrink] >= 0:
                    gold -= drinksPrice[whichDrink]
                    inventory.append(whichDrink)
                    print(f"You gain 1 {whichDrink}.")
                else:
                    print("You do not have enough gold")
            else:
                print("That is not an option.")
        case "Food" | "F":
            print(food)
            whichItem = input("Which item would you like to buy? ").capitalize()
            if whichItem in food:
                if gold - food[whichItem] >= 0:
                    gold -= food[whichItem]
                    inventory.append(whichItem)
                    print(f"You gain 1 {whichItem}.")
                else:
                    print("You do not have enough gold")
            else:
                print("That is not an option.")

def shrine():
    global faith
    deities = {
    "Bradely" : "deity of explosives, warcrimes and slurs. ", 
    "Will-Meister" : "the deity of arduous idiocy, ",
    "Tommy" : "deity of guns, ",
    "Lord Windbreaker" : "best mathematician"
    }
    print("Welcome to the shrine, the primary place of worship within the city. "
    f"the existing deities are {deities}.")
    while True:
        q = input("Which deity would you like to study? ").title()
        if q in deities:
            print(f"{q}, {str(deities[q])}")
            confirm = input("Would you like to worship this deity? ").capitalize()
            if confirm == "Yes" or confirm == "Y":
                if faith != "None":
                    change = input(f"You are already following {faith}. If you worship {q}, your faith in {faith} will be annulled. Do you wish to proceed? ").capitalize()
                    if change == "Yes" or change == "Y":
                        faith = q
                        print(f"You have been converted to the faith of {faith}.")
                        break
                    else:
                        print(f"You do not change faith, remaining loyal to the belief of {faith}.")
                        break
                else:
                    faith = q
                    print(f"You have entered the faith of {q}.")
                    break
            else:
                print("You decide to browse the unholy texts of the other deities.")
        else:
            print("That is not a deity worshipped here.")
            leave = input("Would you like to leave the shrine? ").capitalize()
            if leave == "Yes" or leave == "Y":
                print("You leave the shrine.")
                break
def faithBuff():
    global Str, Agi, Dex, Hea, Per, Cha, Int
    fBuff = {
        "Tommy": [-5, "Strength"],
        "Will-Meister": [-100000000, "Intelligence"],
        "Bradely": [-63, "Health"],
        "Lord Windbreaker": [+1000, "Intelligence"],
        "None" : [0, "Strength"]
    }
    count, count1 = 1, 0
    for i in range(int(len(fBuff[faith])/2)):
        match fBuff[faith][count]:
            case "Strength":
                Str += fBuff[faith][count1]
            case "Agility":
                Agi += fBuff[faith][count1]
            case "Dexterity":
                Dex += fBuff[faith][count1]
            case "Health":
                Hea += fBuff[faith][count1]
            case "Perception":
                Per += fBuff[faith][count1]
            case "Intelligence":
                Int += fBuff[faith][count1]
            case "N/A":
                print("")
        count += 2
        count1 += 2
        
def incantations():
    global gold, spells
    spellGCost = {
        "Fireball" : 50,
        "Freeze" : 50,
        "Bless" : 40,
        "Bind" : 40,
        "Barrage" : 50,
    }
    print("Elemental (E), Divine (D), Nature (N), Aether (A)\n")
    while True:
        q = input("Which category of spell would you like to see? ").capitalize()
        if q in legalSpells:
            print(spellDict[q])
            whichSpell = input("Which spell would you like to learn? ").capitalize()
            if whichSpell in spellDict[q]:
                buy = input(f"Do you want to buy {whichSpell} for {str(spellGCost[whichSpell])} gold? ").capitalize()
                if buy == "Yes" or buy == "Y":
                    gold -= spellGCost[whichSpell]
                    spells.append(spellDict[q])
                else:
                    print("You do not buy the spell.")
        else:
            print("Invalid")
            continu = input("Would you like to continue learning? ").capitalize()
            if continu == "Yes" or "Y":
                break
                
def chance():
    global modNlist, whr, gameFinish
    chanceEn = randint(1,100)
    if whr == "tomtress":
        actions = {
        1: ("timp", 25, 1, 1, 2, 10, 5, None),
        2: ("tapybara", 100, 7, 9, 5, 1, 50, None),
        3: ("terodactyl", 125, 7, 7, 4, 10, 125, None),
        4: ("turtom", 1000, 1, 1, 1, 0, 5, None),
        5: ("wom", 7, 4, 4, 10, 3, 3, None),
        6: ("tomsect", 2, 1, 1, 1, 1, 1, None),
        7: ("tont", 50, 7, 7, 3, 1, 20, None),
        8: ("tomilla", 60, 6, 2, 1, 6, 60, None),
        9: ("hippotomamus", 150, 10, 2, 3, 4, 150, None),
        10: ("tombra", 30, 2, 3, 2, 5, 15, None),
        11: ("tomala", 50, 5, 5, 3, 1, 50, None),
        }
        no, health, attack, dexterity, perception, agility, eXp, bossItem = actions[randint(1,11)]
    if whr == "whitley world":
        actions = {
        1: ("itley", 2, 1, 1, 1, 1, 1, None),
        2: ("bitley", 100, 1, 1, 7, 9, 5, None),
        3: ("witley", 25, 2, 2, 4, 5, 20, None),
        4: ("hitley", 10, 2, 2, 10, 10, 5, None),
        5: ("ditley", 7, 4, 4, 10, 3, 3, None),
        6: ("citley", 50, 7, 7, 3, 1, 20, None),
        7: ("citley", 50, 7, 7, 3, 1, 20, None),
        8: ("kitley", 20, 1, 1, 1, 8, 10, None),
        9: ("litley", 40, 6, 5, 7, 7, 80, None),
        10: ("pterodactyley", 200, 8, 8, 5, 15, 200, None),
        11: ("ritley", 2, 1, 1, 1, 1, 1, None),
        }
    if whr == "womp potter, womp, the wompotous potter":
        actions = {
        1: ("wotter", 25, 3, 3, 2, 6, 25, None),
        2: ("botter", 75, 9, 9, 1, 9, 100, None),
        3: ("otter-otter", 40, 2, 2, 6, 7, 10, None),
        4: ("capy-otter", 10, 2, 2, 4, 4, 5, None),
        5: ("wompcrates-potter", 100, 25, 21, 41, 41, 51, None),
        6: ("totter", 10, 2, 2, 5, 6, 5, None),
        7: ("kotter", 20, 4, 4, 1, 0, 20, None),
        8: ("gotter", 25, 1, 4, 3, 4, 25, None),
        9: ("cotter", 2, 1, 1, 1, 1, 2, None),
        10: ("gotter", 25, 1, 4, 3, 4, 25, None),
        11: ("hapotter", 2, 1, 1, 4, 5, 2, None),
        }
    if whr == "domain of the death star":
        actions = {
        1: ("pterodactyley", 200, 8, 8, 5, 15, 200, None),
        2: ("terodactyl", 125, 7, 7, 4, 10, 125, None),
        3: ("capy-otter", 10, 2, 2, 4, 4, 5, None),
        4: ("pterodactyley", 200, 8, 8, 5, 15, 200, None),
        5: ("terodactyl", 125, 7, 7, 4, 10, 125, None),
        6: ("capy-otter", 10, 2, 2, 4, 4, 5, None),
        7: ("pterodactyley", 200, 8, 8, 5, 15, 200, None),
        8: ("terodactyl", 125, 7, 7, 4, 10, 125, None),
        9: ("capy-otter", 10, 2, 2, 4, 4, 5, None),
        10: ("pterodactyley", 200, 8, 8, 5, 15, 200, None),
        11: ("terodactyl", 125, 7, 7, 4, 10, 125, None),
        }
    else:
        print("")
    if chanceEn <= 33:
        no, health, attack, dexterity, perception, agility, eXp, bossItem = actions[randint(1,11)]
        encounter(no, None)
        fight(no, health, attack, dexterity, perception, agility, eXp, bossItem)
    elif chanceEn <= 66 and chanceEn > 33:
        print("Placeholder")
    elif chanceEn <= 99 and chanceEn > 66:
        print("Nothing notable occurs.")
    else:
        match whr:
            case "tomtress":
                if "Tom" in livingBosses:
                    encounter("Tom", "Tom")
                    fight("Tom", 100, 7, 15, 1, 1, 10000, "tommy gun")
                else:
                    print("Tom has already died.")
            case "whitley world":
                if "Bradley" in livingBosses:
                        encounter("Bradley", "Racist Programmer")
                        fight("Bradley", 69420, 69, 420, 2000000000, 856, -432000, "Taco")
                else:
                    print("Bradley has already died.")
            case "womp potter, womp, the wompotous potter":
                if "William" in livingBosses:
                    encounter("William", "Porgy")
                    fight("William", 69418, 999, 4, 1, 88, 10000, "Diabetes Type 3")
                else:
                    print("William has already died.")
            case "domain of the death star":
                if "Windbreaker" in livingBosses:
                    encounter("Windbreaker", "Breaker of Wind")
                    fight("Windbreaker", 1, 70000000, 1500000, 1000000, 10000000, 100000000000000000, "God")
                else:
                    print("Windbreaker has already died.")
                    gameFinish = True

    
    experienceCheck()

def removeNoneFromLists(listName):
    if len(listName) > 1 and listName[0] == "None":
        listName.remove("None")

def save():
    global name, classn, faith, gold, bankedGold, experience, statUpgrade, summonNumber, totalSummonNumber, renown, honor, Level, trueStr, trueAgi, trueDex, trueHea, truePer, trueCha, trueInt, trueTotHea, inventory, spells, bestiar, achievements, equipped_items, equipped_itemsList
    try:
        open("saveFileG.txt", "x")
    except:
        print("Loading Save File")
    finally:
        q = input("Which would you like to Save (S) or Load (L)? ").title()
        if q == "Save" or q == "S":
            opens, appends = open("saveFile.txt", "w"), open("saveFile.txt", "a")
            opens.write(name+"\n"+classn+"\n"+faith+"\n"+str(gold)+"\n"+str(bankedGold)+"\n"+str(experience)+"\n"+str(statUpgrade)+"\n"+str(summonNumber)+"\n"+str(totalSummonNumber)+"\n"+str(renown)+"\n"+honor+"\n"+str(Level)+"\n"+str(trueStr)+"\n"+str(trueAgi)+"\n"+str(trueDex)+"\n"+str(trueHea)+"\n"+str(truePer)+"\n"+str(trueCha)+"\n"+str(trueInt)+"\n"+str(trueTotHea)+"\n")
            count1 = 0
            for i in range(len(inventory)):
                appends.write(inventory[count1]+", ")
                count1 += 1
            appends.write("\n")
            count1 = 0
            for i in range(len(spells)):
                appends.write(spells[count1]+", ")
                count1 += 1
            appends.write("\n")
            count1 = 0
            for i in range(len(bestiar)):
                appends.write(bestiar[count1]+", ")
                count1 += 1
            appends.write("\n")
            count1 = 0
            for i in range(len(originClass)):
                appends.write(originClass[count1]+", ")
                count1 += 1
            appends.write("\n")
            count1 = 0
            for i in range(len(livingBosses)):
                appends.write(livingBosses[count1]+", ")
                count1 += 1
            appends.write("\n")
            count1 = 0
            for i in range(len(summons)):
                appends.write(summons[count1]+", ")
                count1 += 1
            appends.write("\n")
            with open("achievementsG.txt", "w") as data:
                data.write(str(achievements))
            with open("equippedItemsG.txt", "w") as data:
                count1 = 0
                for i in range(len(equipped_itemsList)):
                    data.write(equipped_itemsList[count1]+", ")
                    count1 += 1
                appends.write("\n")
            opens.close()
        elif q == "Load" or q == "L":
            opens = open("saveFileG.txt", "r")
            name, classn, faith, gold, bankedGold, experience, statUpgrade, summonNumber, totalSummonNumber, renown, honor, Level, trueStr, trueAgi, trueDex, trueHea, truePer, trueCha, trueInt, trueTotHea, inventory, spells, bestiar = opens.readline(), opens.readline(), opens.readline(), int(opens.readline()), int(opens.readline()), int(opens.readline()), int(opens.readline()), int(opens.readline()), int(opens.readline()), int(opens.readline()), opens.readline(), int(opens.readline()), int(opens.readline()), int(opens.readline()), int(opens.readline()), int(opens.readline()), int(opens.readline()), int(opens.readline()), int(opens.readline()), int(opens.readline()), opens.readline().split(","), opens.readline().strip().split(","), opens.readline().strip().split(",") 
            count2 = 0
            for x in inventory:
                inventory[count2] = inventory[count2].strip()
                count2 += 1
            inventory.pop(len(inventory)-1)
            count2 = 0
            for x in spells:
                spells[count2] = spells[count2].strip()
                count2 += 1
            spells.pop(len(spells)-1)
            count2 = 0
            for x in bestiar:
                bestiar[count2] = bestiar[count2].strip()
                count2 += 1
            bestiar.pop(len(bestiar)-1)
            count2 = 0
            for x in originClass:
                originClass[count2] = originClass[count2].strip()
                count2 += 1
            count2 = 0
            for x in livingBosses:
                livingBosses[count2] = livingBosses[count2].strip()
                count2 += 1
            count2 = 0
            for x in summons:
                summons[count2] = summons[count2].strip()
                count2 += 1
            count = 0
            try:
                spells.remove("None")
                bestiar.remove("None")
                originClass.remove("None")
                livingBosses.remove("None")
                summons.remove("None")  
            except:
                print("")
            with open("achievementsG.txt", "r") as data:
                achievements = data.readline().strip().split(",")
            with open("equippedItemsG.txt", "r") as data:
                equipped_itemsList = data.readline().strip().split(",")
                print(equipped_itemsList)
                count, count1 = 0, 1
                equipped_items.clear()
                for i in range(int(len(equipped_itemsList)/2)):
                    equipped_items.update({equipped_itemsList[count].strip() : equipped_itemsList[count1].strip()})
                    count += 2
                    count1 += 2
            opens.close()
        else:
            print("Exiting Save Files")


def chois():
    global carry, inventoryTwo, trueStr, trueAgi, trueDex, trueHea, truePer, trueCha, trueInt, Str, Agi, Dex, Hea, Per, Cha, Int, gameFinish
    count = 0
    for i in range(len(listsConfig)):
        removeNoneFromLists(listsConfig[count])
        count += 1
    Str, Agi, Dex, Hea, Per, Cha, Int = trueStr, trueAgi, trueDex, trueHea, truePer, trueCha, trueInt
    statBoosts(equipped_items["Head"])
    statBoosts(equipped_items["Chest"])
    statBoosts(equipped_items["Gloves"])
    statBoosts(equipped_items["Leggings"])
    statBoosts(equipped_items["Boots"])
    statBoosts(equipped_items["Right Hand"])
    statBoosts(equipped_items["Left Hand"])
    faithBuff()
    renownCheck()
    experienceCheck()
    TotHea = Hea * 10
    while True:
        if len(livingBosses) == 0:
            gameFinish == True
        if gameFinish == True:
            print("Check new file")
            with open("conclusion.txt", "a") as data:
                data.write("Well done\nYou finish game\nEnding")
        townQuestion = input("\nWhere would you like to go?"
                    " You may go to "
                    " the Blacksmith (W), the Armory (A), the Bank (B),"
                    " the Tavern (H), the Shrine (S),"
                    " the Market (M), the Menu,"
                    " the Incantation Store (I) or back Out (O). ").title()
        match townQuestion:
            case "Market" | "M":
                print("Going to the Market\n")
                shop()
                chois()
            case "Blacksmith" | "W":
                print("Going to the Blacksmith\n")
                blacksmith()
                #NOTE: The function can be used within its definition, as shown below
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
            case "Tavern" | "H":
                tavern()
                chois()
            case "Shrine" | "S":
                shrine()
                chois()
            case "Incantations" | "Incantation Store" | "I":
                incantations()
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