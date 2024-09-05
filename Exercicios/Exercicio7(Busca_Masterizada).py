import unicodedata
import os
import time
os.system('cls') or None
frase = ""
i = 0
while frase != "SAIR":
    cont_recarreg =0
    print("SE QUISER FINALIZAR, DIGITE 'SAIR'")
    frase = input("Digite uma frase: ")
    frase_modificada = unicodedata.normalize("NFD", frase)
    frase_modificada = frase_modificada.encode("ascii", "ignore")
    frase_modificada = frase_modificada.decode("utf-8")
    i = 0
    qtd_apareceu_mais_vezes = 0
    letra_apareceu_mais_vezes = ""
    while i < len(frase):
        letra_atual = frase_modificada[i]
        qtd_apareceu_mais_vezes_atual = frase_modificada.count(letra_atual)
        if letra_atual == " ":
            i += 1
            continue
        if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
            qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
            letra_apareceu_mais_vezes = letra_atual
        i += 1
    print(f"A letra que apareceu mais foi '{letra_apareceu_mais_vezes.upper()}' e apareceu {qtd_apareceu_mais_vezes} vezes na frase:\n{frase}\n")
    time.sleep(5)
    while cont_recarreg  < 3:
        time.sleep(0.05)
        os.system('cls') or None
        print("Recarregando.")
        time.sleep(0.5)
        os.system('cls') or None
        print("Recarregando..")
        time.sleep(0.5)
        os.system('cls') or None
        print("Recarregando...")
        time.sleep(0.5)
        os.system('cls') or None
        cont_recarreg += 1
    time.sleep(1)
    os.system('cls') or None
else:
    print("Código finalizado")