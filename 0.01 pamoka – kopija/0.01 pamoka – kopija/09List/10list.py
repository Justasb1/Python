#List Comprehension
a = [2, 4, 8, 4, 1, 8, 9]
#reikia naujo saraso, kuriame elementai pakelti kvadratu
kva = []
for i in a:
    kv = i * i
    kva.append(kv)
print(kva)

listCo =[i*i for i in a]
print(listCo)