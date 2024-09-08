lista = ["Fleipe","Rebeca","Carol","Ivan"]

lista_enumerada = enumerate(lista)
print(next(lista_enumerada))

for item in lista_enumerada: # 0,Fleipe / 1,Rebeca / 2,Carol / 3,Ivan
    print(item)
#! Enumerate após ser utilizado elimina os itens no fim de um for por exemplo
for item in lista_enumerada: # Nada acontece pois não tem mais itens
    print(item)
    
#! OU SEJA NÃO USE ENUMERATE EM UMA VÁRIAVEL

for item in enumerate(lista): # 0,Fleipe / 1,Rebeca / 2,Carol / 3,Ivan
    print(item)

print(lista)

for indice,nome in enumerate(lista): #Está fazendo o desempacotamento da lista
    print('\t',indice)