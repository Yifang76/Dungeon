from random import *
import sys
gold, bankedGold = 0, 0
statUpgrade, experience = 0, 0
summonNumber = int(0)
totalSummonNumber = None
activeBounties = []
bestiar = []
inventory = ["helmet", "sword"]
spells = []
faith = None
eTotHea = int(1)
carry = True
summons = []
shopStock, bankedItems = [], []
n = None
renown = 0
hEqItem, cEqItem, lEqItem, gEqItem, bEqItem, rhEqItem, lhEqItem = None, None, None, None, None, None, None
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

name = input("Name, please ").capitalize()
print("Knight: (Strength: 10, Agility: 3, Dexterity: 8,\nHealth: 7, Perception: 4, Charisma: 6 (Within lawful lands) or 0 (in foreign lands),\nIntelligence: 5)")
print("Merchant: (Strength: 1, Agility: 8, Dexterity: 1,\nHealth: 3, Perception: 8, Charisma: 10,\nIntelligence: 6)")
print("Summoner: (Strength: 1, Agility: 4, Dexterity: 1,\nHealth: 2, Perception: 9, Charisma: 2,\nIntelligence: 8)")
print("Mage: (Strength: 2, Agility: 4, Dexterity: 4,\nHealth: 5, Perception: 7, Charisma: 3,\nIntelligence: 10)")
attriQuery = input("Would you like a guide on the attributes? ").capitalize()
if attriQuery == "Yes":
    print("Strength determines the base damage you do, Agility determines your evasion, Dexterity determines base damage,\nPerception determines your critical chance, Charisma determines your barter rate and speech, Intelligence determines your spellcraft\nand Health determines your HP.")
def classv(LevelG, StrG, AgiG, DexG, HeaG, PerG, ChaG, IntG, TotHeaG):
    global Level, Str, Agi, Dex, Hea, Per, Cha, Int, TotHea
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
                print("Wolf")
                whichSummo = input("Which summon would you like to start with? ").capitalize()
                if whichSummo == "Wolf":
                    summons.append("wolf")
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
        case "Tom":
            if name == "Tom":
                classv()
                break
        case "William":
            if name == "William":
                classv(120,3,3,3,5,3,0,10,50)
                break
        case _:
            print("That is not an option")
#Meant To be Empty to store Values
weaponModifier = {

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
    "Giant's Mausoleum" : 100,
}

fenceDict = {
    "necronomicon" : 10,
    "demon heart" : 20,
    "dragon scale" : 50,
    "human flesh" : 5,
    "dragon tooth" : 50
}

pList = ["Stormcrag", "Havoc's Rock", "Duskmire", "Ironhold", "Thornwood", "Giant's Mausoleum"]
crime = {}
liteList = [
"leather", "iron" ]
enemyList = ["imp", "warlord", "dictator", "insect", "bandit", "ent", "wolf"]
originClass = []
ascensionItems = ["Vanta's vessel", "Murmur's mask, Lautrec's boon"]
invalidSell = ["King's Charter"]
illItems = ["necronomicon", "demon heart", "dragon scale", "human flesh"]
#cChangeItem are all items that perform a class change
cChangeItem = ["necronomicon", "demon heart", "dragon tooth"]
safe = ["Cetus","Ashborn"]
livingBosses = ["Reign", "Quasar", "The Wicked",]
bosses = ["Reign", "Quasar", "The Wicked",]
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

requirements = ["teleport scroll", "dandylion", "burdock",
    "protect scroll", "pipewort", "ragwort",
    "sprites scroll", "snapdragon", "toadflex",
    "zombie scroll", "devilsbit", "bones",
    "swift scroll", "speedwell", "sage",
    "freeze scroll", "bind weed", "bog weed",
    "doppleganger scroll", "fox glove", "catsear",
    "invisible scroll", "chondrilla", "hemlock",
    "reverse scroll", "thistle", "skullcap",
    "heal scroll", "balm", "feverfew",
    "fireball scroll", "dragonsteeth", "mousetail",
    "lightning scroll", "cud weed", "knap weed"
    ]
