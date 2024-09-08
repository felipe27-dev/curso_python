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

import os
import time
import random    
os.system('cls') or None
cont_recarreg = 0
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

while True:
    loop = True
    os.system('cls') or None
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
    print("Esse é o jogo da forca, o seu objetivo é adivinhar qual é a palavra escolhida.")
    print("1 - Frutas")
    print("2 - Escola")
    print("3 - Filmes")
    print("4 - Países")
    print("5 - Animais")
    print("6 - Aleatório")
    print("7 - Sair")
    opcao = (input("\nDigite o tema desejado:"))
    if opcao == "1":
        tema = Frutas
        palavra = random.choice(tema)
        tema = "Frutas"
    elif opcao == "2":
        tema = Escola
        palavra = random.choice(tema)
        tema = "Escola"
    elif opcao == "3":
        tema = Filmes
        palavra = random.choice(tema)
        tema = "Filmes"
    elif opcao == "4":
        tema = Países
        palavra = random.choice(tema)
        tema = "Países"
    elif opcao == "5":
        tema = Animais
        palavra = random.choice(tema)
        tema = "Animais"
    elif opcao == "6":
        tema = Aleatório
        palavra = random.choice(tema)
        tema = "Aleatório"
    elif opcao == "7":
        print("Saindo...")
        time.sleep(3)
        os.system('cls') or None
        exit()
    else:
        print("Opção inválida")
        time.sleep(3)
        continue
    tentativas = 0
    letras_acertadas = ""
    print(f"O tema é: {tema}")
    time.sleep(3)
    while loop == True:
        os.system('cls') or None
        print(f"\nO tema é: {tema}\n")
        print("\nPara chutar a palavra completa, digite 1\n")
        letra_digitada= input("\nDigite uma letra: ").lower() 
        if  letra_digitada == "1":
            chute = input("\nDigite a palavra completa: ").lower()
            if chute == palavra:
                os.system('cls') or None
                print(f"\nVocê descobriu!!!\nA palavra era '{palavra.capitalize()}'\nE você levou {tentativas} tentativas")
                time.sleep(4)
                break
            else:
                print("Palavra errada")
                time.sleep(2)
                chute = ''
                continue
        if len(letra_digitada) > 1 :
            print("Digite apenas uma letra")
            time.sleep(2)
            continue
        if letra_digitada in letras_acertadas:
            print("Esta letra já foi digitada")
            time.sleep(2)
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
                os.system('cls') or None
                print(f"\nVocê descobriu!!!\nA palavra era '{palavra.capitalize()}'\nE você levou {tentativas} tentativas")
                time.sleep(4)
                loop = False
                os.system('cls') or None
            if all(letra in letras_acertadas for letra in palavra):
                os.system('cls') or None
                print(f"\nVocê descobriu!!!\nA palavra era '{palavra.capitalize()}'\nE você levou {tentativas} tentativas")
                time.sleep(4)
                loop = False
                os.system('cls') or None
                
