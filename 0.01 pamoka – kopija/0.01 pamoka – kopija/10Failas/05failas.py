def ivedimas(txt):
    sk = int(input(txt + ' = '))
    return sk

def rasom(txt):
    with open('data5.txt', 'a', encoding='utf-8') as f:
        f.write(txt + '\n')


kiek = ivedimas('Kiek skaiciu norime ivesti')
rasom(f'Vartotojas ives {kiek} skaicius')
sum = 0
list1 = []
for i in range(1, kiek+1):
    sk = ivedimas(f'sk{1}')
    list.append(sk)
    rasom(f'sk{i} = {sk}')
rasom(f'skaiciu sima = {sum}')