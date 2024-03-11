def skaityti(): 
    with open ('11data.txt', 'r', encoding='utf-8') as f:
        eilutes = f.readlines()
        print(eilutes)
        duomenys = {}




skaityti()