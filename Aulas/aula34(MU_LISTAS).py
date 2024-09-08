#Métodos  úteis: append, insert, pop, del, clear, extend, +
# Create, read, update, delete CRUD
lista = [10,20,30,40,50,60,70,80,90,100]
lista2 = ["Fleipe","Rebeca"]
print(lista)

del lista[0] #deleta elemento da lista
print(lista) #20,30,40,50,60,70,80,90,100

lista.append(110) #adiciona elemento na lista
print(lista) #20,30,40,50,60,70,80,90,100,110

lista.pop() #remove o último elemento da lista
print(lista) #20,30,40,50,60,70,80,90,100

lista.insert(5,65) #insere elemento em um lugar específico na lista
print(lista) #20,30,40,50,60,55,70,80,90,100

lista.clear() #remove todos os elementos da lista
print(lista) #[]
lista = [1,2,3]

lista3 = lista + lista2
print(lista3) #[1,2,3,"Fleipe","Rebeca"]

lista4 = lista.extend(lista2) #extende duas listas e modifica a lista original
print(lista4) #None
print(lista) #1,2,3,"Fleipe","Rebeca"]

lista2 = lista.copy() #cria uma cópia da lista independente da lista original
print(lista2) #[1,2,3,"Fleipe","Rebeca"]





