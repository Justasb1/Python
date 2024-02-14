# Petriuko pazymiai, ivesti pazymius, rasti vidurki
# Turi mama, ir jei rodo tik teigiamus pazymius , vidurkis
# Turi teti, jam rodomi pazymiai 6 ir didesni , vidurkis 
# [2, 4, 8, 7, 3, 6, 2, 1, 4]
# [4, 8, 7, 6, 4] mamos
# [8, 7, 6] tecio
# adaptuoti programa, kad tiktu visai klasei
MAMA = 4
TATA = 6
#----------------kiekiu ivedimas----------------------
def gautiKieki (vardas):
    kiek = int(input(f'Kiek {vardas} turi pazymiu? '))
    return kiek
#-----------------------------------------------------
#----------------Pazymiu ivedimas---------------------
def gautiPazymius(vardas, kiek):
    paz=[]
    i = 0
    while i<kiek:
        p = int(input(f'Įveskite {vardas} {i+1}-ąjį pažymį....'))
        if 1<=p<=10:
            paz.append(p)
            i += 1
        else:
           print('Blogas pazymys!!!!!')
    return paz
#-----------------------------------------------------
#-------------------vidurkiuo skaiciavimas------------
def gautiVidurki(paz):
    if len(paz) == 0:
        return 0
    else:
        return sum(paz) / len(paz)
#-----------------------------------------------------
#-----------------tevams masyvas----------------------
def gautiTevuList (paz, kriterijus):
    newList = []
    for i in paz:
        if i >= kriterijus:
            newList.append(i)
    return newList
#-----------------------------------------------------
#-------------Rezultatas-----------------------------
def pateiktiRezultata(vardas):
    paz = gautiPazymius(vardas, gautiKieki(vardas))
    pazT = gautiTevuList(paz, TATA)
    pazM = gautiTevuList(paz, MAMA)
    print(f'{vardas} pazymiai: {paz}. Vidurkis {gautiVidurki(paz)}')  
    print(f'{vardas} pazymiai teciui: {pazT}. Vidurkis teciui {gautiVidurki(pazT)}')  
    print(f'{vardas} pazymiai mamai: {pazM}. Vidurkis mamai {gautiVidurki(pazM)}')  
#---------------------------------------------------
klase = ['Petras', 'Jonas', 'Ona', 'Domas', 'Tomas']
for i in klase:
    pateiktiRezultata(i)






