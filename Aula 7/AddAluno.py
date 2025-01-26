# def AdicionarAlunos(nome,notaportugues,notaMatematica,listaAlunos):
#     aluno = {'nome':nome,'portugues':notaportugues,'matematica':notaMatematica}
#     listaAlunos.append(aluno)
# def RemoverAlunos(nome,listaAlunos):
#     indice = 0
#     for aluno in listaAlunos:
#         if nome == aluno['nome']:
#             listaAlunos.pop(i)

#             i= i + 1

# def CalcularMedia(listaAlunos):
#     somaP = 0
#     somaM = 0

#     for aluno in listaAlunos:
#         somaP = somaP + aluno['potugues']
#         somaM = somaM + aluno['matematica']

#         media = somaP/len(listaAlunos)
#         media = somaM/len(listaAlunos)

#         print('A média de portugues foi de: {somaP}')
#         print('A média de matematica foi de: {somaM}')


# alunos = [
#     {'nome':'Luiz','portugues':10,'matematica':8},
#     {'nome':'Letica','portugues':10,'matematica':10},
#     {'nome':'André','portugues':6,'matematica':7}
# ]

# while True:
#     opcao = input('Digite uma opcao\n1 - Adicionar Aluno e notas\n2 - Remover Aluno\n3 - Calcular a média da turma\n4 - Sair\n')
   

#     if opcao == '4':
#         print('Sair')
#         break
#     elif opcao == '1':
#         nome = input('Digite o nome: ')
#         portugues = int(input('Digite a nota de portugues: '))
#         matematica = int(input('Digite a nota de mateatica: '))

#         AdicionarAlunos(nome,portugues,matematica,alunos)
#         print(alunos)

#     elif opcao == '2':
#         nome = input('Digite seu nome: ')
#         RemoverAlunos(nome,alunos)
#         print(alunos)

#     elif opcao == '3':
#         CalcularMedia(alunos)


def adicionarAluno(name,age,matric,studants):
    aluno = {'nome':name,'idade':age,'matricula':matric}
    studants.append(aluno)

# Deletar um aluno
def deletarAluno(nome,alunos):
    indice = 0
    for aluno in alunos:
        if aluno['nome'] == nome:
            alunos.pop(indice)
        indice = indice + 1
        print(indice)


# Lista de dicionários

alunos = [
        {'nome':'Maria','idade':16,'matricula':11111},
        {'nome':'Ana','idade':17,'matricula':3333},
        {'nome':'Gabriel','idade':15,'matricula':44444}
    ]
aluno = {'nome':'João','idade':17,'matricula':12345}

alunos.append(aluno)

adicionarAluno('Caio',15,12345,alunos)
deletarAluno('Ana',alunos)
print(alunos)

for i in range (2):
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do Aluno: '))
    matricula = int(input('digite a matrícula do aluno: '))
    adicionarAluno(nome,idade,matricula,alunos)

print(alunos)
        
                
  
    