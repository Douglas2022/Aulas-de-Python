salarios = [1000,5000,7000,850]

# def aumentar_salario(salario):
    # return salarios  * 1.1
    # if salario > 3000:
    #     novoSalario = salario * 1.8
    # else:
    #     novoSalario = salario * 1.1
    #     return novoSalario
    
novoSalario = list(filter(lambda x : x > 2000,salarios))
print(novoSalario)
  