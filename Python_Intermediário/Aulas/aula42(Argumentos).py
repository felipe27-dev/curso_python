"""
Argumentos nomeados tem como nome (=) sinal de igual
Argumentos não nomeados (Posicionais) recebe apenas o argumento (valor)
"""
def soma(x,y):
    print(x/y)

soma(6,3) #argumentos nomeados resultado: 2.0
soma(y=6,x=3) #argumentos não nomeados resultado: 0.5
