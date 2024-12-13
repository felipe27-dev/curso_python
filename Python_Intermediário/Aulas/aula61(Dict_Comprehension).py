pessoa = {
    'nome': "Felipe", 
    'sobrenome': "Souza",
    'idade' : 17,
    'altura' : 1.8,
}

nova_pessoa = {
    chave: valor.upper() if isinstance(valor,str) else valor
    for chave,valor in pessoa.items()
}

print(nova_pessoa)