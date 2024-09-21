"""
Ao definir uma função, os parâmetros (argumentos)
podem ter valores padrões. Caso o valor não seja
enviado para o parâmetro, o valor padrão será usado

Refatorar: Editar o seu código
"""
#! Usar 0 como valor padrão é ruim para o desenvolvimento
def soma(x,y,z=None): #Valor padrão = None
    if z is None: #Verificação se o Z existe
        print((x/y))
    else:
        print((x/y+z))
        
soma(6,3,9)
soma(6,3)