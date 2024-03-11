sar1 = [4, 18, 29, 7, 9, 6, 14, 2]
sar2 = [5, 8, 9, -1, 25, 8, 7, 9]
# x + y kay x < y ir x - y kai x > y
def sumavimas(list1 , list2):
    list3 = []
    for i in range (len(list1)):
        if list1[i] < list2[i]:
            el = list[i] = list2[i]
        else:
            el = list1[i] - list2[i]
        list3.append(el)
        return list3
    
print(sumavimas(sar1, sar2))
    