import math
def bascara(a,b,c):
    delta = b**2 - 4*a*c
    if delta >1 :
        x1=(- b + math.sqrt(delta)) / (2*a)
        x2=(- b - math.sqrt(delta)) / (2*a)
        return x1,x2
    elif delta == 0:
        x1 = -b/(2*a)
        return x1,
    else:
        parteReal = -b /(2 * a)
        parteimaginaria = math.sqrt(-delta) / (2 * a)
        return(parteReal + parteimaginaria * 1j,parteReal - parteimaginaria * 1j)
    
a = int(input('Digite o coeficiente de (A)\n'))   
b = int(input('Digite o coeficiente de (B)\n'))
c = int(input('Digite o coeficiente de (C)\n'))
   
result = bascara(a,b,c)
print(f'As raizes da equação são:{result} ')
   
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número è par: ')
else:
    print(f'O número è impar: ')


      





    
