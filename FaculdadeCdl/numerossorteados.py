import random
Numeros = []

for i in range(1,100):
    Numeros.append(random.randint(1,1000))

Pares = 0
Impares = 0

for Numeros in Numeros:
    if Numeros %2 == 0:
        Pares += 1
    else:
        Impares += 1

Percentual_Pares = (Pares / 100) * 100
Percentual_Impares = (Impares / 100) * 100

print(f'Porcentagem de números Pares:{Percentual_Pares}%')
print(f'Porcentagem de números Impares:{Percentual_Impares}%')



                        

    
