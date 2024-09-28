# Métodos úteis para dicts
"""
len - quantas chaves você tem no seu dict
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existir
"""
pessoa = {
    'nome': "Felipe", #nome = chave / Felipe = valor
    'sobrenome': "Souza",
    'idade' : 17,
    'altura' : 1.8,
}

#len
print(len(pessoa)) # 4 chaves = nome, sobrenome, idade, altura
#! KEYS VALUES E ITEMS PODEM SER CONVERTIDOS PARA TUPLA OU LISTA PARA ITERAR(SELECIONAR) SEUS VALORES
#keys
print(pessoa.keys()) #dict_keys(['nome', 'sobrenome', 'idade', 'altura'])
#values 
print(pessoa.values()) #dict_values(['Felipe', 'Souza', 17, 1.8])
#items
print(pessoa.items()) #dict_items([('nome', 'Felipe'), ('sobrenome', 'Souza'), ('idade', 17)...])
#Exemplo for:
for chave,valor in pessoa.items():
    print(chave,valor) #nome, Felipe / sobrenome, Souza / idade, 17 / altura,1.8]

#setdefault
pessoa.setdefault('CPF',0)
print(pessoa["CPF"]) #0
