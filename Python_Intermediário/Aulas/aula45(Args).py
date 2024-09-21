#args = argumentos não nomeados
# - *args (empacotamento e desempacotamento)
import random
x,y, *resto = 1,2,3,4,5,6
print(f"{x=} {y=} {resto=}")

def soma(*args):
    total = 0
    for i in args:
        total += i
    return total

soma1 = soma(1,2,3,4,5) #passa uma quantidade ilimitada de argumentos, quantos tem
soma2 = soma(1,2,3,4,5,6,7,8,9,10,12,34314,3545,232)

print(soma1)
print(soma2)
print(sum([1,2,3,4,5,6,7,8,9,10,12,34314,3545,232]))