# Petriuko pazymiai, ivesti pazymius, rasti vidurki
kiek = int(input('Kiek petriukas turi pazymiu? '))
p=[]
for i in range(kiek):
    # paz = int(input(f'Iveskite {i+1}- aji, pazymi.....'))
    paz = int(input(f' p[{i}] = '))
    p.append(paz)
print(f'Petriuko pazymiai {p}')

suma = sum(p)
vid = suma / len(p)
print(f'Vidurkis {vid}')