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
#Self Explanatory
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
#Self Explanatory
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
