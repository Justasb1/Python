m = [4, 8, 4, 52, 14, 14, 25, -25, 145]
d = m.copy()
print(id(d))
print(id(m))
# range(start, stop, step)
e = m[::]
f = m[1:3]
print(f)
e1 = m[0:len(m)]
kasAntras = m[0::2]
print(kasAntras)
noriu = m[1:3] + m[5:7]
print(noriu)
kopija = m + []
n = m[:5]
p = m[5:]
print(kopija)