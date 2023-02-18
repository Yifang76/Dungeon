import random

name = input("Name, please ")

nlist = "imp","warlord","dictator"
n = random.choice(nlist)
if n == "warlord" or n == "dictator":
    det = str("a")
else:
    det = str("an")

vlist = "stands","looks","glares"
v = random.choice(vlist)


palist = "saunter","walk","run"
pv = random.choice(palist)

print("As you "+pv+" down the path, "+det+ " "+n+ " "+v+ " there menacingly. What will you do? ")





#return stops any instructions after it from working; it ends the specific area.
