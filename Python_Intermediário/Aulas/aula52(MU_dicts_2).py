# Métodos úteis para dicts 3
"""
get - obtem uma chave
pop - remove um item com uma chave especificada
popitem - remove o último item
update - atualiza um dicionário
"""

pessoa = {
    'nome': "Felipe", #nome = chave / Felipe = valor
    'sobrenome': "Souza",
    'idade' : 17,
    'altura' : 1.8,
}

#get
print(pessoa.get('nome','vazio')) #Felipe, se a chave não existir, retorna vazio

#pop
idade = pessoa.pop('idade') #Retira permanentemente valores de um dicionário e salvar em uma variável
print(pessoa) # {'nome': 'Felipe', 'sobrenome': 'Souza', 'altura': 1.8}
print(idade) # 17

#popitem
pessoa.popitem() #remove o último item do dicionário
print(pessoa) # {'nome': 'Felipe', 'sobrenome': 'Souza'}

#update
pessoa.update({'nome':'Jorge','idade': 18}) #atualiza valores e adiciona chaves e valores
print(pessoa) # {'nome': 'Jorge', 'sobrenome': 'Souza', 'idade': 18}