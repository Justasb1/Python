# Petriuko pazymiai, ivesti pazymius, rasti vidurki
kiek = int(input('Kiek Petriukas turi pazymiu? '))
p=[]
for i in range(kiek):
    paz= int(input(f'Įveskite {i+1}-ąjį pažymį....'))
    # paz= int(input(f' p[{i}] = '))
    p.append(paz)
print(f'Pertriuko pazymiai {p}')


suma = sum(p)
vid = suma / len(p)
print(f'Vidurkis {vid}')