# Atspausdinti visus pirminius skaicius is intervalo nuo 2 iki sk
sk = int(input('sk = ...'))

for j in range(2, sk+1):
    pirminis = True
    for i in range(2, (j//2)+1):  
        if j % i == 0:          
            pirminis = False        
            break                    
    if pirminis :                
        print(j, end=', ')
