lista = ['a', 1, 'b', 2, True, 1.1, False, 1.2, ["banana",1], (1,2,3)]
lista_limpa = []

#IsInstance serve para verificar se um item pertence a um tipo de dado
#Por exemplo estou filtrando apenas os inteiros e reais
for item in lista:
    print(item,isinstance(item,(int, float)))
    
    if isinstance(item, (int, float)):
        
        if isinstance(item, bool):
            continue
        else:
            lista_limpa.append(item)
        
print("\n",lista_limpa)