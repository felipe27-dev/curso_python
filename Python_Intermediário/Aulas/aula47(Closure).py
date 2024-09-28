def saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

falar_oi = saudacao("Oi")
falar_tchau = saudacao("Tchau")

for nome in ["Fleipe","Rebeca","Carol"]:
    print(falar_oi(nome))
    print(falar_tchau(nome))

