from random import *
rarityValues = {
"common": "5",
"rare": "20",
"mythical": "50",
"legendary": "100",
}
inventory = ["common axe"]
factors = ["int","faith","strength","dexterity","health"]
factor = choice(factors)
q = input("")
print(q.split)
if q.split() in inventory:
    print(factor)
    tFactor = rarityValues + factor
    print(tFactor)