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
