
"""
!Usuário digita um número inteiro
?Fala se o número é par ou ímpar
?Caso o usuário não digitar um número INTEIRO fala isto
"""
try:
    numero = int(input("Digite um número inteiro: "))
    if (numero % 2) == 0 :
     print("O número é par")
    else:
       print("O número é impar ")
except:
   print("Isto não é um número inteiro")


"""
!Pergunta a hora do usúario
?Responde baseado no horário 
*Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

hora  = int(input("Digite a hora, por favor (hh): "))
if hora >= 0 and hora <= 11:
   print("Obrigado! E bom dia :) ")
elif hora >= 12 and hora <= 17:
   print("Obrigado! E boa tarde :) ")
elif hora >= 18 and hora <= 23:
   print("Obrigado! E boa noite :) ")
   
"""
!Peça o nome do usuário
?Classifique o nome
*4 a 5 letras - curto / 5 a 6 - normal / mais que 6 - muito grande
"""
nome = input("Digite o seu nome: ")
tamanho_nome = int(len(nome))
if tamanho_nome >= 1:
   if tamanho_nome < 5:
      print("Seu nome é curto")
   elif tamanho_nome >= 5 and tamanho_nome <= 6:
      print("Seu nome é normal")
   elif tamanho_nome> 6:
      print("Seu nome é muito grande")
else:
   print("Digite pelo menos 2 caracteres")