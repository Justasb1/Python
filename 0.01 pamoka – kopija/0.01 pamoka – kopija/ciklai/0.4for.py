#atspausdinit visus skaicius nuo 1 iki n. jei patenka skaicius 13 jo nespausdinti.
#atspausdinit visus skaicius nuo 1 iki n. jei patenka skaicius, kurio kvadratas = 169 jo nespausdina
n = int(input('n= '))
for i in range(1, n+1):
    print(i, end=(','))
    if i == 13:
        continue
    print('Tra ta ta', end=(', '))