create = ["teleport scroll", "protect scroll", "sprites scroll", "zombie scroll", "swift scroll", "freeze scroll",
    "doppleganger scroll", "invisible scroll", "reverse scroll", "heal scroll", "fireball scroll", 
    "lightning scroll"]
summonStats = {
    "imp": (25, 1, 1, 2, 10,),
    "warlord": (100, 7, 9, 5, 1,),
    "dictator": (75, 3, 3, 1, 5,),
    "bandit": (10, 2, 2, 10, 10,),
    "wolf": (7, 4, 4, 10, 3,),
    "insect": (2, 1, 1, 1, 1,),
    "ent": (50, 7, 7, 3, 1,),
    "insect": (2, 1, 1, 1, 1,),
    "insect": (2, 1, 1, 1, 1,),
    "insect": (2, 1, 1, 1, 1,),
    "insect": (2, 1, 1, 1, 1,),
}
nTotHea = TotHea
#NEED TO TEST
def classChange(newClass, itemUsing, lev, stre, agi, dex, hea, per, cha, inte, totHea, specialAbility, specialAbilityValue):
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

def crimCheck(tim):
    global crime
    if tim.split()[1] == "Years" or tim.split()[1] == "Year":
        crime.update({str("Years"): (crime["Years"]) + int(tim.split()[0])})

    if tim.split()[1] == "Months" or tim.split()[1] == "Month":
        crime.update({str("Months"): (crime["Months"]) + int(tim.split()[0])})

    if tim.split()[1] == "Days" or tim.split()[1] == "Day":
        crime.update({str("Days"): (crime["Days"]) + int(tim.split()[0])})
    return (""+str(crime["Years"])+" year(s), "+str(crime["Months"])+" month(s) and "+str(crime["Days"])+" day(s)") #When f"" used [ is declared as unmatched

def guard(statement, tim, place):
    q = input(f"You are charged with {statement}. You will be sentenced for {crimCheck(tim)}. "
    "What will you do? (Resist Arrest (F), Evade Arrest (E) Bribe Guard (B), "
    "Persuade Guard (P) Intimidate Guard (I) or Accept Arrest (A)) ").capitalize()
    answer = False
    while answer == False:
        match q:
            case "Resist Arrest" | "Resist" | "Fight" |"F":
                guardF(place)
            case "Evade Arrest" | "Evade" |"E":
                guardE(place,tim)
            case "Accept Arrest" | "Accept" | "A":
                guardA()
            case "Bribe Guard" | "Bribe" | "B":
                guardB(place)
            case "Persuade Guard" | "Persuade" | "P":
                print("Persuade")
            case "Intimidate Guard" | "Intimidate" | "I":
                print("Intimidate")
            case _:
                print("Hey, stop trying to evade justice!")

#eStr and (presumably) eDex undefined. Try using method in chance?
#danger not defined and time not defined, along with eStr and eDex
def guardF(place):
    global summonNumber, summons, TotHea, classn, totalSummonNumber, tim
    enemyHealth = {
        "Cetus" : 10,
        "Ashborn" : 50,
    }
    eTotHea = int(enemyHealth[place])
    while TotHea > 0:
        if eTotHea > 0:
            opt = input("What will you do? (Fight (F), Use Item (U), Surrender (S) or Retreat (R).) ").capitalize()
            match opt:
                case "Fight" | "F":
                    eTotHea = eTotHea - (int(Str) * int(Dex))
                    print(f"The guard currently has {eTotHea} health left.")
                    TotHea = TotHea - (int(eStr) * int(eDex))
                    print(f"You currently have {TotHea} health left.")
                case "Use Item" | "Use" | "Item" | "I":
                    print("Item")
                case "Surrender" | "S":
                    print("Surrender")
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
            tim = str(int(tim.split()[0]) + int(5)) +" "+tim.split()[1]
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
            tim = str(int(tim.split()[0]) + int(5)) +" "+tim.split()[1]
            crimCheck(tim)
            print(f"Wounded, you are dragged to prison by the guards, sentence increasing to {tim}.")
            if classn == "Knight":
                #CHANGE LINE UNDER THIS COMMENT TO ACCOUNT FOR MULTIPLE ITEMS. (E.G. King's Charter, Queen's Pardon, ect.)
                if "King's Charter" in inventory:
                    inventory.remove("King's Charter")
                    print("Due to your crime, you have lost the King's Charter.")
                    
        else:
            print("You died")
            sys.exit()

