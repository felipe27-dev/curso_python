import pprint
def p(valor):
    pprint.pprint(valor, sort_dicts=False,width=80)
#ajuda ao imprimir valores, melhor que o print
lista = [ 
    [(x,y) ]
    for x in range(3)
    for y in range(3)    
]


p(lista)