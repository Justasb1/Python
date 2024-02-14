#rez = 100 / sk 

while True:    
    try:
        sk = int(input('Iveskite skaiciu...'))
        rez = 100 / sk
        break
    except ValueError as ex:
        print(f'Blogai ivesti duomenys ...Kartokite...Klaida {ex}')
    except ZeroDivisionError:
        print(f'Dalyba is {sk} negalima. Klaida {ex}')
print(f'Mums pavayko...{rez}')        