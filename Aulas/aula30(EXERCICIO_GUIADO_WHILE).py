
nome = input("Digite seu nome: ")
indice = 0 
while indice < len(nome):
    if nome[indice] == " ":
        print(f"O {indice+1}º caractere do seu nome é um espaço")
        indice += 1
        continue
    print(f"A {indice+1}º letra do seu nome é {nome[indice]}")
    indice += 1
print("Acabou")

nome = input("Digite seu nome: ")
indice = 0 

while indice < len(nome):
    print(f"*{nome[indice]}", end="")
    indice += 1
    
print("*\nAcabou")