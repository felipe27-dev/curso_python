"""
Faça um jogo para o usuário adivinhar qual 
a palavra secreta. 
- Você vai propor uma palavra secreta 
qualquer e vai dar a possibilidade para 
o usuário digitar apenas uma letra. 
Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está 
na palavra secreta. 
- Se a letra digitada estiver na 
palavra secreta; exiba a letra; 
- Se a letra digitada não estiver 
na palavra secreta; exiba *. 
Faça a contagem de tentativas do seu 
usuário.
"""
"""
import unicodedata
import os
import time
os.system('cls') or None
palavra = "Paralelo".lower()
tentativas = 0
acertou = 0
antigas_letras = []
while acertou < len(palavra):
    letra_digitada = input("Digite uma letra: ")
    if len(letra_digitada) > 1 :
        print("Digite apenas uma letra")
        continue
    if letra_digitada.lower() in palavra:
            if letra_digitada in antigas_letras:
                if antigas_letras.count(letra_digitada.lower()) >= palavra.count(letra_digitada.lower()):
                    print("Essa letra está na palavra, mas já foi digitada o número máximo de vezes")  
                    continue 
                if palavra.count(letra_digitada.lower()) > 1:
                    print(letra_digitada)
                    acertou += 1
                    tentativas +=1
                    antigas_letras += letra_digitada
                    continue
                else:
                    print("Essa letra já foi digitada")  
                    continue
            print(letra_digitada)   
            acertou += 1
    else:
        if letra_digitada in antigas_letras:
                print("Essa letra já foi digitada")  
                continue
        else:
            print("*")
    tentativas +=1
    antigas_letras += letra_digitada
print(f"\nVocê descobriu!!!\nA palavra era '{palavra.capitalize()}'\nE você levou {tentativas} tentativas")
"""
import unicodedata
import os
import time
import random
import numpy
os.system('cls') or None
cont_recarreg = 0
Frutas = ["banana","melancia","pera","abacaxi","morango"]
Escola = ["lapis","aluno","borracha","professor","lapiseira"]
Filmes = ["coringa","vingadores","avatar","titanic","spirit"]
Países = ["brasil","dinamarca","espanha","australia","egito"]
Animais = ["dromedario","lagartixa","capivara","mosquito","urso"]
Aleatório = ["banana","melancia","pera","abacaxi","morango",\
    "lapis","aluno","borracha","professor","lapiseira",\
    "coringa","vingadores","avatar","titanic","spirit",\
    "brasil","dinamarca","espanha","australia","egito",\
    "dromedario","lagartixa","capivara","mosquito","urso"]
print("-"*50)
print(" "*17+"Jogo da Forca")
print("-"*50)
time.sleep(4)
while cont_recarreg  < 3:
    time.sleep(0.05)
    os.system('cls') or None
    print("Carregando.")
    time.sleep(0.5)
    os.system('cls') or None
    print("Carregando..")
    time.sleep(0.5)
    os.system('cls') or None
    print("Carregando...")
    time.sleep(0.5)
    os.system('cls') or None
    cont_recarreg += 1
time.sleep(1)
os.system('cls') or None
print("1 - Frutas")
print("2 - Escola")
print("3 - Filmes")
print("4 - Países")
print("5 - Animais")
print("6 - Aleatório")
opcao = int(input("\nDigite a opção desejada:"))
if opcao == 1:
    tema = Frutas
    palavra = random.choice(tema)
    tema = "Frutas"
elif opcao == 2:
    tema = Escola
    palavra = random.choice(tema)
    tema = "Escola"
elif opcao == 3:
    tema = Filmes
    palavra = random.choice(tema)
    tema = "Filmes"
elif opcao == 4:
    tema = Países
    palavra = random.choice(tema)
    tema = "Países"
elif opcao == 5:
    tema = Animais
    palavra = random.choice(tema)
    tema = "Animais"
elif opcao == 6:
    tema = Aleatório
    palavra = random.choice(tema)
    tema = "Aleatório"
else:
    print("Opção inválida")
    exit()
tentativas = 0
acertou = 0
letras_acertadas = ""
palavra_usuario = ""
print(f"O tema é: {tema}")
while True:
    letra_digitada = input("\nDigite uma letra: ")
    if len(letra_digitada) > 1 :
        print("Digite apenas uma letra")
        continue
    if letra_digitada in letras_acertadas:
        print("Esta letra já foi digitada")
        continue
    tentativas += 1
    print("Palavra: ",end="")
    for letra in palavra:
        if letra in letras_acertadas:
            print(letra,end="")
            continue
        if letra_digitada == letra:
            print(letra,end="")
            letras_acertadas += letra
        else:
            print("*",end="")
        if letras_acertadas == palavra:
            print(f"\nVocê descobriu!!!\nA palavra era '{palavra.capitalize()}'\nE você levou {tentativas} tentativas")
            quit()
        if all(letra in letras_acertadas for letra in palavra):
            print(f"\nParabens, a palavra era '{palavra.capitalize()}'\nE você levou {tentativas} tentativas")
            quit()
