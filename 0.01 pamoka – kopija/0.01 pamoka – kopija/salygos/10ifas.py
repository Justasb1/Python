# ivedami du skaiciai a ir b jei jie vienodu zenklu juos sudauginti. Jei skirtingi - sudeti
# -2 -8 ; -2 8 ; 5 8 ; 5 -8
a=int(input("a=..."))
b=int(input("b=..."))
# if (a>0 and b>0) (a<0 and b>0):
if a*b>0:
    rez = a * b
else :
    rez = a + b
print(rez)