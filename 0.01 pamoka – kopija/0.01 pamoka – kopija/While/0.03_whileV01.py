#ivedamas bet koks skaicius. Apskaiciuokite jo skaitmenu suma...
# 125 suma = 8
def sumavimas(skaicius):
    suma = 0
    while skaicius > 0:
        x1 = sk % 10
        suma += x1
        skaicius //= 10
    return suma

sk = int(input('sk...'))
ats = sumavimas(sk)
print(f'Skaicius {sk} skaitmenu suma = {ats}')