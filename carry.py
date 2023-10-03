while carry == True:
    chance()
    carryOn = input("Would you like to carry on? ").capitalize()
    if carryOn == "No":
        print("You are returning to the city of Celkis.")
        townQuestion = input("Where would you like to go? You may go to the Alchemist (A), the Blacksmith (B) or the Market (M). ").capitalize()
        if townQuestion == "Market" or townQuestion == "M":
            print("Going to the Market")
            shop()
        elif townQuestion == "Blacksmith" or townQuestion == "B":
            print("Going to the Blacksmith")
            blacksmith()
        elif townQuestion == "Alchemist" or townQuestion == "A":
            print("Going to the Alchemist")
        carry = False
    elif carryOn == "Yes":
        print("You are resuming with your journey. ")
        
    else:
        print("That is not an option.")
