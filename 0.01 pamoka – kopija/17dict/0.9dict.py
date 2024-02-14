import os
print(os.getcwd())

def skaitomFaila():
    with open('09data.txt', encoding='utf-8')as f:
        txt = f.readlines()
        print(txt)

# vardas : [ ]
def suvestine():
    dalyviai = dict()
    duomenys = skaitomFaila()
    for elem in duomenys:
        vardas, taskai = elem.split()[:2]
        # print(f'{vardas} --->{taskai}')
        taskai = int(taskai)
        if vardas in dalyviai:
            dalyviai[vardas].append(taskai)
        else:
            dalyviai[vardas] = [taskai]
    return dalyviai

zaidejai = suvestine()
rezultatai = [(v, sum(t), max(t) for v, t in zaidejai.items)]
print(rezultatai)