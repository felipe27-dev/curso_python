import random
cpf = ""
multiplicador = 10
cpf_modificada = ""
for i in range(9):
    cpf += str(random.randint(0,9))
#?Verificação do Primeiro Digíto
for indice,item in enumerate(cpf):
    cpf_modificada += str(int(item*multiplicador))
    multiplicador -= 1
verificador_1 = 0
for i,item in enumerate(cpf_modificada):
    digito_anterior = cpf_modificada[i]
    verificador_1 += int(digito_anterior)
verificador_1 *= 10
verificador_1 = verificador_1 % 11
verificador_1 = verificador_1  if verificador_1 <= 9 else 0
cpf += str(verificador_1)

#?Preparação de variáveis para o Segundo Digíto
cpf_modificada = ""
multiplicador = 11

#?Verificação do Segundo Digíto
for indice,item in enumerate(cpf):
    cpf_modificada += str(int(item*multiplicador))
    multiplicador -= 1
verificador_2 = 0
for i,item in enumerate(cpf_modificada):
    digito_anterior = cpf_modificada[i]
    verificador_2 += int(digito_anterior)
verificador_2 *= 10
verificador_2 = verificador_2 % 11
verificador_2 = verificador_2  if verificador_2 <= 9 else 0
cpf += str(verificador_2)

#? Formatação para o cliente
lista_cpf = []
for item in cpf:
    lista_cpf.append(str(item))
lista_cpf.insert(3,".")
lista_cpf.insert(7,".")
lista_cpf.insert(11,"-")

#? Limpeza para mostrar para o cliente
cpf_para_cliente = ""
for i,item in enumerate(lista_cpf):
    cpf_para_cliente += str(item)
print("O CPF gerado é :",cpf_para_cliente)

