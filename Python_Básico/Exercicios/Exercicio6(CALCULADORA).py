import os
import time
import pyautogui as pt

os.system('cls') or None
opcao = "0"
try:
    while opcao != "5":
        print("Fleipe's Calculadora")
        print("-"*20)
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        opcao = input("Digite a opção desejada: ")
        if opcao == "5":
            continue
        if opcao not in ["1","2","3","4","5"]:
            print("Digite uma opção válida!")
            time.sleep(2)
            os.system('cls') or None
            continue
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
        if opcao == "1":
            print(f"Operação selecionada: Adição")
            print(f"{n1} + {n2} = {n1+n2}")
            time.sleep(5)
            sair = input("Digite 'SAIR' para finalizar a calculadora ou\n"  
                        "Digite outra coisa para continuar: ")
            sair = sair.upper()
            if sair == "SAIR":
                pt.hotkey("shift","q")
            time.sleep(3)
            os.system('cls') or None
        elif opcao == "2":
            print(f"Operação selecionada: Subtração")
            print(f"{n1} - {n2} = {n1-n2}")
            time.sleep(5)
            sair = input("Digite 'SAIR' para finalizar a calculadora\n"  
                        "ou outra coisa para continuar: ")
            sair = sair.upper()
            if sair == "SAIR":
                pt.hotkey("shift","q")
            time.sleep(3)
            os.system('cls') or None
        elif opcao == "3":
            print(f"Operação selecionada: Multiplicação")
            print(f"{n1} x {n2} = {n1*n2}")
            time.sleep(5)
            sair = input("Digite 'SAIR' para finalizar a calculadora\n"  
                        "ou outra coisa para continuar: ")
            sair = sair.upper()
            if sair == "SAIR":
                pt.hotkey("shift","q")
            time.sleep(3)
            os.system('cls') or None
        elif opcao == "4":
            print(f"Operação selecionada: Divisão")
            print(f"{n1} ÷ {n2} = {n1/n2}")
            time.sleep(5)
            sair = input("Digite 'SAIR' para finalizar a calculadora\n"  
                        "ou outra coisa para continuar: ")
            sair = sair.upper()
            if sair == "SAIR":
                pt.hotkey("shift","q")
            time.sleep(3)
            os.system('cls') or None
    print("Programa Finalizado")
except:
    print("Digite algo válido")