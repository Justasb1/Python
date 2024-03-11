# patikrinti ar teigiamas sveikas skaicius ar bet kas
ivestis = input('Iveskit e simboliu seka...')
ivestis = ivestis.strip()#atsikratom tarpu gale ir priekyje
if ivestis.isdigit():
    print('Taip')
else:
    print('Ne')