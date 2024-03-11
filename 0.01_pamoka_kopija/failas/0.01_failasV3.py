with open('failas/data1V3.txt','w', encoding='UTF-8') as f:
    f.write('Pirmas kartas su failu.....\n')
    f.write('ąčęėįšųūž\n')
    a = 656
    f.write(str(a))
    f.write(f'\nmano skaicius {a}')
print('Kita dalis')