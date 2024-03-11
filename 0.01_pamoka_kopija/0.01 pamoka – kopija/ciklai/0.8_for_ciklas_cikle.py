# parasyti programa kuri atspausdina daugybos lentele nuo 1 iki 10


for i in range(1, 11):
    print(f'Daugyba is {i}')
    for j in range(0, 11):
        rez = i * j
        print(f'{i} x {j} = {rez}')
    print()
    