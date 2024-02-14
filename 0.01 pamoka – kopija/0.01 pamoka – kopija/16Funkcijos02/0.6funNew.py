#filter
sar = [5, 8, 9, -1, 25, 8, 7, 9, 4, 6, 14, 19]
def arLyginis (sk):
    return sk % 2 == 0

print(list(filter(arLyginis, sar)))
nelyginiai=list(filter(lambda n: n % 2 !=0, sar))
print(nelyginiai)

cars = ['Ford', 'BMW', 'Volvo', 'Audi', 'KIA', 'Mercedes', 'Subaru', 'Honda', 'Suzuki', 'A']
print(max(cars))
didZodis = max(cars, key = lambda car: len(car))
print(didZodis)
help(max)