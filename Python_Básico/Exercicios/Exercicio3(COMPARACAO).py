valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
if valor1 > valor2:
    print("O primeiro valor que é {} é maior que o segundo valor que é {}".format(valor1,valor2))
elif valor2 > valor1:
    print("O segundo valor que é {} é maior que o primeiro valor que é {}".format(valor2,valor1))
elif valor1 == valor2:
    print("O primeiro valor que é {} é igual ao segundo valor que é {}".format(valor1,valor2))