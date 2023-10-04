def fight(noun, StrReq, DexReq, eStr, eDex):
    global TotHea
    global opon
    global carry
    commence = True
    while commence == True:
        opo = input(opon).capitalize()
        if opo == "Fight" or opo == "F":
            commence = False
            if n == noun:
                if Str >= StrReq and Dex >= DexReq:
                    TotHea == str(TotHea)
                    #print("You have "+TotHea+".")
                    #print("Minigame starting")
                    print("Rules: you are given a number between 1 and 10. If you get within 1 digit of the original number, you deal a fatal wound (which does the highest damage). Three digits difference leads to a body hit (which does mediocre damage) and finally anything over a three number difference will be a miss")
                    while TotHea > 0:
                        global eTotHea
                        print(eTotHea)
                        eTotHea = int(eTotHea)
                        if eTotHea > 0:
                            if TotHea > 0:
                                guess = randint(1,10)
                                print(guess)
                                pguess = int(input("What do you believe the number is? "))
                                if pguess == int(guess) or pguess == int(guess) - int(1) or pguess == int(guess) + int(1):
                                    td = int(Str) + int(Dex) + int(2)
                                    eTotHea = int(eTotHea) - int(td)
                                    td = str(td)
                                    eTotHea = str(eTotHea)
                                    print("Critical hit! You deal "+td+" against your enemy, leaving them with "+eTotHea+" health left.")
                                elif pguess == int(guess) - int(2) or pguess == int(guess) + int(2):
                                    td = int(Str) + int(Dex) - int(1)
                                    eTotHea = int(eTotHea) - int(td)
                                    td = str(td)
                                    eTotHea = str(eTotHea)
                                    print("Mediocre hit. You deal "+td+" against your enemy, leaving them with "+eTotHea+" health left.")
                                elif pguess <= int(guess) - int(3) or pguess >= int(guess) + int(3):
                                    td = int(Str) + int(Dex) - int(5) 
                                    eTotHea = int(eTotHea) - int(td)
                                    td = str(td)
                                    eTotHea = str(eTotHea)
                                    print("Weak hit. You deal "+td+" against your enemy, leaving them with "+eTotHea+" health left.")
                                        
                                eguess = randint(1,10)
                                if eguess == int(guess) or eguess == int(guess) - int(1) or eguess == int(guess) + int(1):
                                    etd = int(eStr) + int(eDex) + int(2)
                                    TotHea = int(TotHea) - int(etd)
                                    TotHea = str(TotHea)
                                    etd = str(etd)
                                    print("Critical hit! Your enemy deals "+etd+" to you, leaving you with "+TotHea+" left.")
                                elif eguess == int(guess) - int(2) or eguess == int(guess) + int(2):
                                    etd = int(eStr) + int(eDex) - int(1)
                                    TotHea = int(TotHea) - int(etd)
                                    TotHea = str(TotHea)
                                    etd = str(etd)
                                    print("Mediocre hit. Your enemy deals "+etd+" to you, leaving you with "+TotHea+" left.")
                                elif eguess <= int(guess) - int(3) or eguess >= int(guess) + int(3):
                                    etd = int(eStr) + int(eDex) - int(5)
                                    TotHea = int(TotHea) - int(etd)
                                    TotHea = str(TotHea)
                                    etd = str(etd)
                                    print("Weak hit. Your enemy deals "+etd+" to you, leaving you with "+TotHea+" left.")
                                TotHea = int(TotHea)
                                eTotHea = str(eTotHea)
                            else:
                                print("You died")
                                carry = False
                                return()


                        else:
                            if classn == "Summoner":
                                summon = randint(1,2)
                                if summon == 1:
                                    aq = input("You have defeated your enemy. Would you like to add this creature to your army?").capitalize()
                                    if "Yes" or "Y":
                                        print("You gain a new summon.")
                                        summonNumber = summonNumber + 1
                                        summons = summons.append(n)
                                    elif summonNumber >= maxSummon:
                                        TotHea = int(TotHea) - int(2)
                                        TotHea = str(TotHea)
                                        print("Attempting to gain a new minion, you discover that the toll is too much. You are left with "+TotHea+ "health.")
                                        if TotHea <= 0:
                                            print("You died.")
                                            carry = False
                                            return()
                                    else:
                                        print("The enemy dies")
                                else:
                                    print("The enemy dies")
                            else:
                                print("You have vanquished your enemy.")
                                lootdrop = randint(1,2)
                                if lootdrop == 1:
                                    itemDrop = randint(1,3)
                                    if itemDrop == 1:
                                        loot = ad + weapon
                                    elif itemDrop == 2:
                                        loot = resource
                                    else:
                                        loot = valuable
                                    print("You obtained a "+loot+".")
                                    global inventory
                                    inventory.append(loot)
                                    print(inventory)
                                else:
                                    print("You obtained nothing")
                                break
                    sys.exit()
                    
                    
                else:
                    nTotHea = int(TotHea) - randint(1,TotHea)
                    nTotHea = str(nTotHea)
                    TotHea = str(TotHea)
                    print("You aren't strong enough to wield your weapon effectively.")
                    print("You lost. HP falls from "+TotHea+" to "+nTotHea)
        elif opo == "Run" or opo == "R":
            retreat = randint(1+Agi,100)
            if retreat >= 50:
                print("You successfully fled, coward.")
                break
            else:
                print("You failed to escape.")
        else:
            print("That is not an option")
    #commence = True