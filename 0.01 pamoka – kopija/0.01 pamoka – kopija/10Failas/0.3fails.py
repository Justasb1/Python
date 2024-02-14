# w r a w+ r+
def sukurtiFaila(txt):
    with open('data3.txt', 'w+', encoding='utf-8') as f:
        f.write('5\n')
        f.write('8\n')
        f.seek(0)
        a = int(f.readline())
        b = int(f.readline())
        s = a + b
        f.write(txt)
        f.write(f'\n{a} + {b} = {s}')

for i in range(0, 4 ):
    sukurtiFaila(f'{i}bet kas')