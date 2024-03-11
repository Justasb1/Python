#suskaiciuoti visus Lt simbolius
txt = "ĄMan labai patinka Ęrytais anksit keltisįĘė ir eiti į mokyklą"
lt = ('ĄČĘĖĮŠŲŪŽąčęėįšųž')
kiekis = 0
for i in txt:
    if i in lt:
        kiekis += 1 #kiekis = kiekis + 1
    else:
        print(i, end=', ')
print(f'sakinyje "{txt}" yra {kiekis} LT simboliu')