#Try, except, else e finally

try:# Tenta executar o código abaixo
    #import joerge
    a = 27
    b = 0
    c = a/b
    print(c)
except ZeroDivisionError: #Caso encontra este erro em especifico executa o codigo abaixo
    print("Não é possivel dividir por zero")
except NameError: #Caso encontra este erro em especifico executa o codigo abaixo
   print("Variável não encontrada")
except (TypeError,IndexError): #Caso encontra qualquer um dos dois erros executa o codigo abaixo
    print("Erro de tipo ou index")
except Exception as error: #Caso encontra qualquer erro executa o codigo abaixo
    print("Erro:",error.__class__.__name__) #Mostra o erro que aconteceu
except Exception: #Caso encontra qualquer erro executa o codigo abaixo
    print("Erro desconhecido")
else: #Executa se o try der certo, ou seja não teve erro
    print("Executou o else")
finally: #Executa sempre com erro ou sem erro
    print("Executou o finally")
print("\nFim")