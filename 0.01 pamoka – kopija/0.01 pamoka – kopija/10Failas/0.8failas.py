def skaitom():
    with open('0.8failas.txt', 'r') as f:
        txt = []
        while True:
            eil = f.readline()
            if eil:
                txt.append(eil)
            else:
                break
    return

visiData = skaitom()
print(visiData)
skaiciai = []
for eil in visiData:
    eilSk=[int(x) for x in eil.split(' ')]
    skaiciai.append(eilSk)

    print(skaiciai)
    print(skaiciai[0][2])