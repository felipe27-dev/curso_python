#Estrutura de reptição
#While = enquanto / executa enquanto a condição dada for verdadeira
#FAZER UM WHILE COM QUE PRINTE O NÚMERO 1 DO LADO DO OUTRO
contador  = 0
while contador < 10:
    contador = contador + 1
    print(contador,end="")
    if contador == 5:
        break                
print("ACABOU")
