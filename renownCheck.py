def renownCheck():
    global renown
    renownToHonor = {
        -100 : "Villain",
        -50 : "Feared",
        0 : "Neutral",
        50 : "Loved",
        100 : "Hero",
    }
    if renown <= -100:
        honor = "Villain"
    elif renown <=-50 and renown > -100:
        honor = "Feared"
    elif renown == 0:
        honor = "Neutral"
    elif renown <= 50 and renown > 100:
        honor = "Loved"
    elif renown <= 100:
        honor = "Hero"
    else:
        honor = "Unidentified"