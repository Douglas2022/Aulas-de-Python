class Contabancaria():
    def __init__(self,nome,saldo = 0):
        self.nome = nome
        self.saldo = saldo
    def depositar(self,valor):
        self.saldo += valor
        print(f'O valor depositado com sucesso,seu salário novo é de:{self.saldo}')
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Voce não possui saldo suficiente.')
    def mostrarSaldo(self):
        print(f'Seu saldo é de: {self.saldo}')

conta = Contabancaria(1200,'João')
while True:
    opcao = input('1- Depositar\n2- Sacar\n3- Mostar Saldo\n4- Sair\n')
    if opcao == 'Sair':
        print('Saindo...')
        break
    elif opcao == '1':
        valor = float(input('Digite o valor depositado!'))
        conta.depositar(valor)
    elif opcao == '2':
        valor = float(input('Digite o valor a ser sacado:'))
        conta.sacar(valor)
    elif opcao == '3':
        conta.mostrarSaldo()
        
    
    


    
       
       



    
