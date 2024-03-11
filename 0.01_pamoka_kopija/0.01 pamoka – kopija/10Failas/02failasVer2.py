def sukurti():
    with open('data2.txt', 'w', encoding='utf-8') as f:
        f.write('25, 14, 23, 12, 74, -2\n')
        f.write('11, 14, 21, 15, 14\n')


def nuskaityti():
    with open('data2.txt', 'r', encoding='utf-8') as f:
        eilute1  = f.readline()
        eilute2  = f.readline()
    return eilute1, eilute2

sukurti()
eilutes = nuskaityti()
# print(type(eilutes))
# print(eilutes)
sk = []
for i in eilutes:
    txt = []
    txt = i.split(', ')
    eilSk = [int(j) for j in txt]
    sk.append(eilSk)
print(sk)


