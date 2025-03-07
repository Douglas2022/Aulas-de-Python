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
    
def contador(numero):
    return len(str(numero))

numero = int(input('Digite um número inteiro positivo:\n'))

if numero < 0:
    input(f'O numero {numero} tem {contador(numero)} digitos.')
else:
    input('Informe o numero inteiro: \n')