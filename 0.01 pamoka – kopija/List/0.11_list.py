txt =['25, -12, 45, 87, 45, 87, -25, 45']
#gauti skaiciu sarasa

sk =[]
for i in txt.split(', '):
    el = int(i)
    sk.append(el)

listSk = [int(i) for i in txt.split(', ')]
print(listSk)
listskLyg = [int[i] for i in txt.split(', ') if int(i) % 2 == 0]