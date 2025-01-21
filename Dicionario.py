# listasdenome = ['Ana','Carlos','Caio','Davi']
# print(listasdenome[3])
# media = 0
# n1 = n2 = n3 = n4 = 0.0
# nome, idade = "Fabio",47

# print(type(media))
# x = 3
# y = 4
# print(not('y == x'))
produto = 'Iphone'
quantidade_estoque = 200

print("O produto",produto,"tem",quantidade_estoque,"unidade no estoque",sep=",")

import time
print("Contagem")
for i in range(5):
    print(5 - i)
    # print(5 - i, end="\r")
    time.sleep(1)
    print("Acabou")