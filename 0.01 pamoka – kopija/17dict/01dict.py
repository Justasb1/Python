#Vardas tel.nr

komandaA = (Jonas = 15, Tadas = 18, Kestas = 22, Rimas = 19, Algis = 28)
            print(komandaA)
            tuscias = dict() #{}

prekes = {
    'Duona' : 1.25,
    'Vanduo' : 0.65,
    'Mesa' : 7.25,
    'Alus be alc' : 1.25,
    'Zuvis' : 8.14,
    'Saldainiai "Sostine"' : 16.25,
}

komandaA = dict.fromkeys(['Jonas', 'Petras', 'Stasys', 'ir t.t'],'Nezaide')
print(komandaA)

print(prekes['Saldainiai "Sostine"'])
# print(prekes['Traskuciai']) #klaida
ats = 'Deja tos prekes nera'
print(prekes.get('Vitaminai', ats))
print(prekes.get('Zuvis', ats))
prekes['Pienas'] = 1.56