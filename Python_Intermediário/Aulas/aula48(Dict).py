#Estrutura do tipo par de chave e valor
#São consideradas comos os índices e podem feitos de tipos mutáveis: str,float,tuple
#usa os caracteres {} ou a classe dict para criar dicionários
#São mutáveis como listas
#EX:

pessoa = {
    'nome': "Felipe", #nome = chave / Felipe = valor
    'sobrenome': "Souza",
    'idade' : 17,
    'altura' : 1.8,
    'endereços': [
        {"rua": "Jose", "numero": 123},
        {"rua": "Carlos", "numero": 345},
    ],
}
print(pessoa,type(pessoa))

print(pessoa["nome"])