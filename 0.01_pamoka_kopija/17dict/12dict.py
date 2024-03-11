def skaityk():
    with open('Python/0.01_pamoka_kopija/17dict/12data.txt', 'r', encoding='utf-8') as f:
        eilutes = f.readlines()
        duomenys = {}
        for eilute in eilutes:
            kirptiPerKab = eilute.split(', ')
            vardas = kirptiPerKab[0]
            pazTxt = kirptiPerKab[1].split(' ')
            duomenys[vardas] = [int(paz) for paz in pazTxt]
        return duomenys

def spausdinti(klase):
    with open('12rez.txt', 'a', encoding='utf-8') as f:
        for vardas, pazymiai in klase.items():
            f.write(f'{vardas:18} {str(pazymiai)[1:-1]}\n')

def triname():
    with open('12rez.txt', 'w', encoding='utf-8'):
        pass

triname()
klase = skaityk()
spausdinti(klase)

# Correct the sorted function
geriausi = dict(sorted(klase.items(), key=lambda item: sum(item[1]), reverse=True))
