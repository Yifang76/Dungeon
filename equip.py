def equip(itemEquip, eVerb):
    global hEqItem
    global cEqItem
    global lEqItem
    global gEqItem
    global bEqItem
    global rEqItem
    global lEqItem  # You have 'lEqItem' twice in the global declarations; consider removing duplicates.

    if itemEquip is not None:
        print(f"You already have {itemEquip} in this slot.")
    else:
        print(f"You currently have {inventory}.")
        whichEq = input("What would you like to equip? ")
        if whichEq in inventory:
            itemEquip = whichEq  # Update the local variable
            inventory.remove(whichEq)
            print(f"You are now {eVerb} {itemEquip}.")
            # Update the global variable with the equipped item
            if eVerb == "equipping":
                hEqItem = itemEquip  # Assuming hEqItem corresponds to a slot
            # Update other global variables if needed

    return itemEquip  # Return the updated itemEquip

# Example usage:
inventory = ['Sword', 'Shield', 'Helmet']
hEqItem = None  # Initialize hEqItem
hEqItem = equip(hEqItem, "equipping")  # Call the function and update hEqItem
