#a ir c Rasti stataus trikampio plota s
import math
a = float(input("a....."))
c = float(input("a....."))
b = math.sqrt(math.pow(c,2) - a**2) #gali buti ir c*c, c**2, math.pow(c,2)
plotasS = (a*b)/2
print("Plotas lygus", plotasS)
