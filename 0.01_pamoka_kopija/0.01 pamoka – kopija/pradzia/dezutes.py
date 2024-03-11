p = int(input("Kiek yra prekiu"))
d = int(input("Kiek telpa i didele deze"))
m = int(input("Kiek telpa i maza deze"))
dDez = p // d
tarpinislikutis = p % d 
mDez = tarpinislikutis // m
LikoPrekiu = tarpinislikutis % m #p % m
print(f"Mums reikes {dDez} dideliu deziu, {mDez}mazu deziu ir liks {LikoPrekiu} prekiu")