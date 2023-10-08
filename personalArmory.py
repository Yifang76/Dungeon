def armory():
    global hEqItem
    global cEqItem
    global lEqItem
    global gEqItem
    global bEqItem
    global rhEqItem
    global lhEqItem
    global whereEq
    WoR = input("Would you like to Equip (E) or Remove (R) equipment? ").capitalize()
    match WoR:
        case "Equip" | "E":
            whereEq = input("Which slot would you like to equip: Head (H), Chest (C), Gloves (G), Leggings (L), Boots (B),"
            "Right Hand (RH) or Left Hand (LH)? ").capitalize()
            match whereEq:
                case "Head" | "H":
                    equip(hEqItem, "wearing")
                case "Chest" | "C":
                    cEqItem = equip(cEqItem, "wearing")
                case "Gloves" | "G":
                    equip(gEqItem, "wearing")
                case "Leggings" | "L":
                    equip(lEqItem, "wearing")
                case "Boots" | "B":
                    equip(bEqItem, "wearing")
                case "Right" | "RH" | "Rh":
                    equip(rEqItem, "using")
                case "Left" | "LH" | "Lh":
                    equip(lEqItem, "using")
                case _:
                    print("That is not an option.")
        case "Remove" | "R":
            remove()
        case _:
            print("That is not an option.")

def equip(itemEquip, eVerb):
    global hEqItem
    global cEqItem
    global lEqItem
    global gEqItem
    global bEqItem
    global rhEqItem
    global lhEqItem
    if itemEquip is None:
        print(f"You currently have {inventory}.")
        whichEq = input("What would you like to equip? ")
        if whichEq in inventory:
            itemEquip = whichEq
            inventory.remove(whichEq)
            print(f"You are now {eVerb} {itemEquip}.")
        else:
            print(f"You already have {itemEquip} in this slot.")



def remove():
    whichRem = input("What would you like to remove? ")