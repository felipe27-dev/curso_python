import pprint
def p(valor):
    pprint.pprint(valor, sort_dicts=False,width=80)
#ajuda ao imprimir valores, melhor que o print
    
lista = [
    numero #valor que vai ser inserido "mapeamento"
    for numero in range(10) #iteração entre valores, selecionando um por um
    if numero %2 == 0 #condição para o valor ser inserido "filtro"
    ]
p(lista)