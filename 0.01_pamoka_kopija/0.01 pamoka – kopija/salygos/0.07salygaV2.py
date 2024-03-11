# ivedami du skaiciai surasti did ir maz
a = int(input('a= '))
b = int(input('b= '))

def rezultatas(did, maz):
    print(f'did = {did}, maz = {maz}')
    at = did - maz
    print('at =',at)
    
if a>b:
    rezultatas(a, b)
     
elif a<b:
    rezultatas(b, a)
else:
    print('Skaiciai lygus')
    