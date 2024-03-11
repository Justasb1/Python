#rez = 100 / sk 
#else
while True:    
    try:
        sk = int(input('Iveskite skaiciu...'))
        rez = 100 / sk
    except ValueError as ex:
        print(f'Blogai ivesti duomenys ...Kartokite...Klaida {ex}')
    except ZeroDivisionError:
        print(f'Dalyba is {sk} negalima. Klaida {ex}')
    else:
        print(f'Panasu, kad viskas gerai {rez}')
        break
print(f'Mums pavyko...{rez}')
     