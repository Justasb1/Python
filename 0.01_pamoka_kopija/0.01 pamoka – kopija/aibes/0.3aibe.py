#3 didelius sarasus, reikia isrinkti uniklius, issaugoti kitmae sarase
import time
def fun (*args):
    sar = []
    for i in args:
        for j in i :
            if j not in sar:
                sar.append(j)
        return sar




sarA = list(range(10000))
sarB = list(range(2500, 16000, 2))
sarC = list(range(1000, 30000, 3))

pradzia1 = time.time()
fun(sarA, sarB, sarC)
pabaiga1 = time.time() - pradzia1

pradzia2 = time.time()
aibe1 = set(sarA)
sarUniAibe = list(aibe1.union(set(sarB), set(sarC)))
pabaiga2 =time.time()

print(pabaiga1)
print(pabaiga2)


