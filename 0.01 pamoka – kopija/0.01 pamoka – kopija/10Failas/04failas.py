def kuriam(failas, tekstas):
    with open(failas, 'w', encoding='utf-8')as f:
        f.write(tekstas)

for i in range(1,20):
    kuriam(f'labas\{i}file.txt', f'{i} byloje irasyta informacija')