# Petriuko pazymiai, ivesti pazymius, rasti vidurki
# Turi mama, ir jei rodo tik teigiamus pazymius , vidurkis
# Turi teti, jam rodomi pazymiai 6 ir didesni , vidurkis
# [2, 4, 8, 7, 3, 6, 2, 1 ,4]
# [4, 8 ,7, 6, 4] mamos
# [8, 7, 6] tecio
kiek = int(input('Kiek petriukas turi pazymiu? '))
p=[]
i = 0
while i<kiek:
    paz = int(input(f'Iveskite {i+1}- aji, pazymi.....'))
    if 1<=paz<=10:
        p.append(paz)
        i += 1
    else:
        print('Blogas pazimys!!!!')



print(f'Petriuko pazymiai {p}')


def naujas(list1, kriterijus):
    newList = []
    for i in list1:
        if i >= kriterijus:
            newList.append(i)
    return newList



tetis = naujas(p, 6)
mama = naujas(p ,4)
senelis = naujas(p, 7)
print(tetis)
print(mama)
print(senelis)
suma = sum(p)
vid = suma / len(p)
print(f'Vidurkis {vid}')