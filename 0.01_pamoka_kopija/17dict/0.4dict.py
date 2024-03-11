# greitai reikia suskaiciuoti visu prekiu suma :
prekes = {
    'Duona' : 1.25,
    'Vanduo' : 0.65,
    'Mesa' : 7.25,
    'Alus be alc' : 1.25,
    'Zuvis' : 8.14,
    'Saldainiai "Sostine"' : 16.25,
}
print(sum(prekes.values()))

# reikia funkcijos kur suvedi prekes varda ir automatiskai nuskaiciuoja suma nuo korteles : 

# def perkam():
#     suma = 0
#     while True:
#         vienaPreke = input('Ka perkame? ') #atspausdinti prekes kurios yra sarase
#         if vienaPreke == 'end': #kazkas patikrintu ar tokia preke yra tarkim ivedus = tra ta ta paraso, - kad tokios prekes nera
#             break
#         suma += prekes[vienaPreke]
#     return suma # ne tik suma, bet ir prekes sudetas i sarasa

def perkam ():
    suma = 0
    sarasas = []
    while True:
        vienaPreke = input(f'Prekių sąrašas: {str(list(prekes.keys()))[1:-1]} Ka perkame? ') #atspausdinti prekes, kurios yra sarase
        if vienaPreke == 'end': # kazkur patikrintu, ar tokia preke yra. Tarkim parasius tra ta ta, tokios prekes nera
            break
        elif vienaPreke in prekes.keys():
            suma  += prekes[vienaPreke]
            sarasas.append(vienaPreke)
        else:
            print('Tokios prekės nėra!')
       
    return f'Jūsų pirkinių sąrašas: {str(sarasas)[1:-1]}. Išleidote: {suma}' # ne tik sumą, bet ir prekes sudetas į sąrašą

print(perkam())