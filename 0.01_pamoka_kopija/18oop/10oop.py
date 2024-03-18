# @dekoratoriai
import time
def kiekLaiko(func):
    def pradziaPabaiga(*args, **kwargs):
        pradzia = time.time()
        rez = func(*args, **kwargs)
        pabaiga = time.time()
        print(f'Vykdymo laikos funkcijai "{func.__name__}" : {pabaiga-pradzia}sek.')
        return rez
    return pradziaPabaiga


@kiekLaiko
def MusuFunkcija(n):
    suma = 0
    for i in range(n):
        suma += i
    return suma

print(MusuFunkcija(1_000_000))

@kiekLaiko
def MusuFunkcija1(n, k):
    suma = 1
    for i in range(1, n):
        suma += i*k
    return suma

print(MusuFunkcija1(10_000, 5))

wow_wrapped = kiekLaiko(MusuFunkcija)
wow_wrapped(1_000_000)