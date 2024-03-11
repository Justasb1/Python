# Nustatyti ar ivestas skaicius pirminis ar sudetinis
# pirminis turi tik 2 daliklius save ir 1 :)
sk = int(input('sk = ...'))
kiek = 0
for i in range(2, (sk+1)//2):  #<---|\
    if sk % i == 0:            #<---| \
       pirminis = False        #<---|  -- Optimizavimas
    break                      #<---| /
if pirminis :                  #<---|/
    print(f'Skaicius {sk} priminis ')
else:
    print(f'Skaicius {sk} sudetinis ')