#Need to Run
def guardE(place,tim):
    global crime
    q = randint(1,100-Agi)
    if q <= 10:
        print("You successfully escaped the guards, however your crime has not been forgotten.")
        crimeCheck(tim)
    else:
        guardF(place)

#ADD
def guardA():
    print("You have been apprehended.")

def guardB(place):
    bribe = {
        "Cetus" : 100,
    }
    if place in bribe:
        if int(bribe[place])-Cha <= 0:
            print(f"Give me {int(bribe[place])} gold and we'll call it even.")
            if q == "Yes" or q == "Y":
                gold = gold - int(bribe[place])
                print(f"You have {gold} gold left.")
                tim = 0
            else:
                guardF(place)
        success = randint(1,int(bribe[place])-Cha)
        if success < 10:
            print(f"Give me {int(bribe[place])} gold and we'll call it even.")
            if q == "Yes" or q == "Y":
                gold = gold - int(bribe[place])
                print(f"You have {gold} gold left.")
                tim = 0
            else:
                guardF(place)
        else:
            print("No bribery!")
            guardF(place)


    else:
        print("How dare you try to bribe an officer of the law!")
        tim = str(int(tim.split()[0]) + int(5)) +" "+tim.split()[1]
        crimCheck(tim)


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
                    guard("intention to sell an illegal item", "20 years","Cetus")
                    break
            else:
                print("I see, I see. Well then, guards!")
                guard("intention to sell an illegal item", "20 years","Cetus")
                break
        else:
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
                if sellWhich in ascensionItems:
                    print("Sorry; that's useless.")
                    break
                else:
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


