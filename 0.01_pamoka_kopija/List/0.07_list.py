# Petriuko pazymiai, ivesti pazymius, rasti vidurki
kiek = int(input('Kiek petriukas turi pazymiu? '))
p=[]
i = 0
while i<kiek:
# for i in range(kiek):
    paz = int(input(f'Iveskite {i+1}- aji, pazymi.....'))
    # paz = int(input(f' p[{i}] = '))
    if 1<=paz<=10:
        p.append(paz)
        i += 1
    else:
        print('Blogas pazimys!!!!')
        # continue
print(f'Petriuko pazymiai {p}')

suma = sum(p)
vid = suma / len(p)
print(f'Vidurkis {vid}')