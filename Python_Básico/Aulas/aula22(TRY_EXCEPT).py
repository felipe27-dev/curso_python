
numero = input("Vou dobrar o número que digitar: ")
try:
    numero_float = float(numero)
    print(f"O dobro de {numero_float} é {numero_float*2}")
except:
    print("Poh mano, vc cagou o sistema")