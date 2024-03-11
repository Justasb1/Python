# atspausdinti visus isvesto skaiciaus daliklius
# 12 --> 1, 2, 3, 4, 6, 12
sk = int(input('sk = ...'))
kiek = 0
for i in range(1, sk+1):
    if sk % i == 0:
        kiek += 1
        print(i, end=(', '))
print(f'Ju yra {kiek}')
