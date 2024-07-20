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
        "Murmur's Mask" : "Mask of Murmur the Maelstrom, a silent force is imbued within the mask's eyes. It is said that when worn, one can hear the sounds of the sea.",
        "Skrill's Spine" : "",
        "Fortress' Fangs" : "",
        #Need to edit to account for '

    }
    summonsDict = {
        "Frost Knight Theodore" : "",
        "Magma Blade Entil" : "",
    }
    q = input("What would you like to do. View Stats (S), View Inventory (I), View Journal (J),"
    " View Spells (T), View Summons (M), Use Item (U), Save/Load (C) or Check Level (L). ").capitalize()
    match q:
        case "View Stats" | "Stats" | "S":
            print(f"Without modifiers, you have:\nHealth: {trueTotHea}\nStrength: {trueStr}\nDexterity: {trueDex}\n"
            f"Perception: {truePer}\nCharisma: {trueCha}\nIntelligence: {trueInt} ")
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
        case "Save" | "Load" | "SL" | "C":
            save()
        case "Check Level" | "L":
            print(f"You are currently level {Level}.")
            print(f"You have {experience} EXP and you will need {experienceRequired-experience} EXP to level up.")
        case _:
            print("That is not an option.")
