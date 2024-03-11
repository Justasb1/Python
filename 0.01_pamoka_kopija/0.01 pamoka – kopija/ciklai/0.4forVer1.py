#atspausdinit visus skaicius nuo 1 iki n. jei patenka skaicius 13 jo nespausdinti.
#atspausdinit visus skaicius nuo 1 iki n. jei patenka skaicius, kurio kvadratas = 169 jo nespausdina
n = int(input('n= '))
for i in range(-n, n+1):
    kv = i**2
    if kv == 169:
        continue
    print(i, end=(', '))
else:
    print('As vykdomas jei cikas nenutrauktas')
print('Kiti sakiniai')