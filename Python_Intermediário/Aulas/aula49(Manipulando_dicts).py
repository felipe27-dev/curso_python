pessoa = {
    "nome" : "Jotapê"
}
print(pessoa)

...

pessoa["amigo"] = "Neo" #adiciona chave e valor

print(pessoa)
print(pessoa["amigo"])

del pessoa["amigo"] #deleta chave e valor

print(pessoa)

if (pessoa.get("amigo")): #verifica se existe chave e valor #? Evita Keyword error
    print(pessoa.get("amigo"))
else:
    print("Amigo não existe")