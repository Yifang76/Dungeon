import random

name = input("Name, please ")

def noun(one, two, three):
    nlist = one, two, three
    n = random.choice(nlist)
    if n == "warlord" or n == "dictator":
        det = str("a")
    else:
        det = str("an")
    return n


noun("imp","warlord","dictator")

def verb(one, two, three):
    vlist = one, two, three
    v = random.choice(vlist)
    return v

verb("stands","looks","glares")

def playact(one, two, three):
    palist = one, two, three
    pv = random.choice(palist)
    return pv

playact("saunter","walk","run")

print("As you "+pv+" down the path, "+det+ " "+n+ " "+v+ " there menacingly. What will you do? ")





#return stops any instructions after it from working; it ends the specific area.
