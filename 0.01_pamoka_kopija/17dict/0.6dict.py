draugai = {
    'Zygis' : 37,
    'Jonas': 45,
    'Algis': 28,
    'Ona' : 38,
    'Greta' : 25,
    'Aidas' : 28
}
print(draugai)
print(sorted(draugai))
pagalVarda = dict(sorted(draugai.items()))
print(pagalVarda)
pagalAmziu = dict(sorted(draugai.items(), key = lambda kv:kv[1])) # kv[0], bet raudonuoja del skliausteliu - atspausdinti abeceles tvarka 
print(pagalAmziu)

