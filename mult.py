def multiplayer():
    mult = input("Would you like to activate multiplayer? ").lower()
    match mult:
        case "yes" | "y":
            print("Multiplayer activated")
            party = input("Would you like to play )
        case "no" | "n":
            print("Multiplayer off ")
        case _:
            print("Not an option")
