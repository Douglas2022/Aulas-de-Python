# listasdenome = ['Ana','Carlos','Caio','Davi']
# print(listasdenome[3])
# media = 0
# n1 = n2 = n3 = n4 = 0.0
# nome, idade = "Fabio",47

# print(type(media))
# x = 3
# y = 4
# # print(not('y == x'))
# produto = 'Iphone'
# quantidade_estoque = 200

# print("O produto",produto,"tem",quantidade_estoque,"unidade no estoque",sep=",")

# import time
# print("Contagem")
# for i in range(5):
    
#     # print(5 - i, end="\r")
# #     print(5 - i, end="\r")
# #     time.sleep(1)
#     print("Acabou")

lista = list(range(5))
lista = list(range(1,6))
lista = list(range(1,10,2))
lista = list(range(5,0,-1))
print(lista)

import time 
for i in range(5,0,-1):
    print(i,end="\r")
    time.sleep(i)