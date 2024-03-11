# a : 154
# b : 12
def skaityk():
    with open('Python/0.01_pamoka_kopija/17dict/13data.txt', 'r', encoding='utf-8') as f:
        tekstas = f.read()
        # tekstas = tekstas.replace(' ','').replace('\n','')
        tekstas = tekstas.lower()
        simboliai = set(tekstas)
        dictSimboliai = dict.fromkeys(list(simboliai), 0)
        for raide in dictSimboliai.keys():
            dictSimboliai[raide] = tekstas.count(raide)
        return dictSimboliai
    
def spausdink():
    with open('Python/0.01_pamoka_kopija/17dict/13rez.txt', 'w', encoding='utf-8') as f:
        for raide, kiekis in rezultatas.items():
            f.write(f'Simboliu {raide} yra {kiekis}\n')

duomenys = skaityk()
duomenys = dict(sorted(duomenys.items(), key=lambda kv: -kv[1]))