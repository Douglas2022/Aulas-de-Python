alunos = [
        {'nome':'Maria','idade':16,'matricula':11111},
        {'nome':'Ana','idade':17,'matricula':3333},
        {'nome':'Gabriel','idade':15,'matricula':44444}
    ]

def adicionarAlunos(name,age,registration,studants):
    aluno = {'nome':name,'idade':age,'matricula':registration}
    studants.append(aluno)

def deletarAluno(nome,alunos):
    indice = 0
    for aluno in alunos:
        if aluno['nome'] == nome:
            alunos.pop(indice)
            indice = indice + 1
            print(indice)

aluno = {'nome':'João','idade':17,'matricula':12345}
alunos.append(aluno)

adicionarAlunos('Caio',15,34521,alunos)
deletarAluno('Ana',alunos)
print(alunos)

for i in range(2):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade do aluno: '))
    matricula = int(input('Digite a matricula do aluno: '))
    adicionarAlunos(nome,idade,matricula,alunos)


print(alunos)