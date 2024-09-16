#Validação do CPF
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
74682489070
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re 

while True:
#? Declaração de variáveis
    cpf = re.sub(r"[^0-9,.,-]","",input("Digite o CPF para verificá-lo: "))
    lista_cpf = []
    multiplicador = 10
    lista_cpf_modificada = []
    
#? Verificação de tamanho de CPF
    if len(cpf) < 11:
        print("Digite um CPF válido ")
        continue
    elif len(cpf) > 14:
        print("Digite um CPF válido e menor")
        continue
#? Verificação CPF repetido
    if cpf == str(cpf[0]*len(cpf)) :    
        print("Digite um CPF válido, sem repetições multíplas")
        continue
    else:
        break

#? Formatação do CPF
for indice,item in enumerate(cpf): #tratamento de itens da lista
    if item == "." or item == "-":
        continue
    
    lista_cpf.append(int(item))
del lista_cpf[9:11] #limpeza de itens da lista

#?Verificação do Primeiro Digíto
for indice,item in enumerate(lista_cpf):
    lista_cpf_modificada.append(item*multiplicador)
    multiplicador -= 1
verificador_1 = sum(lista_cpf_modificada)
verificador_1 *= 10
verificador_1 = verificador_1 % 11
verificador_1 = verificador_1  if verificador_1 <= 9 else 0

#?Preparação de variáveis para o Segundo Digíto
lista_cpf.append(verificador_1)
lista_cpf_modificada = []
multiplicador = 11

#?Verificação do Segundo Digíto
for indice,item in enumerate(lista_cpf):
    lista_cpf_modificada.append(item*multiplicador)
    multiplicador -= 1
verificador_2 = sum(lista_cpf_modificada)
verificador_2 *= 10
verificador_2 = verificador_2 % 11
verificador_2 = verificador_2  if verificador_2 <= 9 else 0

#? Limpeza para mostrar para o cliente
lista_cpf.append(verificador_2)
lista_cpf.insert(3,".")
lista_cpf.insert(7,".")
lista_cpf.insert(11,"-")
cpf_para_cliente = ""
for i,item in enumerate(lista_cpf):
    cpf_para_cliente += str(item)
    
#? Verificação de validez de CPF
if verificador_1 == int(cpf[-2]):
    if verificador_2 == int(cpf[-1]):
        print(f"O CPF digitado ({str(cpf_para_cliente)}) é válido")
    else:
        print("O CPF digitado não é válido")
else:
    print("O CPF digitado não é válido")

