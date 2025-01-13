notas = input('Digite sua notas: ')
notas = float
aulas = input('Quantidade de aulas: ')
aulas = int

if(notas >=7 and aulas >= 40):
    print('Aprovado!')
elif aulas <40:
    print('Reprovado por falta!')
else:
    print('Reprovado!')