pessoa = {
    'nome': 'Felipe',
    'sobrenome': 'Souza',
}
a,b = pessoa
print(a) #nome
print(b) #sobrenome

a,b = pessoa.values()
print(a) #Felipe
print(b) #Souza

a,b = pessoa.items()
print(a) #('nome', 'Felipe')
print(b) #('sobrenome', 'Souza')

(a1,a2),(b1,b2) = pessoa.items()
print(a1,a2) #nome Felipe
print(b1,b2) #sobrenome Souza

informacoes_pessoais = {
    'idade': 17,
    'altura': 1.8
}

usuario = {**pessoa,**informacoes_pessoais}
print(usuario) # {'nome': 'Felipe', 'sobrenome': 'Souza', 'idade': 17, 'altura': 1.8}

#Kwargs - Keyword Arguments
def mostra_argumentos_nomeados(*args,**kwargs):
    print(kwargs,"  " , args)
    
mostra_argumentos_nomeados(1,2,3,4,5, nome='Felipe', sobrenome='Souza')