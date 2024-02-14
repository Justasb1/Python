# kad rezultatas butu isvedamas 5 + 8 = 13

def ivedimas(txt):
    sk = int(input(f'{txt}...'))
    return sk

def skaiciavimas():
    sk1 = ivedimas('Pirmas')
    sk2 = ivedimas()
    suma = sk1 + sk2
    return sk1, sk2, suma
    # suma = ivedimas("Pirmas") + ivedimas("Antras")
    # return suma

def isvedimas():
    a1, a2, rez = skaiciavimas()
    print(f'{a1} + {a2} = {rez}')
    rez = skaiciavimas()
    print(f'{rez[0]} + {rez[1]} = {rez[2]}')
    
    
    isvedimas()
