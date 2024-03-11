# ivedami du skaiciai surasti did ir maz
a = int(input('a= '))
b = int(input('b= '))
if a>b:
    did = a
    maz = b
    print(f'did = {did}, maz = {maz}')
    at = did - maz
    print('at =',at) 
elif a<b:
    did = b
    maz = a
    print(f'did = {did}, maz = {maz}')
    at = did - maz
    print('at =',at)
else:
    print('Skaiciai lygus')
    
print(f'did = {did}, maz = {maz}') 