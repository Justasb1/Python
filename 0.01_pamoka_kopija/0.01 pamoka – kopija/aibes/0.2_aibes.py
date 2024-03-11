aibeA = {1, 2, 3, 4, 5}
aibeB = {1, 2, 3, 4, 5, 7, 8, 11}
aibeC = {}

#ar poaibis?
print(aibeA.issubset(aibeB))

print(aibeB.issubset(aibeA))

#Virsaibis
print(aibeA.issuperset(aibeA))
print(aibeA.issuperset(aibeB))

#ar visi skirtingi
print(aibeA.isdisjoint(aibeA))
print(aibeA.isdisjoint(aibeB))

#aibiu sajunga
aibiuSajunga = aibeA.union(aibeB)
print(aibiuSajunga)

#sankirta, sandauga bendri elementai
abiSankirta = aibeA.intersection(aibeB)
print(abiSankirta)

aibeD = {1, 2, 3, 8, 11, 12, 13}
#skirtumas
aibeSkirtumas1 = aibeA.difference(aibeB)
print(aibeSkirtumas1)
aibeSkirtumas2 = aibeB.difference(aibeB)
print(aibeSkirtumas2)

#atimami bendri elemntai paliekami visi kiti
aibeKazkas = aibeB.symmetric_difference(aibeD)
print(aibeKazkas)

#update
aibeA.update(aibeB)
print(aibeA)

#salinimas
aibeA.remove(1)
print(aibeA)
# aibeA.remove(100)
# print(aibeA)
aibeA.discard(1000)
print(aibeA)
aibeA.discard(2)
print(aibeA)

kazkas=aibeA.pop()
print(kazkas)
print(aibeA)

# aibeA.clear()
# print(aibeA)

del(aibeA)
print(aibeA)