def correctPA(q, correctP):
    count = 0
    while count < len(correctP)-1:
        if q.split()[count] in correctP:
            return True
        else:
            count += 1
    print("Invalid item for slot")


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
            if whichEq in available_items and correctPA(whichEq,whereEq+"CorrectPlace") == True:
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
        "necronomicon" : "Necromancer",
        "demon heart" : "Demon",
        "dragon tooth" : "Dragonkin",
        "Vanta's vessel" : "Lost Soul",
    }

    spellDescDict = {
        "fireball" : "Basic sorcery for Elemental mages.\nFire was once deemed as taboo before its uses were brought to light.\nDeals 5 base fire damage multiplied by upgrade level.",
        "curse" : "Basic sorcery for Occult mages.\n Once upon a time, occult magic was accepted in society, acting as a parallel to faith; after the First Tragedy, it's hideous visage was truly revealed to the world",
    
        "Abyssal Antonym" : "",
        "Cursed Call" : "",
        "Legacy's Lightning" : "",
        "Murphy's Madness" : "",
        "Soul Snatcher" : "",
        "" : "",
    }
    weaponDescDict = {
        "sword" : "A common sword, favoured by scavengers lucky enough to find one.",
        "Brandle" : "Brandle, Giant Slayer. Once wielded by a warmaster involved in the giant wars, this blade was used to fell many a giant. Its legend, whilst forgotten to many, still imbues this blade with giant-slaying capabilities.\n"
        "And when the Giant Slayer died in battle, fallen like so many of his men, his soul couldn't bear. And so, his life became forfeit as he held onto one purpose. To slay giants. Thus, the urban legend of The Wicked was formed.",
        "Vanta's Vessel" : "Vessel of Vanta the Vile, crushed by a destructive force unfamiliar to the natural order",
        "Murmur's Mask" : "Mask of Murmur the Maelstrom, a silent force is imbued within the mask's eyes. It is said that when worn, one can hear the sounds of the sea."
        "Skrill's Spine" : "",
        "Fortress' Fangs" : "",
        #Need to edit to account for '

    }
    summonsDict = {
        "Frost Knight Theodore" : "",
        "Magma Blade Entil" : "",
    }
    q = input("What would you like to do. View Stats (S), View Inventory (I), View Journal (J),"
    " View Spells (T), View Summons (M), Use Item (U) or Check Level (L). ").capitalize()
    match q:
        case "View Stats" | "Stats" | "S":
            print(f"Without modifiers, you have:\nHealth: {TotHea}\nStrength: {Str}\nDexterity: {Dex}\n"
            f"Perception: {Per}\nCharisma: {Cha}\nIntelligence: {Int} ")
        #    print(f"With modifiers, you have:\nHealth: {nTotHea}\nStrength: {nStr}\n Dexterity: {nDex}"
        #    f"Perception: {nPer}\nCharisma: {nCha}\nIntelligence: {nInt} ")
        case "View Inventory" | "Inventory" | "I":
            print(f"You currently carry {inventory}.")
            checkDesc = input("Would you like to check an item description? ").capitalize()
            if checkDesc == "Yes" or checkDesc == "Y":
                whichDesc = input("Which item would you like check? ")
                if whichDesc in inventory:
                    print(f"{whichDesc.capitalize()}: {str(weaponDescDict[whichDesc])}")
                else:
                    print(f"You do not have {whichDesc}.")
            elif checkDesc == "No" or checkDesc == "N":
                print("You conclude your check.")
            else:
                print("That is not an option")
        case "View Summons" | "Summons" | "M":
            print(summons)
            q = input("Which summon would you like to view? ")
            if q in summonsDict and q in summons:
                print(summonsDict[q])
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

                else:
                    print(f"You have decided to not use {whichItem}.")

            else:
                print("That is not an option")
               # chois() 
        case "Check Level" | "L":
            print(f"You are currently level {Level}.")
            print(f"You have {experience} EXP and you will need {experienceRequired-experience} EXP to level up.")
        case _:
            print("That is not an option.")



#Possibly Uneeded
def nounList(firstV, secondV, thirdV, fourthV, fifthV, sixthV, seventhV, eighthV, ninthV, tenthV):
    global n, modNlist
    nlist = [firstV, secondV, thirdV, fourthV, fifthV, sixthV, seventhV, eighthV, ninthV, tenthV]
    modNlist = [item for item in nlist if item is not None]
    print(modNlist)
    n = choice(modNlist)

def where():
    global whr
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
                    q = input("Physical (P), Spell (S), Incantation (I) or Summon (R)? ").capitalize()
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
                        case "Incantation" | "I":
                            usingSummon = False
                            print("Incantation")
                        case "Summon" | "R":
                            print(summons)
                            whichSummon = input("Which summon would you like to use? ")
                            if whichSummon in summons:
                                usingSummon = True
                                health, strength, dexterity, perception, agility = summonStats[whichSummon]
                                print(f"{health},{strength},{dexterity},{perception},{agility}")
                            else:
                                print("Not a summon")
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
            print("You died.")
            sys.exit()

def itemUse():
    global TotHea, inventory, despair
    healthHeal = {
        "apple" : 5,
        "1" : 10,
    }
    despairHeal = {
        "Malchor's Maltor": 1,
        "Alastor's Anchor": 5,
        "Intrail's Ichor": 10,
    }
    if usingSummon == True:
        health, strength, dexterity, perception, agility = summonStats[whichSummon]
        trueHea = health
    else:
        health = TotHea
        trueHea = Hea*10
    print(inventory)
    q = input("Which item would you like to use? ")
    if q in inventory:
        if q in healthHeal:
            inventory.remove(q)
            if health + healthHeal[q] <= trueHea:
                health += healthHeal[q]
                print(f"You currently have {health} health.")
            else:
                health = trueHea
                print("Your health is maxed out")
        if q in despairHeal:
            inventory.remove(q)
            if despair - despairHeal[q] < 0:
                despair -= despairHeal[q]
                print(f"Your despair is currently at {despair}.")
            else:
                despair = 0
                print("Your despair completely subsides")

