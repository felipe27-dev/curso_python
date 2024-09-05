"""
Usuário digita o nome
usuário digita idade 

informo coisas para o usuário

-nome
-nome invertido
-nome com espaços ou não 
-número de letras do nome
-primeira letra do nome
-última letra do nome
-se nada for digitado 

"""
nome = (input("Digite o seu nome: "))
idade = (input("Digite a sua idade: "))
if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print("Seu nome contém espaços")
        numero_nome = len(nome)
        numero_nome = numero_nome - 1
        print(f"Seu nome tem {numero_nome} letras")
    else:
        print("Seu nome não contém espaços")
        numero_nome = len(nome)
        print(f"Seu nome tem {numero_nome} letras")
    if (nome[0] == " "):
        print(f"A primeira letra do seu nome é {nome[1]}")   
    else:
        print(f"A primeira letra do seu nome é {nome[0]}") 
    ult_letra = (len(nome) - 1)
    print(f"A última letra do seu nome é {nome[ult_letra]}")
else:  
    print("Desculpa,você deixou campos vazios")