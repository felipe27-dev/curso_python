def contas(x,y):
    
    somaconta = x+y
    subtracaoconta = x-y
    multipicacaoconta = x*y
    divisaoconta = x/y
    listaconta = [somaconta, subtracaoconta, multipicacaoconta, divisaoconta] #Retorna uma lista
    return listaconta #Retorna uma lista, mutavel

def contas2(x,y):
    
    somaconta = x+y
    subtracaoconta = x-y
    multipicacaoconta = x*y
    divisaoconta = x/y
    return somaconta, subtracaoconta, multipicacaoconta, divisaoconta #Retorna uma tupla, não mutavel
    
conta1 = contas(1,2)
conta2 = contas2(1,2)
print(conta1)
print(conta2)