def blacksmith():
    global inventory, ad, adlist, weaponModifier, new
    CraftorUpgrade = input("Would you like to craft or upgrade? ").capitalize()
    if CraftorUpgrade == "Craft":
        craft = input("What would you like to craft: charm or weapon? ").capitalize()
        if craft == "Charm":
            if "gem" in inventory:
                if "leather" in inventory:
                    inventory.remove("gem")
                    inventory.remove("leather")
                    newCharm = ad + "charm"
                    rarities(newCharm)
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
                            if splinch[0] == "Charm":
                                inventory.remove("iron")
                                inventory.remove(whichUp)
                                inventory.append(ad + splinch[1])
                                print(inventory)
                            else:
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
                                    inventory.remove(whichUp)
                                    inventory.remove("iron")
                                    ne = splinch[len(splinch)-1].replace("+","")
                                    ne = int(ne) + 1
                                    new = "+" + str(ne)
                                    splinch.remove(splinch[len(splinch)-1])
                                    splinch.append(new)
                                    inventory.append(" ".join(splinch)) 
                                    print(inventory)
                                    weaponModifier.update({" ".join(splinch) : ne})
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

def alchemist():
    print(create)
    q = input("Which item would you like to create? ")
    if q in create:
        h = requirements.index(q)
        print(f"You need {requirements[h+1]} and {requirements[h+2]}")
        cauldron(q, requirements.index(q))

def cauldron(item, herb):
  if requirements[herb+1] in inventory and requirements[herb+2] in inventory:
    inventory.remove(requirements[herb+1])
    inventory.remove(requirements[herb+2])
    inventory.append(item)
    print(item+" has been created")
  else:
    print("Cannot create "+item+": you don't have the correct herbs")

def trainer():
    print("Knight, Summoner, Berserker, Mage, Priest")
    while True:
        classn = input("Which class would you like to become? ").capitalize()
        match classn:
            case "Knight":
                classv(15, 10, 3, 8, 7, 4, 6, 5, 70)
                inventory.append("King's Charter")
                break
            case "Summoner":
                classv(5, 1, 4, 1, 2, 9, 2, 8, 20)
                totalSummonNumber = Int
                break
            case "Berserker":
                print("Berserker")
                break
            case "Mage":
                print("Mage")
                break
            case "Priest":
                print("Priest")
                break
            case "Tom":
                if name == "Tom":
                    classv()
                    break
            case "William":
                if name == "William":
                    classv(120,3,3,3,5,3,0,10,50)
                    break
            case _:
                print("That is not an option")

def journal():
    global honor, renown
    q = input("What would you like to view? Honor (H), Bestiary (B), Quests (Q) or Bounties (C). ").capitalize()
    match q:
        case "Honor" | "H":
            print(f"Title: {honor}")
            print(f"You have {renown} renown.")
        case "Bestiary" | "B":
            bestiary()
        case "Quests" | "Q":
            print("Active Quests Go Here")
        case "Bounties" | "C":
            print(activeBounties)
        case _:
            print("That is not an option.")

