imc = float(input('Digite o IMC: '))
peso = float
altura = float
imc = peso/(altura * altura)

if imc <= 18.5:
    print('Abaixo do peso ')
elif imc >= 18.5 and imc < 24.9:
    print('Peso Normal')
elif imc >= 24 and imc < 29.9:
    print('Sobrepeso')
else:
    print('Acima do peso')