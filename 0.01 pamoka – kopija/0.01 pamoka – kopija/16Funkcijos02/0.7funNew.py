#*args **kwargs

 #komandaA = (Algis = 20, Jonas = 17, Giedrius = 15, Tadas = 19, Stasys = 23)

# komandaA = {'Algis' : 20, 'Jonas' : 17, 'Giedrius' : 15, 'Tadas' : 19, 'Stasys' : 23}

def suma(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        print(f'Zaidejas {k} surinko {v} tasku')
        sum += v
    return sum
# komandaA