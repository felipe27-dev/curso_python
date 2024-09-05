i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ""
frase = input("Digite uma frase: ")
letra_buscada = input("Digite a letra que quer buscar na frase anterior: ")
vezes_aparecidas = frase.lower().count(letra_buscada.lower())
print(f"A letra '{letra_buscada}' apareceu {vezes_aparecidas} vezes na frase:\n{frase}\n")