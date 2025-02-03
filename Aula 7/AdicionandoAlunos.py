# def adicionarAlunos(name,age,registation,studants):
#     aluno = {'nome': name,'idade': age,'matricula': registation}
#     studants.append(aluno)

# def deletarAluno(nome,alunos):
#     indice = 0
#     for aluno in alunos:
#         if aluno['nome'] == nome:
#             alunos.pop(indice)
#             indice = indice + 1
#             print(indice)
         
    
#     # Lista de dicionários

# alunos = [
#         {'nome':'Maria','idade':16,'matricula':11111},
#         {'nome':'Ana','idade':17,'matricula':3333},
#         {'nome':'Gabriel','idade':15,'matricula':44444}
#     ]
# aluno = {'nome':'João','idade':17,'matricula':12345}

# alunos.append(alunos)

# adicionarAlunos('Caio',17,3456,alunos)

# for i in range(2):
#     nome = input("Digite o nome do aluno: ")
#     idade = int(input("Digite a idade do aluno: "))
#     matricula = int(input("Digite a matricula do aluno: "))

#     print(alunos)

#Crie um programa em python que simule um sistema de biblioteca. P programa deve permitir que o usuário realize as seguintes operações:
# 1 - Cadastrar Livro: O usuário pode cadastrar um novo livro, informando o título, autor e quantidade de cópias disponíveis
# 2 - Verificar Disponibilidade: O usuário pode verificar se um lívro está disponível para empréstimo.
# 3 - Emprestar Livro: O usuário pode emprestar um livro reduzindo a quantidade de livros disponíveis
# 4 - Devolver Livro: O usuário pode devolver um livroi, aumentando a quantidade de livros disponíveis
# 5 - Listar Livros: O usuário pode visualizar todos os livros cadastrados na biblioteca.
# 6 - Sair: O usuário pode sair do sistema

def cadastraLivro(nome,autor,qtde,listaLivros):
    livro = {'titulo':nome,'autor':autor,'qtde':qtde}
    listaLivros = (livro)

def verifivarLivros(listaLivros,nome):
    for livro in listaLivros:
        if nome == livro['titulo']:
            return livro['qtde']
        return 'Livro não encontrado!'

def emprestarLivros(listaLivros,nome):
    for livro in listaLivros:
        if nome == livro['titulo']:
            return livro['qtde'] - 1
        

def devolverLivro(listaLivros,nome):
    for livro in listaLivros:
        if nome == livro['titulo']:
            return livro['qtde'] + 1
        
        



listaLivros = [
                {'titulo':'Pequeno Prícipe','autor':'João','quantidade':5},
                {'titulo':'O diário de um banana','autor':'Maria','quantidade':4},
                {'titulo':'A maldição da moleira','autor':'Caio','quantidade':8},
                {'titulo':'a','autor':'Caio','quantidade':8}
               ]

while True:
    opcao = input("1- cadadrastar\n 2- Verificar\n 3- Emprestar\n 4- Devolver\n 5- Listar\n 6- sar \n")
    if opcao == '6':
        print("Saindo do sitema!")
        break;

    elif opcao == '1':
        nome = input("Digite o nome do livro:\n")
        autor = input("Digite o nome do autor:\n")
        qtde = input("Digite a quantidade de cópias:\n")
        cadrastarLivro = input(nome,autor,qtde,listaLivros)

    elif opcao == '2':
         nome = input("Digite o nome do livro:\n")
         print("Verificar a disponibilidade do livro:\n ",listaLivros,nome)

    elif opcao -- '3':
        nome = input("Digite o nome do livro: ")
        emprestarLivros(listaLivros,nome)
        print(listaLivros)
     
    elif opcao == '4':
        nome = input('Digite o npme do livro: ')
        devolverLivro(listaLivros,nome)
        print(listaLivros)

    elif opcao == '5':
        for livro in listaLivros:
            print('livro':{livro['titulo']qtde:{livro['qtde']}})

         
    




         








