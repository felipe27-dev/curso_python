import os
import time
import random    
os.system('cls') or None
print("-"*90)
print(" "*35+"Lista de compras")
print("-"*90)
time.sleep(4)
lista_de_compras = []
try:
    while True:
        os.system('cls') or None
        print("Lista de compras")
        print("1 - Inserir itens")
        print("2 - Apagar")
        print("3 - Listar")
        print("4 - Fechar")
        opcao_lista = input("Selecione uma opção: ")
        if opcao_lista == "1":
            os.system('cls') or None
            item_compra = input("Insira o item desejado: ")
            quant_bool = input("Deseja inserir quantidade, [S]im ou [N]ão: ").upper()
            if quant_bool == "S":
                os.system('cls') or None
                print("Item que será adicionado:",item_compra)
                print("1 - Unidade")
                print("2 - Gramas ou Quilogramas")
                print("3 - Mililitros ou Litros")
                print("4 - Pacotes")
                print("5 - Não quero colocar medida")
                opcao_quant = input("\nQual a medida do item: ")
                if opcao_quant == "1":
                    os.system('cls') or None
                    print("Item que será adicionado:",item_compra)
                    quantidade_item = int(input("\nQuantas unidades são: "))
                    item_compra = str(quantidade_item) +" unidades de " + item_compra
                    lista_de_compras.append(item_compra)
                    print(item_compra,"foi adicionado")
                    time.sleep(2)
                    continue
                if opcao_quant == "2":
                    os.system('cls') or None
                    print("Item que será adicionado:",item_compra)
                    print("Caso seja quilogramas, digite em gramas e faremos a conversão")
                    quantidade_item = int(input("\nQuantas gramas são: "))
                    if quantidade_item >= 1000:
                        quantidade_item = quantidade_item/1000
                        item_compra = str(quantidade_item) +"kg de " + item_compra
                        lista_de_compras.append(item_compra)
                        print(item_compra,"foi adicionado")
                        time.sleep(2)
                    item_compra = str(quantidade_item) +"g de " + item_compra
                    lista_de_compras.append(item_compra)
                    print(item_compra,"foi adicionado")
                    time.sleep(2)
                    continue
                if opcao_quant == "3":
                    os.system('cls') or None
                    print("Item que será adicionado:",item_compra)
                    print("Caso seja litros, digite em mililitros e faremos a conversão")
                    quantidade_item = int(input("\nQuantos mililitros são: "))
                    if quantidade_item >= 1000:
                        quantidade_item = quantidade_item/1000
                        item_compra = str(quantidade_item) +"L de " + item_compra
                        lista_de_compras.append(item_compra)
                        print(item_compra,"foi adicionado")
                        time.sleep(2)
                        continue
                    item_compra = str(quantidade_item) +"ml de " + item_compra
                    lista_de_compras.append(item_compra)
                    print(item_compra,"foi adicionado")
                    time.sleep(2)
                    continue
                if opcao_quant == "4":
                    os.system('cls') or None
                    print("Item que será adicionado:",item_compra)
                    quantidade_item = int(input("\nQuantos pacotes são: "))
                    item_compra = str(quantidade_item) +" pacotes de "+ item_compra
                    lista_de_compras.append(item_compra)
                    print(item_compra,"foi adicionado")
                    time.sleep(2)
                    continue
                if opcao_quant == "5":
                    continue  
                else:
                    print("Digite uma opção válida")
                    time.sleep(2)
                    continue
            lista_de_compras.append(item_compra)
            print(item_compra,"foi adicionado")
            time.sleep(2)
            continue
        if opcao_lista == "2":
            if lista_de_compras == []:
                print("\nNão há nenhum item para deletar")
                time.sleep(2)
                continue
            os.system('cls') or None
            print("Esta é sua lista")
            for indice,item in enumerate(lista_de_compras):
                print(indice+1,"-",item)
            deletar_item = int(input("\nInsira o número do item para deletar: "))
            del lista_de_compras[deletar_item-1]
            print(item_compra," foi deletado")
            time.sleep(2)
            continue
        if opcao_lista == "3":
            if lista_de_compras == []:
                print("\nNão há nenhum item para listar")
                time.sleep(2)
                continue
            os.system('cls') or None
            print("Esta é sua lista")
            for indice,item in enumerate(lista_de_compras):
                print(indice+1,"-",item)
            input("\nDigite qualquer coisa para continuar: ")
            continue
        if opcao_lista == "4":
            print("Saindo...")
            time.sleep(2)
            os.system("cls") or None
            quit()
        else:
            print("Digite uma opção válida")
            time.sleep(3)
            os.system("cls") or None
except:
    print("Digite algo válido")
    time.sleep(2)
    os.system("cls") or None