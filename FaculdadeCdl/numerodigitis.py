# def Fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (Fibonacci(n -1)) + (Fibonacci(n - 2))
    
# termos = int(input('\nDigite um número inteiro positivo: \n'))

# for i in range(termos):
#     print(Fibonacci(i),end= ' ')


# for i in range(1,11):
#     print(f'10 x {i} = {10*i}')
    
# def contador(numero):
#     return len(str(numero))

# numero = int(input('Digite um número inteiro positivo:\n'))

# if numero < 0:
#     input(f'O numero {numero} tem {contador(numero)} digitos.')
# else:
#     input('Informe o numero inteiro: \n')

import random

def adivinhe():
    numeroSecreto = random.randint(1,100)
    tentativa=10
    print('BEM-VINDO AO JOGO DE ADVINHAÇÃO: \n')
    print('OBS: O numero é de 1 a 100: \n')

    while tentativa > 0: 
        palpite = int(input(f'Tentativas restantes {tentativa} .Qual o seu palpite?\n'))
        if palpite < numeroSecreto:
            print('O número é maior\n')

        elif palpite > numeroSecreto:
            print('O número é menor\n')

        else:
            print(f'Voce acertou:{numeroSecreto}\n')
            break

        tentativa -= 1

        if tentativa == 0:
             print('Voce perdeu:{numeroSecreto}\n')

adivinhe()
