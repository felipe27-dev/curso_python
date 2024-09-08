lista = ["Felipe","Rebeca","Carol","Ivan"]
indice = 0
for nome in lista:
    print(indice,nome)
    indice += 1

#Jeito do prof(mais dificil e complexo):
lista = ["Felipe","Rebeca","Carol","Ivan"]
indices = range(len(lista))

for indice in indices:
    print(indice,lista[indice])
