users = {
    'Tomuxxx':{'psw':'54/dsT', 'Admin':False, 'id':1451},
    'Algiukassss':{'psw':'as87/dsT', 'Admin':False, 'id':1452},
    'Deivisss':{'psw':'/$34*/+58as', 'Admin':False, 'id':1}
}
print(users['Tomuxxx'])
print(users['Tomuxxx']['psw'])
#noriu visu slaptazodziu sraso

print(users.items())
for user, info in users.items():#info in users liste vieno data pasirinkimas 
    print(f"Vartotojas {user}slaptazodis: {info['psw']}")