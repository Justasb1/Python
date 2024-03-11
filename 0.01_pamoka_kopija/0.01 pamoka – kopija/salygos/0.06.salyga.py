#ivedamas pazimys
# -beg iki 0 negalimas balas
# 1 iki 3 blogas
# 4 iki 6 patenkinimas
# 7 ir 9 geras
# 10 puikus
# 11 iki +beg negalimas balas
sk = int(input('p='))

# if p<=0 :
#     print('negalimas balas')
# elif 1<=p<=3 :
#     print('blogas')
# elif 4<=p<=6 :
#     print('patenkinamas')
# elif 7<=p<=9 :
#     print('geras')
# elif p==10:
#     print('puikus')
# else:
#     print('negalimas balas')

# if sk <= 0:
#     print('Negalimas balas')
if 0<=sk<= 3:
    print('Blogas')
elif sk <= 6:
    print('Patenkinamas')
elif sk <= 9:
    print('Geras')
elif sk == 10:
    print('Puikus')
else :
     print('Negalimas balas')