txt = 'Ieskom.Bet koks tekstas, tik cia nera to ko ieskom. Bet koks tekstas, tik cia nera to ko ieskom'
txt1 = 'Ieskom.Bet koks tekstas, tik cia nera to ko ieskom. Bet koks tekstas, tik cia nera to ko ieskom'

# sukurti sarasa, kuriame saugomi o raides indeksai
# 1. Ar reikia "priimt" A ? Reikia
# txtMazas = txt.lower()
# vieta_a = []
# for i in range(len(txt)):
#     if txt[i].lower() == 'a':
#       vieta_a.append(1)

# print(vieta_a)

print(txt.count('a'))
print(txt1.find('A'))
print(txt1.find('A', 15))