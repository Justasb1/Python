txt = 'Mano batai buvo du, bet kazkas atsitiko - nerandu'
print(len(txt))
print(txt[len(txt)]-1)
print(txt[-1])
kiek_a = txt.count('a')
print(kiek_a)
kiekZodziu = txt.count('a')
print(kiek_a)
print(f'Zodziu yra {txt.count(" ")}')

print(txt.capitalize)

print(txt.upper()) # Taip / ne tAIP TAIP

print(txt.lower())

print(txt.islower())
print(txt.isupper())

print(txt.find('at'))
print(txt.find('at', 7, 40))

t = '123a456'
t1 = '123as;456'
t2 = 'asdf'
t3 = 'asdf;df'
print(t.isalnum())
print(t1.isalnum())
print(t.isalpha())
print(t2.isalpha())
print(t3.isalpha())
t4 = ' Labas '