try:
    f = open('failas/data1V2.txt','w', encoding='UTF-8')
    f.write('Pirmas kartas su failu.....\n')
    f.write('ąčęėįšųūž\n')
    a = 656
    f.write(str(a))
    f.write(f'\nmano skaicius {a}')
finally:
    f.close()