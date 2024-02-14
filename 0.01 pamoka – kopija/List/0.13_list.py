sar1 = [5, 8, -2.5, 4, -8, 4, -2, -5]
sar2 = [2.5, 4, 5, -5, 4, -4, 1, -1]
# Man reikia poru kurios tenkina tokia salyga sar1[i] + 2*sar[j] == 0
poros = []
for i in sar1:
    for j in sar2:
        if + 2*j == 0:
            poros.append([i,j])
print(poros)

sar0 = [(i , j) for i in sar1 for j in sar2 if i+2*j == 0 ]
print(sar0)