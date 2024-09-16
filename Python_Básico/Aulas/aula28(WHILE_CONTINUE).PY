contador = 0

while contador < 100:
    contador += 1
    if contador >= 10 and contador<= 20:
        print(f"Não vou mostrar o valor de {contador}")
        continue
    
    if contador == 30:
        break   
    
    print(contador)
               
print("ACABOU")