import sys 


iterable = ["Fleipe","banana","NÃO"]
iterator = iter(iterable)
lista = [numero for numero in range(100000)] #800984 de bytes na memória / A lista está completa na memória
generator = (numero for numero in range(100000))#200 bytes na memória
print(sys.getsizeof(generator))
print(sys.getsizeof(next(generator)))
print(sys.getsizeof(lista))