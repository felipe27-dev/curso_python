#Fazendo normalmente
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

print("\n"*1) #Separador
#Fazendo List Comprehension
lista = [numero for numero in range(10)]
print(lista)

#Fazendo List Comprehension com if 
lista = ["Não vou mostrar o três" if numero == 3  else numero
         for numero in range(10)]
print(lista)

print("\n"*1) #Separador

#Mapeamento de Dados
lista_de_pessoas = [
    {'nome': 'Fleipe','sobrenome': 'Souza',},
    {'nome': 'Rebeca','sobrenome': 'Salles',},
    {'nome': 'Carol','sobrenome': 'Borges',},
    {'nome': 'Ivan','sobrenome': 'Alves',},
]
nova_lista_de_pessoas = [
    {**pessoa, 'sobrenome' : pessoa['sobrenome'] + " " + "Novo" }
    for pessoa in lista_de_pessoas
]
print(*nova_lista_de_pessoas, sep="\n")