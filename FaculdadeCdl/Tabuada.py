def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        print('Erro: divisão por zero')
        return None

def menu():
    print('OPERAÇÕES MATEMÁTICAS')   
    print('(1) - Soma')   
    print('(2) - Subtração')   
    print('(3) - Multiplicação')   
    print('(4) - Divisão')   
    print('(5) - Sair')   

def calculadora():
    while True:
        menu()
        try:
            escolha = int(input('Escolha a operação desejada! (1-5): '))

            if escolha == 5:
                print('Saindo da calculadora...')
                break

            if escolha in [1, 2, 3, 4]:
                numero1 = float(input('Digite o primeiro número: '))
                numero2 = float(input('Digite o segundo número: '))

                if escolha == 1:
                    print(f'{numero1} + {numero2} = {soma(numero1, numero2)}')
                elif escolha == 2:
                    print(f'{numero1} - {numero2} = {subtracao(numero1, numero2)}')
                elif escolha == 3:
                    print(f'{numero1} * {numero2} = {multiplicacao(numero1, numero2)}')
                elif escolha == 4:
                    resultado = divisao(numero1, numero2)
                    if resultado is not None:
                        print(f'{numero1} / {numero2} = {resultado}')
            else:
                print('Opção inválida. Escolha um número entre 1 e 5.')

        except ValueError:
            print('Entrada inválida. Digite um número inteiro entre 1 e 5.')