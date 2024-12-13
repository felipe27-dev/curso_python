lista = [
    {'nome': 'Fleipe','sobrenome': 'Souza',},
    {'nome': 'Rebeca','sobrenome': 'Salles',},
    {'nome': 'Carol','sobrenome': 'Borges',},
    {'nome': 'Ivan','sobrenome': 'Alves',},
]

def exibir(lista):
    for item in lista:
        print(item,sep='\n')    
    print("\n")
l1 = sorted(lista, key=lambda item: item['sobrenome']),
#Nome da função / item: / Nome da chave (sobrenome) 
l2 = sorted(lista, key=lambda item: item['nome']),

exibir(l1)
exibir(l2)

