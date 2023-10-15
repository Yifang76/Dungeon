from random import *
rarityValues = {
"common": "5",
"rare": "20",
"mythical": "50",
"legendary": "100",
}
inventory = ["common axe"]
factors = [" int", " faith", " strength", " dexterity", " health"]
factor = choice(factors)
q = input("")
f = q.split()
print(f)
if q in inventory:
    if f[0] in rarityValues:
        print(factor)
        print(f[0])
        tFactor = str(rarityValues[f[0]]) + factor
        print(f"{q} = {tFactor}.")
    else:
        print("NO")
else:
    print("NO")




