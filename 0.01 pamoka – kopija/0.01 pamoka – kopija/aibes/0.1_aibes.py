#set
aibeA = set()
print(type(aibeA))
aibeA.add(5)
print(aibeA)
aibeB = {}
print(type(aibeB))
aibeB = {1, 2, 5, 8, 7, 8, 7, 9, 1, 8, 5}
print(aibeB)
list1 = (1, 2, 5, 8, 7, 8, 7, 9, 1, 8, 5)
list2 = list(set(list1))
print(list2)