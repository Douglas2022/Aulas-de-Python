idade = [18,22,25,30,50,80]
contador = 0
for idades in idade:
    if idades >= 18:
        contador = contador + 1
        print(f'Temos {contador} pessoas de idade')
