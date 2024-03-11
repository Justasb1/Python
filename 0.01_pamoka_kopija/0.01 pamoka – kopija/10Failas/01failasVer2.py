try:
    f = open('data1Ver2.txt', 'w', encoding='utf-8')
    f.write('Pirmas kartas su failu....\n')
    f.write('ąČęĖįŠųūŽ\n')
    a = 656
    # labas
    f.write(str(a))
    f.write(f'\nmano skaičius {a}')
finally:
    f.close()