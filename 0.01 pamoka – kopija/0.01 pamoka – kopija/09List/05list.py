m = [4, 8, 4, 52, 14, 14, 25, -25, 145]
# m.sort()
print(m)
m.reverse()
print(m)
m.sort(reverse=True)

txt = ['a', 'ab,', 'b', 'aa', 'ac', 'cb', 'abc', 'ca']
txt.sort()
print(txt)
txt.sort(key=len, reverse=True)
print(txt)