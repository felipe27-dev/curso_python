"""
LISTAS = MUTÁVEIS
LISTAS = ARRAY
Suporta qualquer tipo de dado
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#         012345
#        -654321
string = "Fleipe"

nomes = ["Fleipe","Rebeca"]
lista = []
lista2 = [123,True,"Fleipe",1.2,lista]

print(bool(lista)) #False / Lista vazia é falso
print(bool(nomes)) #True / Lista preenchida é verdadeiro
print(type(nomes)) #class = list
print(lista2) #uma lista suporta qualquer tipo de dado

for nome in nomes: #separação de itens da lista
    print(nome) #Fleipe / Rebeca

lista2[1] = "Banana" #alteração de itens da lista através de fatiação
print(lista2) #[123,"Banana","Fleipe",1.2,]

#Metodos úteis	
