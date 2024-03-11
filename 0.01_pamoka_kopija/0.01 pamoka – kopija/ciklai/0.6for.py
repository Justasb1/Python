#petriuka pazymiai Ivedamas keikis, atspausdinti vidurki
kiek = int(input('Kiek pas Petriuka pazymiu?'))
suma = 0
for i in range(kiek):
    p = int(input(f'Iveskite Petriuko {i+1}-aji pazymi....'))
    suma += p
vid = suma / kiek
print(f'Petriuko vidurkis {vid}')