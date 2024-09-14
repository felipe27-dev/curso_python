#Listas dentro de listas
salas = [
    ["Meg","Jessie","Nita"],
    ["Sam","Gale","Belle"],
    ["Chester","Cordelius","Dynamike",(0,10,20,30,40)]
]
print(salas)
print(salas[0])
print(salas[0][1])
print(salas[2][3][2])
print("-"*30)
for sala in salas:
    for item in sala:
        print(item)
