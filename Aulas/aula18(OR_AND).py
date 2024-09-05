'''
OPERADOR LÓGICO OR
'''
entrada = input("Digite E para entrar ou S para Sair: ")
senha = input("Digite sua senha: ")

if (entrada == "E" or entrada == "e") and senha == "admin123":
    print("Você entrou")
else:
    print("Você saiu")