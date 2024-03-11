import sys
duomSar = ['duom1.txt', 'duom2.txt', 'duom 3.txt', 'duom4.txt']   # <-- masyvas
duomKlaida = []
duomInfo = []


for byla in duomSar:
        try:
            with open(byla, 'r', encoding='utf-8') as f:
                duomInfo.append(f.read())
        except Exception as ex:
            duomKlaida.append(byla)
            sys.exit()
        finally:
            with open('logo.txt','a', encoding='utf-8') as f:
                for i in duomInfo:
                    f.write(f'{i}\n')
                f.write(str(duomKlaida))