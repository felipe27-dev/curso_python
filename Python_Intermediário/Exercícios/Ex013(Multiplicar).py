# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
# Crie uma função que fala se o número é par ou ímpar

import time
import os
#? Definição de funções
def multiplicar(*args):
    total = 1
    lista = list(args)
    listamultiplicar = []
    numero_atual = ""
    for item in lista:
        for indice in item:
            if indice == "," or indice == " ":
                listamultiplicar.append(int(numero_atual))
                numero_atual = ""
                continue
            numero_atual += str(indice)
        listamultiplicar.append(int(numero_atual))
        numero_atual = ""
        break
    for numero in listamultiplicar:
        total *= numero
    return total
def parouimpar(numero_verificado):
    verificacao =  (numero_verificado % 2) == 0
    if verificacao:
        mensagem = f"{numero_verificado} é um número par"
    else:
        mensagem = f"{numero_verificado} é um número ímpar"
    return mensagem
while True:
    os.system("cls") or None 
    print("1 - Multiplicar")
    print("2 - Verificar se é par ou ímpar\n")
    opcao = input("Digite sua opção desejada: ")
    if opcao == "1" :
        multiplicadores = list(input("Digite os números para multiplicar (separe por vírgulas): "))
        resultado = multiplicar(multiplicadores)
        print("A multiplicação é:",resultado)
        time.sleep(5)
        os.system("cls") or None 
    elif opcao == "2":
        numero_verificado = int(input("Digite um número: "))
        resultado = parouimpar(numero_verificado)
        print(resultado)
        time.sleep(5)
        os.system("cls") or None 
    else:
        print("Digite uma opção válida")
        time.sleep(3)
        os.system("cls") or None 