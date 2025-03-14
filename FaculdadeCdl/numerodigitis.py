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



# def adivinhe():
#     numeroSecreto = random.randint(1,100)
#     tentativa=10
#     print('BEM-VINDO AO JOGO DE ADVINHAÇÃO: \n')
#     print('OBS: O numero é de 1 a 100: \n')

#     while tentativa > 0: 
#         palpite = int(input(f'Tentativas restantes {tentativa} .Qual o seu palpite?\nc'))
#         if palpite < numeroSecreto:
#             print('O número é maior\n')

#         elif palpite > numeroSecreto:
#             print('O número é menor\n')

#         else:
#             print(f'Voce acertou:{numeroSecreto}\n')
#             break

#         tentativa -= 1

#         if tentativa == 0:
#              print('Voce perdeu:{numeroSecreto}\n')

# adivinhe()

# import random
# def adivinha():
#     numeroSecreto = random.randint(1,100)
#     tentativas = 10
#     print('Bem-vindo ao jogo de advinhação!/n OBS: O numero é de 1 a 100 e suas tentativas são 10.')
#     while tentativas > 0:
#         palpite = int(input(f'Tentativas restantes {tentativas}. Qual é o seu palpite?\n'))
#         if palpite < numeroSecreto:
#             print('O numero é maior:')
#         elif palpite > numeroSecreto:
#             print('O numero é menor')
#         else:
#             print('Acertou{numeroSecreto}')
#             break
#         tentativas -= 1

#         if tentativas == 0:
#             print('Voce perdeu {numeroSecreto}')

# adivinha()
     
for i in range(1,11):
    print(f'10 x {i} = (10 * {i})')
    




