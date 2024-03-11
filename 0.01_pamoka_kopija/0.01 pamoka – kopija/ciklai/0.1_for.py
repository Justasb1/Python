txt = "Man labai patinka rytais anksit keltis ir eiti i mokykla"
kiekis = 0
for i in txt:
    if i ==' ':
        kiekis += 1 #kiekis = kiekis + 1
if kiekis!=0:
    kiekis += 1
print(f'sakinyje "{txt}" yra {kiekis} zodziu')