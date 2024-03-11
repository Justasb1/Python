#Kazkiek prekiu apskaiciuoti ju pvm 21



def pvm1(x1, x2=0, x3=0):
    return sum([x1, x2 , x3])*0.21
pvmDydis1 = pvm1(2.25, 18.25, 25.25)
print(pvmDydis1)

pvmDydis2 = pvm1(2.25, 18.25)
print(pvmDydis2)

def pvm2(*args):
    print(type(args))
    return sum(args)*0.21

pvmDydis3 = pvm2(2.25, 18.25, 15, 14, 25.47, 14, 47)
print(pvmDydis3) 