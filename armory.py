inventory = ["Helmet", "Chestplate", "Gloves", "Leggings", "Boots", "Sword", "Shield"]
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

# Rest of the code remains the same


        
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
    whereRem = input("From which slot would you like to remove equipment? ").capitalize()
    if whereRem in equipped_items:
        item = equipped_items[whereRem]
        if item:
            inventory.append(item)
            equipped_items[whereRem] = None
            print(f"You have removed the {item} from {whereRem}.")
        else:
            print(f"There is no equipment in {whereRem} to remove.")
    else:
        print("Invalid slot selection.")

# Scenario:
# Let's say you have an inventory with the items mentioned above.
# Initially, all equipped items are set to None.
# You want to equip a Helmet on your Head and a Sword in your Right Hand.

print("Welcome to the Armory!")
while True:
    print(f"Inventory: {inventory}")
    print("Equipped:", ", ".join([f"{slot} - {item if item else 'Empty'}" for slot, item in equipped_items.items()]))
    armory_choice = input("Enter 'A' to access the Armory or 'Q' to quit: ").capitalize()

    if armory_choice == "Q":
        print("Thanks for visiting the Armory. Goodbye!")
        break
    elif armory_choice == "A":
        armory()
    else:
        print("Invalid choice. Please enter 'A' to access the Armory or 'Q' to quit.")
