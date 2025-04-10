# notas = [8.0,5.5,1.4]
# media = (notas[0] + notas[1] + notas[2] ) /3
# notas = [8.0,5.5,1.4]

# notas = [8.0,5.5,1.4]
# for i in range(3):
#     print(notas[i])

# notas = []
# notas.append(float(input('\nDigite a primeira nota do aluno: ')))
# notas.append(float(input('\nDigite a segunda nota do aluno: ')))
# notas.append(float(input('\nDigite a terceira nota do aluno: ')))
# print(notas)


numeroAlunos = 3
media = 0
nome = []
notas = []

for i in range(numeroAlunos):
    nome.append(input('Digite o nome do aluno: '))
    notas.append(float(input(f'Informe a nota de ' +nome[i] + ': ')))
    media = media + notas[i]

media = media / notas
print('A média dos alunos é de ',media)

for i in range(numeroAlunos):
    if notas[i] > media:
        print('Parabéns',nome[i])

# num_alunos = 40
# nomes = []
# notas = []
# media = 0
# for i in range(num_alunos):
# nomes.append(input('Informe o nome do aluno: '))
# notas.append(float(input('Informe a nota de ' + nomes[i] + ': ')))
# media = media + notas[i]
# media = media / num_alunos
# print('A media da turma eh ', media)
# for i in range(num_alunos):
# if notas[i] > media:
# print('Parabens', nomes[i])