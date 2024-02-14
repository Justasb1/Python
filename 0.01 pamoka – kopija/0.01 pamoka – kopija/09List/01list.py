a = 5
t = True
m = [4, 8, 4, 52, 14, 14, 25, -25, 145]
print(m[0])
print(m[-1])
print(len(m))
print(m[len(m)-1])
user = ['Tomas', 18, 1.79, True, [5, 8, 7, 9, 6]]
print(user[2])
print(user[-1])
print(user[-1][1])
print(m)

n = m
print(n)
print(m)
m[0]=131313
print(id(n))
print(id(m))
m = 8
print(n)
print(m)
