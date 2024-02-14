# Petriuko pazymiai, ivesti pazymius, rasti vidurki
# Turi mama, ir jei rodo tik teigiamus pazymius , vidurkis
# Turi teti, jam rodomi pazymiai 6 ir didesni , vidurkis 
# [2, 4, 8, 7, 3, 6, 2, 1, 4]
# [4, 8, 7, 6, 4] mamos
# [8, 7, 6] tecio

def naujas(list1, kriterijus):
    newList = []
    for i in list1:
        if i >= kriterijus:
            newList.append(i)
    return newList

kiek = int(input('Kiek Petriukas turi pazymiu? '))
p=[]
i = 0
while i<kiek:
    paz= int(input(f'Įveskite {i+1}-ąjį pažymį....'))
    if 1<=paz<=10:
        p.append(paz)
        i += 1
    else:
        print('Blogas pazymys!!!!!')

        

print(f'Pertriuko pazymiai {p}')





tetis = naujas(p, 6)
mama = naujas(p, 4)
senelis = naujas(p, 7)
print(tetis)
print(mama)
print(senelis)
suma = sum(p)
vid = suma / len(p)
print(f'Vidurkis {vid}')