# 1
# 1 2
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
n = int(input('n=...'))
for i in range(n):
    for j in range(1,n+1-i):
        print(j, end=(' . '))
    print()