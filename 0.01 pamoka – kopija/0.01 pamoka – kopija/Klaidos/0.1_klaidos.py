while True:    
    try:
        sk = int(input('Iveskite skaiciu...'))
        break
    except ValueError:
        print('Blogai ivesti duomenys... Kartokite...')
print(f'Mums pavayko...{sk}')        