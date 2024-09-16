#Range tem três estágios (start,stop,step)
#Range não depende do for, nem o for do range

numeros = range(10) #start = 0, stop = 10,step = 0
print(numeros,"\n") #range(0,10)

#? Com o For
for numero in numeros: #0 1 2 3 4 5 6 7 8 9 
    print(numero)

numeros = range(5,10)
print(numeros,"\n") #range(5,10) start = 5, stop = 10,step = 0

#? Com o For
for numero in numeros: # 5 6 7 8 9
    print(numero)

numeros = range(5,10,2) 
print(numeros,"\n") #range(5,10) start = 5, stop = 10,step = 2 (de quantos numeros eu pulo. Ex: 5,7,9)

#? Com o For
for numero in numeros:#5 7 9
    print(numero)