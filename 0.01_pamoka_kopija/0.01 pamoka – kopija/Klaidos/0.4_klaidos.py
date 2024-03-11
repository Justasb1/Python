#rez = 100 / sk 
#else
veikia = True
while True:    
    try:
        sk = int(input('Iveskite skaiciu...'))
        rez = 100 / sk
        veikia = False
    # except Exception as ex:
    #     print(f'Blogai ivesti duomenys ...Kartokite...Klaida {ex}')
    except:
        print('Kazkas blogai')

    else:
        print(f'Panasu, kad viskas gerai {rez}')
    finally:
        print('Man dzin ar gerai ar blogai')

print(f'Mums pavyko...{rez}')
     