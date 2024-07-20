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
#Self Explanatory
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
