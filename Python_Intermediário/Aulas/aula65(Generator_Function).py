#Generator Function são funções que pausam em um yield, ou seja, vão de 1 yield para outro
def generator(n=0, maximum=10):
    while True:
        yield n # Pausa a função e retorna o valor n
        n += 1
        if n >= maximum:
            return
    
gen = generator(n=0,maximum=10000)
#print(next(gen)) #recebe o valor 1 e pausa no primeiro yield
#print(next(gen)) #recebe o valor 2 e retorna onde pausou


for n in gen: #versão com for (simplificada)
    print(n)
    
#yield from (yield compartilhado entre generators)

def generator():
    yield 1
    yield 2
    yield 3
def generator2():
    yield 0
    yield from generator()
    yield 4
    
for n in generator2():
    print(n)