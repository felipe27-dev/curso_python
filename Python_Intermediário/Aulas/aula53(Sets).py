# Sets  = Conjuntos em Python
"""
Sets são mutáveis porém apenas aceitam tipos imutáveis em um valor interno
"""
#Criando um set

set1 = {1, 2, 3, 4} #set1 = {1,2,3,4} set com dados
set2 = set() #set vazio 
print(set1)
print(set2)

#@ Dicts e Sets são coisas diferentes, sets não precisam de chaves

# Sets são eficientes para remover valores duplicados
# de iteráveis.
s1 = {1,2,3,3,3,3,2,2,1,2,1,2}
print(s1) # {1, 2, 3}

# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;

#* s1 = {1,2,[1,2]}
print(s1) #Error

# - não tem índexes;

# - não garantem ordem;
s1 = set("Fleipe")
print(s1) # {'l', 'e', 'i', 'F', 'p'}

# - são iteráveis (for, in, not in)
s1 = {1,2,3,2,3,4,5,6,2}
for valor in s1:
    print(valor,end=" ")
print("\n",s1) # {1, 2, 3, 4, 5, 6}


