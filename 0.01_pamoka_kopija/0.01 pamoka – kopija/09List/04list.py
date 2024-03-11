m = [4, 8, 4, 52, 14, 14, 25, -25, 145]
# print(m*2)
m.append(-13)
print(m)
m.insert(1,-13)
print(m)
print(m.count(14))
did = max(m)
print(did)
maz = min(m)
print(maz)

def didelis(sar):
    # did = sar[0]
    # for i in range(1, len(sar)):
    #     if did < sar[i]:
    #         did = sar[i]
  
    return did
didziausias = didelis(m)
print(didziausias)

def mazius(sar):
    maz = sar[0]
    for i in sar:
        if maz > i:
            maz = i
    return maz