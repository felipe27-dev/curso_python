"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
#! Não utilize o método global - má prática de programação
#! Evite usar uma váriavel global, renomeada em um escopo local
#@ Ao invés disso use parâmetros e argumentos, são mais organizados e não causam conflito
#@ Caso dúvida no funcinamento do escopo, debugue o código
x = 1 # escopo global
z = 2 # escopo global
def escopo():
    x = 10 # escopo local de escopo()
    global z # torna a variável global
    z = 200 # escopo global
    print(x) # 10
    # Um escopo menor consegue atingir outro menor mas não um maior
    def escopo2():
        y = 2 # escopo local de escopo2()
        print(x, y) # 10,2
    escopo2()

print(z) # 2 # escopo global
print(x) # 1 # escopo global
escopo() # 10 #10,2 #escopos locais
print(x) # 1 # escopo global
print(z) # 200 # escopo global modificado pela função escopo e o método global