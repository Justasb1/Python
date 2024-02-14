#ar laimingas
sk = int(input('sk=...'))
laimingas = (sk>=5 and sk<=10) or (sk<=15 and sk<=20)

if laimingas:
    print("Skaicius laimingas")
else:
    print('Skaicius Nelaimingas')