# 1. Sugeneruokite atsitiktini dvimatį masyvą A[n][m], kuriame yra 
# atsitiktiniai skaičiai iš intervalo [10; 30], o masyvo elementai  
# yra  atsitiktiniai skaičiai iš intervalo [-100;  100]. 
# 2. Išsaugokite šį masyvą byloje. 
# 3. Nustatykite, ar šiame masyve yra stulpeliai, kurių visi nariai yra neigiami. 
# Jei yra – sukurkite masyvą B[x], kuriame išsaugokite tų stulpelių numerius.

import random as r

rand_array_size_interval = (10, 30)
rand_element_interval = (-100, 100)

A = []
B = []

r.seed(1)

# Part 1
#n = r.randint(rand_array_size_interval[0], rand_array_size_interval[1])
#m = r.randint(rand_array_size_interval[0], rand_array_size_interval[1])

n = r.randint(*rand_array_size_interval)
m = r.randint(*rand_array_size_interval)
for _ in range(n):
    elems = []
    for _ in range(m):
        elem = r.randint(*rand_element_interval)
        elems.append(elem)
    A.append(elems)

# Check if generating correctly
print('Elements in A:')
print(A)

# Part 2
with open('./2d_Array.csv', 'w') as f:
    for row in A:
        str_columns_array = map(str, row)
        columns_str = ','.join(str_columns_array)  + '\n'
        f.writelines(columns_str)

# Part 3
trigger = []
for _ in range(m):
    trigger.append(False)

for row in A:
    for i, col in enumerate(row):
        # 0 can be +0 or -0
        if col > 0:
            trigger[i] = True

for i, trg in enumerate(trigger):
    if trg == False:
        B.append(i)

print('Elements in B:')
print(B)