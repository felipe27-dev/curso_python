#Métodos Úteis para Sets
"""
add - adiciona um item
update - atualiza um set
clear - limpa o set
discard - remove um item
"""
s1 = set()
s1.add(1) #adiciona um valor único
print(s1)

s1.update({2,3,4}) #atualiza um set e pode adicionar vários valores
print(s1)

s1.discard(4) #remove um item que foi passado pelos parenteses
print(s1)

s1.clear() #limpa o set
print(s1)

print("-"*20)
#Operadores úteis
s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1 | s2 #uniao entre sets, mas pode usar o s3 = s1.union(s2)
print(s3) #{1,2,3,4,5}

s3 = s1 & s2 #interseccao entre sets, mas pode usar o s3 = s1.intersection(s2)
print(s3) #{3}

s3 = s1 - s2 #diferenca entre sets, mas pode usar o s3 = s1.difference(s2), mostra os que só tem no s1
print(s3) #{1,2}

s3 = s1 ^ s2 #diferenca simétrica entre sets, mas pode usar o s3 = s1.symmetric_difference(s2) 
#mostra os que só tem no s1 ou no s2
print(s3) #{1,2,4,5}