def bestiary():
    global bestiar
    bestiaryDict = {
        "imp" : "an imp",
        "dictator" : "a dictator",
        "warlord" : "a warlord",
        "insect" : "an insect",
        "bandit" : "a bandit",
        "ent" : "an ent",
        "wolf" : "a wolf",
    }
    print(f"Your bestiary currently contains: {bestiar}.")
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
        honor = "Villain"
    elif renown <=-50 and renown > -100:
        honor = "Feared"
    elif renown == 0:
        honor = "Neutral"
    elif renown <= 50 and renown > 100:
        honor = "Loved"
    elif renown <= 100:
        honor = "Hero"
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
    global statUpgrade, Cha, Str, Dex, TotHea, Per, Int, Hea
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
                            Hea += number
                            TotHea = Hea*10
                            print(f"Stat points allocated. You have {statUpgrade} stat points remaining.")
                    case "Strength" | "Str" | "S":
                        number = int(input("How many points would you like to allocate? "))
                        if statUpgrade - number >= 0:
                            statUpgrade -= number
                            Str += number
                            print(f"Stat points allocated. You have {statUpgrade} stat points remaining.")
                    case "Dexterity" | "Dex" | "D":
                        number = int(input("How many points would you like to allocate? "))
                        if statUpgrade - number >= 0:
                            statUpgrade -= number
                            Dex += number
                            print(f"Stat points allocated. You have {statUpgrade} stat points remaining.")
                    case "Perception" | "Per" | "P":
                        number = int(input("How many points would you like to allocate? "))
                        if statUpgrade - number >= 0:
                            statUpgrade -= number
                            Per += number
                            print(f"Stat points allocated. You have {statUpgrade} stat points remaining.")
                    case "Charisma" | "Cha" | "C":
                        number = int(input("How many points would you like to allocate? "))
                        if statUpgrade - number >= 0:
                            statUpgrade -= number
                            Cha += number
                            print(f"Stat points allocated. You have {statUpgrade} stat points remaining.")
                    case "Intelligence" | "Int" | "I":
                        number = int(input("How many points would you like to allocate? "))
                        if statUpgrade - number >= 0:
                            statUpgrade -= number
                            Int += number
                            print(f"Stat points allocated. You have {statUpgrade} stat points remaining.")
                    case _:
                        confirm = input("Would you like to carry on allocating? ").capitalize()
                        if confirm == "No" or confirm == "N":
                            break
                        else:
                            print("You proceed to allocate stat points.")
    print(f"You have {statUpgrade} stat points left.")
    print(f"You have:\nHealth: {TotHea}\nStrength: {Str}\nDexterity: {Dex}\n"
    f"Perception: {Per}\nCharisma: {Cha}\nIntelligence: {Int}\nYou have {str(statUpgrade)} unspent stat points.") 
    
            
def tavern():
    global gold
    drinksPrice = {
        "Malchor's Maltor": 10,
        "Alastor's Anchor": 25,
        "Intrail's Ichor": 100,
    }
    drinks = ["Malchor's Maltor", "Alastor's Anchor", "Intrail's Ichor"]
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

#ADD A SEPARATOR (E.G.) # MAYBE TRY bountyList.append(state"#")?
def bounty():
    global liteList, enemyList, activeBounties, bount
    bount = {}
    bountyList = []
    for i in range(5):
        rand = randint(1,2)
        if rand == 1:
            which = choice(enemyList)
            act = "Kill"
        else:
            which = choice(liteList)
            act = "Retrieve"
        rend = randint(1,10)
        cos = randint(1,50)
        if rend == 1:
            state = f"{act} {rend} {which} ({cos} gold). "
        else:
            state = f"{act} {rend} {which}s ({cos} gold). "
        bountyList.append(state)
        bount.update({state : cos})
    while True:
        print(bountyList)
        q = int(input("Which bounty would you like to take? 0 (first) - 4 (last). "))
        if q >= 0 and q <= 4:
            activeBounties.append(bountyList[q])
            bountyList.remove(bountyList[q])
            print(f"Active commissions: {activeBounties}")
            break
        else:
            print("Invalid")
            leave = input("Would you like to leave the Commission Board? ").capitalize()
            if leave == "Yes" or leave == "Y":
                print("You leave the commission board.")
                break
            else:
                print("You gaze upon the bounties on display.")
