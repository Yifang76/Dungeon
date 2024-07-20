gold, bankedGold = 0, 0

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
#Self Explanatory
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
#Self Explanatory
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
