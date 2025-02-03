#Crie um programa em python que simule um sistema de biblioteca. P programa deve permitir que o usuário realize as seguintes operações:
# 1 - Cadastrar Livro: O usuário pode cadastrar um novo livro, informando o título, autor e quantidade de cópias disponíveis
# 2 - Verificar Disponibilidade: O usuário pode verificar se um lívro está disponível para empréstimo.
# 3 - Emprestar Livro: O usuário pode emprestar um livro reduzindo a quantidade de livros disponíveis
# 4 - Devolver Livro: O usuário pode devolver um livroi, aumentando a quantidade de livros disponíveis
# 5 - Listar Livros: O usuário pode visualizar todos os livros cadastrados na biblioteca.
# 6 - Sair: O usuário pode sair do sistema

listaLivros = [
                {'titulo':'Pequeno Prícipe','autor':'João','quantidade':5},
                {'titulo':'O diário de um banana','autor':'Maria','quantidade':4},
                {'titulo':'A maldição da moleira','autor':'Caio','quantidade':8},
                {'titulo':'a','autor':'Caio','quantidade':8}
            ]
def cadastrarlivro(nome,autor,qtde,listaLivros):
    livro = {'titulo': nome,'autor': autor,'qtde': qtde}
    listaLivros.append(livro)

def   disponibilidadeLivro(listaLivros,nome):
    for livro in listaLivros:
        if nome == livro['titulo']:
            return livro['quantidade']
        return 'Livro não encontrado'
    
def emprestarlivro(listaLivros,nome):
    for livro in listaLivros:
        if nome == livro['titulo']:
            livro['quantidade'] = livro['quantidade'] -1

def devolverlivro(listaLivros,nome):
    for livro in listaLivros:
        if nome == livro['titulo']:
            livro['quantidade'] = livro['quantidade'] +1





while True:
    opcao = input('1- Cadastrar\n 2- Verificar\n 3- Emprestar\n 4- Devover\n 5- Listar livros \n 6- Sair')

    if opcao == '6':
        print("Saindo do sistema!")
        break;
    
    elif opcao == '1':
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o autor do livro: ")
        qtde = input("Digite quantidade das copias livro: ")
        cadastrarlivro(nome,autor,qtde,listaLivros)
        print("O livro foi cadastrado com sucesso!")

    elif opcao == '2':
        nome = input("Digite o nome do livro:")
        print(disponibilidadeLivro(listaLivros,nome))

    elif opcao == '3':
        nome = input("Digite o nome do livro: ")
        emprestarlivro(listaLivros,nome)
        print(listaLivros)

    elif opcao == '4':
        nome = input("Digite o nome do livro: ")
        devolverlivro(listaLivros,nome)
        print(listaLivros)


    elif opcao == '5':
        for livro in listaLivros:
          print(f'Título: {livro['titulo']}, Quantidade: {livro['quantidade']}')





