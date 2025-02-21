import random

Numeros = []


for i in range(100):
    Numeros.append(random.randint(1,1000))
    
    Pares = 0
    Impares = 0


    for numero in Numeros:
        if numero %2 == 0:
         Pares += 1
        else:
         Impares += 1


    Percentual_Pares = (Pares / 100) *100
    Percentual_Impares = (Impares / 100) *100

    print(f'Porcentagem de números Pares:{Percentual_Pares}%')
    print(f'Porcentagem de números Impares:{Percentual_Impares}%')
                        

    
