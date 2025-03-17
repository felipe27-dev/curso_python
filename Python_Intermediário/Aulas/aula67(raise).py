#raise - lançando erros

def divisao(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        raise ZeroDivisionError("Nao é possivel dividir por zero")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
divisao(n1,n2)