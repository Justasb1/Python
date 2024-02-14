duomSar = ['duom1.txt', 'duom2.txt', 'duom 3.txt', 'duom4.txt']   # <-- masyvas
duomKlaida = []
duomInfo = []

# for byla in duomSar:
#     f = open(byla, 'r')
#     duomInfo.append(f.read())

for byla in duomSar:
    try:
        with open(byla, 'r', Encoding='utf-8') as f:
            duomInfo.append(f.read())
    except Exception as ex:
        duomKlaida.append(byla)
        print(f'Failas {byla}. Klaida{ex}')
print(duomInfo)
print(duomInfo)