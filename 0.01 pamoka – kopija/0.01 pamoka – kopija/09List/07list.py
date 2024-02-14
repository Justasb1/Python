# Petriuko pazymiai, ivesti pazymius, rasti vidurki
kiek = int(input('Kiek Petriukas turi pazymiu? '))
p=[]
i = 0
geri = 0
blogi = 0
while i<kiek:
    paz= int(input(f'Įveskite {i+1}-ąjį pažymį....'))
    if 1<=paz<=10:
        p.append(paz)
        i += 1
        geri += 1
    else:
        print('Blogas pazymys!!!!!')
        blogi += 1
        

print(f'Pertriuko pazymiai {p}')


suma = sum(p)
vid = suma / len(p)
print(f'Vidurkis {vid}')