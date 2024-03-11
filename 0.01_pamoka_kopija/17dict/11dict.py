def skaityti():
    with open('Python/0.01_pamoka_kopija/17dict/11data.txt', 'r', encoding='utf-8') as f:
        eilutes = f.readlines()
        duomenys = {}
        for eilute in eilutes:
            vardas = eilute[:20].strip()
            likusiDalis = eilute[20:].strip()

            # Check if likusiDalis contains valid integers
            try:
                values = [int(i) for i in likusiDalis.split()]

                # Check if there are enough elements in the list
                if len(values) >= 3:
                    duomenys[vardas] = values
                else:
                    print(f"Skipping line: {eilute.strip()} - Not enough elements after split.")
            except ValueError:
                print(f"Skipping line: {eilute.strip()} - Invalid literal for int()")

    return duomenys

def rezultatas():
    duomenys = skaityti()
    for k, v in duomenys.items():
        duomenys[k].append(3*v[0] + 2*v[1] + v[2])
    return duomenys

def spausdinti(duomenys):
    with open ('Python/0.01_pamoka_kopija/17dict/11rez.txt', 'w', encoding='utf-8') as f:
        f.write('\n---------------------------------------------------------\n')
        f.write('|Vardas                  | Viso | 3 t. | 2 t. | 1 t.| Pr | \n')
        f.write('\n---------------------------------------------------------\n')
        for vardas, taskai in duomenys.items():
            f.write(f'|  {vardas:18}  |  {taskai[4]}  |  {taskai[0]}  |  {taskai[1]}  |  {taskai[2]}  |  {taskai[3]}\n')
        f.write('\n---------------------------------------------------------\n')

def triname():
    with open('Python/0.01_pamoka_kopija/17dict/11rez.txt', 'w', encoding='utf-8') as f:
        pass

triname()
komanda = rezultatas()
spausdinti(komanda)
komandaSurikiuotaRez = dict(sorted(komanda.items(), key = lambda kv:-kv[1][4]))
spausdinti(komandaSurikiuotaRez)
komandaPagalViska = dict(sorted(komanda.items(), key=lambda kv: (-kv[1][4], -kv[1][0], -kv[1][1], -kv[1][2], kv[1][3])))
spausdinti(komandaPagalViska)
