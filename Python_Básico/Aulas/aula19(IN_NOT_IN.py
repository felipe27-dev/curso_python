
comen1 = "Amo minecraft, melhor jogo"
comen2 = "Amo fortinite, melhor fps"
print(comen1)
print(comen2)

busca = input("Digite a palvra que deseja buscar: ")

if (busca in comen1) and (busca not in comen2):
    print("A palavra {} está no comentário 1".format(busca))
    print ("Este é o comentário: ",comen1)
elif (busca not in comen1) and (busca in comen2):
    print("A palavra {} está no comentário 2".format(busca))
    print ("Este é o comentário: ",comen2)
elif (busca not in comen1) and (busca not in comen2):
    print("Está palavra não foi encontrada em nenhum comentário")
elif (busca in comen1) and (busca in comen2):
    print("A palavra {} está nos dois comentários".format(busca))
    print ("Estes são os comentários: ")
    print(comen1)
    print(comen2)