def shrine():
    global faith
    deities = {
    "Galadrialus" : "the deity of warriors and gladiators alike. ", 
    "2" : "the deity of 2____, ",
    "3" : "the deity of 3____, ",
    "4" : "the deity of 4____, ",
    "5" : "the deity of 5____, ",
    }
    print("Welcome to the shrine, the primary place of worship within the city. "
    f"the existing deities are {deities}.")
    while True:
        q = input("Which deity would you like to study? ").capitalize()
        if q in deities:
            print(f"{q}, {str(deities[q])}")
            confirm = input("Would you like to worship this deity? ").capitalize()
            if confirm == "Yes" or confirm == "Y":
                if faith != None:
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
                print("You decide to browse the holy texts of the other deities.")
        else:
            print("That is not a deity worshipped here.")
            leave = input("Would you like to leave the shrine? ").capitalize()
            if leave == "Yes" or leave == "Y":
                print("You leave the shrine.")
                break
def faithBuff():
    fBuff = {
        "Galadrialus": "+5 Str"
    }
    if faith in fBuff:
        fate = fBuff[faith].split()
        if len(fate) > 2:
            count = 1
            for i in range(int(fate/2)):
                if fate[count] == "":
                    variable = variable + fate[count-1]
        else:
            if fate[count] == "":
                variable = variable + fate[count-1]

        
