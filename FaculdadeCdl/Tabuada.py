import random
numerofinal = int(input('Informe o número de 1 a 10:\n'))
soma = 0
numeroGerado = 0

while numeroGerado != numerofinal:
 numeroGerado = random.randint(1,10)
print(f"Numero gerado: {numeroGerado}")
soma += numeroGerado

print(f"Soma dos numeros gerados:{soma}")