def adicionarNumero(lista,numero):
    lista.append(numero)
    print(f'numero{numero} adicionado')
def removerNumero(lista,numero):
 if numero in lista:
    lista.remove(numero)
    print(f'numero{numero} removido')
 else:
    print(f'Número{numero}não encontrado na lista')

def somarNumeros(lista):
   return sum(lista)
def numeroMaximo(lista):
   if lista:
        return max(lista)
   return None
def numeroMinimo(lista):
       if lista:
        return min(lista)
       return None
def menu():
   listaNumeros =[]
   while True:
        print('\nMenu de opcoes: ')
        print('\n1- Adicionar números: ')
        print('\n2- Remover números: ')
        print('\n3- Soma númeross: ')
        print('\n4- Número maxímo: ')
        print('\n4- Número minimo: ')
        print('\nSair ')

        escolha = input('Escolha uma opção')
        if escolha == '1':
           numero = int(input('Digite o número a ser acionado:'))
           adicionarNumero(listaNumeros,numero)
        elif escolha == '2':
            numero = int(input('Digite o número a ser removido:'))
            removerNumero(listaNumeros,numero)
        elif escolha == '3':
            print(f'Soma dos números:{somarNumeros(listaNumeros)}')
        elif escolha =='4':
            maximo = numeroMaximo(listaNumeros)
            if maximo is not None:
                print(f'numero maximo{numeroMaximo}')
            else:
                 print('A lista está vazia')

        elif escolha == '5':
            minimo = numeroMinimo(listaNumeros)
            if minimo is not None:
                print(f'Número minimo{minimo}')
            else:
                print('A lista está vaziq.')
        elif escolha == '6':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválido! Tente novamente')

            


    

        

        

     
   


            
            
           
       





