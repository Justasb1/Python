#penkiazenklis skaicius rasti jo skaitmenine suma
#12345 skaitmenu suma = 15
sk = int(input("Penkiazenklis sk..."))
x1 = sk // 10000 #12345 // 10000==> 1
x2 = sk // 1000 % 10  #12345 // 10000==> 12 % 10 ==> 2
x3 = sk // 100 % 10   #12345 // 10000==> 123 % 10 ==> 3
x4 = sk // 10 % 10    #12345 // 10000==> 1234 % 10 ==> 4
x5 = sk % 10            #12345 // 10000==> 5
suma = x1+x2+x3+x4+x5
print(f"skaiciaus {sk} skaitmenu suma = {suma}")