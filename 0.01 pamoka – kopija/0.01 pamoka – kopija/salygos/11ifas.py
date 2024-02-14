#sporto saka vertia 4 teisejai. bendras balas skaiciuojamas paimant dvieju viduriu vidurki
# 5 6 4 7 vid 5.5
t1 = float(input("t1 = "))
t2 = float(input("t2 = "))
t3= float(input("t3 = "))
t4 = float(input("t4 = "))
# did = max(t1 ,t2, t3, t4)
#kitas budas
# if t1>=t2 and t1>t3 and t1>=t4:
#     did = t1
# elif t2>=t3 and t2>=t4 :
#     did = t2
# elif t3>=t4:
#     did = t3
# else :
#     did = t4

# kitas budas
did = t1
if did<t2:
    did = t2
elif did<t3:
    did = t3
elif did<t4:
    did= t4

print(did)
maz = min(t1, t2, t3, t4)
vid = ((t1 + t2 + t3 + t4) - did - maz) / 2
print(vid)