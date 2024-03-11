def sukurti():
    with open('data2.txt', 'w', encoding='utf-8') as f:
        f.write('25, 14, 23, 12, 74, -2\n')
        f.write('11, 14, 21, 15, 14\n')


def nuskaityti():
    with open('data2.txt', 'r', encoding='utf-8') as f:
        visas  = f.read()
    return visas

sukurti()
visas = nuskaityti()
print(type(visas))
print(visas)