def incantations():
    global gold, spells
    spellGCost = {
        "Fireball" : 50,
        "Freeze" : 50,
        "Bless" : 40,
        "Bind" : 40,
        "Barrage" : 50,
    }
    print("Elemental (E), Divine (D), Nature (N), Aether (A)")
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
    global modNlist, whr
    chanceEn = randint(1,100)
    if whr == "thornwood":
        #Works but MAKE MORE EFFICIENT!
        actions = {
        1: ("imp", 25, 1, 1, 2, 10, 5, None),
        2: ("warlord", 100, 7, 9, 5, 1, 50, None),
        3: ("dictator", 75, 3, 3, 1, 5, 25, None),
        4: ("bandit", 10, 2, 2, 10, 10, 5, None),
        5: ("wolf", 7, 4, 4, 10, 3, 3, None),
        6: ("insect", 2, 1, 1, 1, 1, 1, None),
        7: ("ent", 50, 7, 7, 3, 1, 20, None),
        8: ("insect", 2, 1, 1, 1, 1, 1, None),
        9: ("insect", 2, 1, 1, 1, 1, 1, None),
        10: ("insect", 2, 1, 1, 1, 1, 1, None),
        11: ("insect", 2, 1, 1, 1, 1, 1, None),
        }
    if whr == "ironhold":
        actions = {
        1: ("im", 25, 1, 1, 1, 1, 1, None),
        2: ("wrlord", 100, 7, 9, 1, 1, 1, None),
        3: ("dctator", 75, 3, 3, 1, 1, 1, None),
        4: ("bndit", 10, 2, 2, 1, 1, 1, None),
        5: ("wlf", 7, 4, 4, 1, 1, 1, None),
        6: ("nsect", 2, 1, 1, 1, 1, 1, None),
        7: ("nt", 50, 7, 7, 1, 1, 1, None),
        8: ("nsect", 2, 1, 1, 1, 1, 1, None),
        9: ("nsect", 2, 1, 1, 1, 1, 1, None),
        10: ("nsect", 2, 1, 1, 1, 1, 1, None),
        11: ("nsect", 2, 1, 1, 1, 1, 1, None),
        }
    if whr == "stormcrag":
        actions = {
        1: ("ip", 25, 1, 1, 1, 1, 1, None),
        2: ("walord", 100, 7, 9, 1, 1, 1, None),
        3: ("ditator", 75, 3, 3, 1, 1, 1, None),
        4: ("banit", 10, 2, 2, 1, 1, 1, None),
        5: ("wof", 7, 4, 4, 1, 1, 1, None),
        6: ("inect", 2, 1, 1, 1, 1, 1, None),
        7: ("en", 50, 7, 7, 1, 1, 1, None),
        8: ("inect", 2, 1, 1, 1, 1, 1, None),
        9: ("inect", 2, 1, 1, 1, 1, 1, None),
        10: ("inect", 2, 1, 1, 1, 1, 1, None),
        11: ("inect", 2, 1, 1, 1, 1, 1, None),
        }
    if whr == "havocs rock":
        actions = {
        1: ("ip", 25, 1, 1, 1, 1, 1, None),
        2: ("walord", 100, 7, 9, 1, 1, 1, None),
        3: ("ditator", 75, 3, 3, 1, 1, 1, None),
        4: ("banit", 10, 2, 2, 1, 1, 1, None),
        5: ("wof", 7, 4, 4, 1, 1, 1, None),
        6: ("inect", 2, 1, 1, 1, 1, 1, None),
        7: ("en", 50, 7, 7, 1, 1, 1, None),
        8: ("inect", 2, 1, 1, 1, 1, 1, None),
        9: ("inect", 2, 1, 1, 1, 1, 1, None),
        10: ("inect", 2, 1, 1, 1, 1, 1, None),
        11: ("inect", 2, 1, 1, 1, 1, 1, None),
        }
    if whr == "giants mausoleum":
        actions = {
        1: ("shade", 25, 1, 1, 1, 1, 1, None),
        2: ("ghoul", 100, 7, 9, 1, 1, 1, None),
        3: ("spirit", 75, 3, 3, 1, 1, 1, None),
        4: ("ice spirit", 10, 2, 2, 1, 1, 1, None),
        5: ("snow wolf", 7, 4, 4, 1, 1, 1, None),
        6: ("glacice", 2, 1, 1, 1, 1, 1, None),
        7: ("mammoth", 50, 7, 7, 1, 1, 1, None),
        8: ("zombie", 2, 1, 1, 1, 1, 1, None),
        9: ("skeleton", 2, 1, 1, 1, 1, 1, None),
        10: ("half giant", 2, 1, 1, 1, 1, 1, None),
        11: ("shambling giant", 2, 1, 1, 1, 1, 1, None),
        }
    else:
        print("")
    if chanceEn <= 33:
        no, health, attack, defense, perception, agility, eXp, bossItem = actions[randint(1,11)]
        encounter(no, None)
        fight(no, health, attack, defense, perception, agility, eXp, bossItem)
    elif chanceEn <= 66 and chanceEn > 33:
        print("Placeholder")
    elif chanceEn <= 99 and chanceEn > 66:
        print("Nothing notable occurs.")
    else:
        match whr:
            case "thornwood":
                if "" in livingBosses:
                    encounter("Name", "Statement")
                    fight("Name", 100, 7, 15, 1, 1, 10000, "Drop")
                else:
                    print("Placeholder")
            case "ironhold":
                encounter("Precept", "From the depths of Ironhold, the mechanical Precept, life of the city, reveals itself.")
                fight("Precept", 5000, 15, 30, 1, 15000, "Machine Eye")
            case "stormcrag":
                encounter()
                fight()
            case "giant's mausoleum":
                if "The Wicked" in livingBosses:
                    encounter("The Wicked", "Rising from the corpses of the fallen giants, The Wicked rises for vengeance.")
                    fight("The Wicked", 100, 7, 15, 25, 50, 10000, "Brandle")
                else:
                    print("The corpse of The Wicked has disappeared.")
    experienceCheck()
    
#DELETE FROM HERE

def save():
    opens = open("saveFile.txt", "r")
    if opens:
        q = input()
        if q == "Save" or q == "S":
            opens.write("\n"+name+"\n"+inventory)
            opens.close()
    else:
        creates = open("saveFile.txt", "x")
        























#TO HERE


def chois():
    global carry
    #faithBuff()
    renownCheck()
    experienceCheck()
    TotHea = Hea * 10
    while True:
        townQuestion = input("Where would you like to go?"
                    " You may go to the Alchemist (P),"
                    " the Blacksmith (W), the Armory (A), the Bank (B),"
                    " the Tavern (H), the Bounty Board (C), the Shrine (S),"
                    " the Market (M), the Trainer (T), the Menu,"
                    " the Incantation Store (I) or back Out (O). ").capitalize()
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
                alchemist()
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
            case "Trainer" | "Teacher" | "T":
                trainer()
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
            case "Bounty Board" | "Bounty" | "C":
                bounty()
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
