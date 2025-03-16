class Carro:
    def __init__(self,marca='',ano = 0,modelo = '',velocidade = ''):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.velocidade = velocidade

    def ligar():
        print('O carro está ligado!')
    def desligar():
        print('O carro está desligado')
    def acelerar(self):
        self.velocidade += 10
        if self.velocidade >= 10:
            self.velocidade -= 10
        else:
            print('O carro está parado!')

Carro1 = Carro('Fiat',2023,'Argo',20)
print(Carro1.velocidade)
Carro1.acelerar()

print(Carro1.velocidade)

Carro1.acelerar = 100
print(Carro1.velocidade)

print(Carro1.modelo)

Carro1.acelerar = 100
print(Carro1.velocidade)

Carro1.velocidade = -10



        
    
        
