weapons = {
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

inventory = ["common axe"]
print(inventory)
gold = int(0)

def sell():
    global gold
    while True:
        print(f"You currently have {gold} gold.")
        print(inventory)
        sellWhich = input("What would you like to sell? ")
        if sellWhich in inventory:
            YN = input(f"Would you like to sell {sellWhich}? ").capitalize()
            if YN == "Yes":
                inventory.remove(sellWhich)
                gold = int(gold) + int(weapons[sellWhich])
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

sell()