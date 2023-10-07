classn = input("Pick a class ").capitalize()
def classv(className, message, StrG, AgiG, DexG, HeaG, PerG, ChaG, IntG, TotHeaG, Sclass, SpeciaAbi, SpecialAbiNum):
    global classn
    global Str
    global Agi
    global Dex
    global Hea
    global Per
    global Cha
    global Int
    global TotHea
    global name
    global bankedGold
    global SpeciaAbi
    global SpecialAbiNum
    if classn == className:
        print(message)
        Str = int(StrG)
        Agi = int(AgiG)
        Dex = int(DexG)
        Hea = int(HeaG)
        Per = int(PerG)
        Cha = int(ChaG)
        Int = int(IntG)
        TotHea = int(TotHeaG)
        if classn == Sclass:
            SpecialAbi = int(SpecialAbiNum)

classv("Knight", f"Welcome, knight {name}.", 10, 3, 8, 7, 4, 6, 5, 70, "0", "Pi", 0)
classv("Merchant", f"Welcome, merchant {name}.", 1, 8, 1, 3, 8, 10, 6, 30, "Merchant", bankedGold, 1000)
classv("Summoner", f"Welcome, summoner {name}.", 1, 4, 1, 2, 9, 2, 8, 20, "Summoner", summonNumber, 0)
