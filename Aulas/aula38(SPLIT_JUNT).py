frase = "Felipe gosta de pão, e muita marmelada de goiaba"
lista_crua = frase.split(",") #divide a frase com base no que foi passado nos parenteses como divisor
lista_boa = []

for i,frase in enumerate(lista_crua): #separação de frases
    lista_boa.append(lista_crua[i].strip())
    #strip corta os espaços do inicio e final  #!Rstrip corta direita Lstrip esquerda
print(lista_boa) #['Felipe gosta de pão', 'e muita marmelada de goiaba']

#! Não altere valores de listas mutáveis, crie uma nova variável

frase_unida = " e não d".join(lista_boa) #join define um separador para cada iterável
print(frase_unida) #Felipe gosta de pão e não de muita marmelada de goiaba
