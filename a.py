import random
gold = 0
summonNumber = int(0)
Inventory = []
eTotHea = int(1)
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

classv("Knight", "Welcome, knight "+name+".", 10, 3, 8, 7, 4, 6, 5, 70, "0", "Pi", 0)
classv("Merchant", "Welcome, merchant "+name+".", 1, 8, 1, 3, 8, 10, 6, 30, "Merchant", "Banked Gold", 1000)
classv("Summoner", "Welcome, summoner "+name+".", 1, 4, 1, 2, 9, 2, 8, 20, "Summoner", summonNumber, 0)


items = {
"common axe": 10,
"rare axe": 50,
"mythical axe": 1000,
"legendary axe": 500000,
"common stick": 1,
"rare stick": 2,
"mythical stick": 3,
"legendary stick": 5,
"common sword": 20,
"rare sword": 60
}

itemsLength = len(items)

IVLoop = True

def buySlashSell(variable,number,statement,variabling,variablingtwo,numberw):
    global FirstItem
    global SecondItem
    global ThirdItem
    global four
    global five
    global six
    global gold
    global BoS
    global InvI
    gold = str(gold)
    print("You currently have "+gold+" gold.")
    gold = int(gold)
    if variable == number:
        price = 1
        print(price)
        buyorsell = int(input(statement))
        if variable == variabling:
            if buyorsell == numberw:
                if gold >= price:    
                    gold = gold - price
                    gold = str(gold)
                    print("You have "+gold+" gold left.")
                else:
                    print("You do not have enough gold.")
            else:
                print("Placeholder")
        elif variable == variablingtwo:
            if buyorsell == numberw:
                gold = int(2)
    gold = str(gold)
    print("You have "+gold+" gold left.")
    gold = int(gold)
                

def classSellandBuy(className, FirstItem, SecondItem, ThirdItem, four, five, six):
    global classn
    global itemList
    global itemListChosen
    global Inventory
    if classn == className:
        itemList = [FirstItem,SecondItem,ThirdItem,four,five,six]
        itemListChosen = random.choice(itemList)
def shop():
    global FirstItem
    global SecondItem
    global ThirdItem
    global four
    global five
    global six
    global BoS
    global number
    global IVLoop
    while IVLoop == True:
        BoS = input("Would you like to buy or sell? ").capitalize()
        if BoS == "Buy":
            IVLoop = False
            print(itemList)
            buy = int(input("What would you like to buy? "))
            buySlashSell(buy,1,"Would you like to buy the longsword for 60 gold?",1,2,1)
            buySlashSell(buy,2,"Would you like to buy the axe for 20 gold?",1,2,1)
            buySlashSell(buy,3,"Would you like to buy the spear for 20 gold?",1,2,1)
            buySlashSell(buy,4,"Would you like to buy the shortsword for 20 gold?",1,2,1)
            buySlashSell(buy,5,"Would you like to buy the katana for 20 gold?",1,2,1)
            buySlashSell(buy,6,"Would you like to buy the placeholder for 20 gold?",1,2,1)
            
        if BoS == "Sell":
            if not Inventory:
                print("You have nothing to sell.")
            else:
                IVLoop = False
                print(Inventory)
                sell = int(input("What would you like to sell? "))
                buySlashSell(sell,1,"Would you like to sell the "+str(next(zip(Inventory)))+"for 60 gold?","buy","sell",1)
                buySlashSell(sell,2,"Would you like to sell the axe for 20 gold?","buy","sell",1)
                buySlashSell(sell,3,"Would you like to sell the spear for 20 gold?","buy","sell",1)
                buySlashSell(sell,4,"Would you like to sell the shortsword for 20 gold?","buy","sell",1)
                buySlashSell(sell,5,"Would you like to sell the katana for 20 gold?","buy","sell",1)
                buySlashSell(sell,6,"Would you like to sell the placeholder for 20 gold?","buy","sell",1)


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
    adlist = ["common ","rare ","mythical ","legendary "]
    ad = random.choice(adlist)

    itemlist = ["axe","sword","stick"]
    item = random.choice(itemlist)

    nlist = ["imp","warlord","dictator"]
    n = random.choice(nlist)

    vlist = ["stands","looks","glares"]
    v = random.choice(vlist)


    palist = ["saunter","walk","run"]
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

    if n == "imp":
        eTotHea = int(25)
    if n == "warlord":
        eTotHea = int(100)
    if n == "dictator":
        eTotHea = int(75)

    global opo
    opo = int(input("As you "+pv+" down the path,"+t+"menacingly. What will you do? "))

def fight(noun, StrReq, DexReq, eStr, eDex):
    global TotHea
    global opo
    if opo == 1:
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
                        guess = random.randint(1,10)
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
                                
                        eguess = random.randint(1,10)
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
                            summon = random.randint(1,2)
                            if summon == 1:
                                aq = input("You have defeated our enemy. Would you like to add this creature to your army?").capitalize()
                                if "Yes" or "Y":
                                    print("You gain a new summon.")
                                    summonNumber = summonNumber + 1
                                elif summonNumber >= maxSummon:
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
                                loot = ad + item
                                print("You obtained a "+loot+".")
                                newItem = [loot,]
                                global Inventory
                                Inventory = Inventory + newItem
                                print(Inventory)
                            else:
                                print("You obtained nothing")
                            break
                
                
            else:
                nTotHea = int(TotHea) - random.randint(1,TotHea)
                nTotHea = str(nTotHea)
                TotHea = str(TotHea)
                print("You aren't strong enough to wield your weapon effectively.")
                print("You lost. HP falls from "+TotHea+" to "+nTotHea)
    elif opo == 2:
        retreat = random.randint(1+Agi,100)
        if retreat >= 50:
            print("You successfully fled, coward.")
        else:
            print("You failed to escape.")



def chance():
    chanceEn = random.randint(1,3)
    if chanceEn == 1:
        encounter()
        fight("imp",7, 5, 1, 1)
        fight("warlord",7, 5, 7, 9)
        fight("dictator",7, 5, 3, 3)
    elif chanceEn == 2:
        print("Placeholder")


carry = True
while carry == True:
    chance()
    carryOn = int(input("Would you like to carry on? "))
    if carryOn == 1:
        print("You are returning to the city of Celkis.")
        townQuestion = int(input("Where would you like to go? You may go to the Alchemist, the Blacksmith and the Market. "))
        if townQuestion == 3:
            print("Going to the Market")
            classSellandBuy("Knight", "Longsword","Axe","Spear","Shortsword","Katana","Placeholder")
            classSellandBuy("Merchant","Placeholder","Placeholder","Placeholder","Placeholder","Placeholder","Placeholder",)
            classSellandBuy("Summoner","Placeholder","Placeholder","Placeholder","Placeholder","Placeholder","Placeholder",)
            classSellandBuy("Placeholder","Placeholder","Placeholder","Placeholder","Placeholder","Placeholder","Placeholder",)
            shop()
        elif townQuestion == 2:
            print("Going to the Blacksmith")
        elif townQuestion == 1:
            print("Going to the Alchemist")
        carry = False
    elif carryOn == 2:
        print("You are resuming with your journey. ")
        
    else:
        print("That is not an option.")
