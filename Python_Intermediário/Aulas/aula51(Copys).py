# Métodos úteis para dicts 2 
"""
copy - retorna uma shallow copy(cópia rasa) do dicionário
.deepcopy - retorna uma deep copy(cópia profunda) do dicionário - precisa da biblioteca import copy
"""

pessoa = {
    'nome': "Felipe", #nome = chave / Felipe = valor
    'sobrenome': "Souza",
    'idade' : 17,
    'altura' : 1.8,
}
#COPY
pessoa2 = pessoa #interliga os dois dicionários, se um for modificado o outro tambem será 

#SHALLOW COPY
pessoa3 = pessoa.copy() #apenas copia as informações, não relacionando os dois dicionários
#! QUANDO UMA CÓPIA DE UMA LISTA FOR FEITA, INDEPENDENTE DE SER SHALLOW OU DEEP
#! SE O VALOR DA LISTA FOR ALTERADO, A CÓPIA TAMBEém SERá ALTERADA E VICE-VERSA
#? Então use a biblioteca copy com o método .deepcopy(), as listas não estarão interligadas

