#ivedamas bet koks skaicius. Apskaiciuokite jo skaitmenu suma...
# 125 suma = 8
sk = int(input('sk...'))
suma = 0
kopija = sk
while sk > 0:
    x1 = sk % 10
    suma += x1
    sk //= 10

print(f'Skaicius {kopija} skaitmenu suma = {suma}')