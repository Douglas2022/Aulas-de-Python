import math
# numero1 = int(input('Digite um número: '))
# numero2 = int(input('Digite um número: '))
# soma = numero1 + numero2
# print('O resultado é de: ',soma)

# numero1 = int(input('Digite a primeira nota: '))
# numero2 = int(input('Digite a segunda nota: '))
# numero3 = int(input('Digite a terceira nota: '))
# numero4 = int(input('Digite a quarta nota: '))

# media = (numero1 + numero2 + numero3 + numero4)/4

# print('A media é de: ',media)

# metros = int(input('Digite um número: '))
# ctm = metros/ 100;

# print('O número convertido em metros é de: ',ctm)

# circuferencia = float(input('digite a circuferenca: '))
# raio = circuferencia /(2* math.pi)
# print(f'O raio é de: {raio: 2f}')

# base = int(input('Digite a base: '))
# altura = int(input('Digite a base: '))
# area = base * altura
# print('A area ´é de: ',area)

# n1 = int(input('Digite un numero: '))
# n2 = int(input('Digite un numero: '))
# n3 = int(input('Digite un numero: '))

# menor = min(n1,n2,n3)

# print(f'O menor numero é de:',menor)

# n1 = int(input('Digite un numero: '))
# n2 = int(input('Digite un numero: '))
# n3 = int(input('Digite un numero: '))
# n4 = int(input('Digite un numero: '))
# n5 = int(input('Digite un numero: '))

# maior = max(n1,n2,n3,n4,n5)


# n1 = int(input('Digite un numero: '))
# n2 = int(input('Digite un numero: '))
# n3 = int(input('Digite un numero: '))
# n4 = int(input('Digite un numero: '))
# n5 = int(input('Digite un numero: '))

# numeros = [n1,n2,n3,n4,n5]
# soma = sum(numeros)
# media = soma/len(numeros)


# print('Valor da some:',soma)
# print('Valor d1a media:',media)

# for i in range(1,51):
#     if i % 2 != 0:
#         print(i)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

inicio = min(n1,n2)
fim = max(n1,n2) +1

for i in range(inicio,fim):
    print(i,end=' ')