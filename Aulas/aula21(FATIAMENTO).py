#fatiamento por indices
#           012345678
variavel = "Quero pão"
#          -987654321

print(variavel[6])

#fatiamento inicio 
print(variavel[6:])
#fatiamento final
#Vai até o final da string se omitir
#se não determina um fim, AVISO: SEMPRE +1 POIS ELE PARA 1 A MENOS
print(variavel[6:8])
print(variavel[6:9])
print(variavel[0:6])

#len serve para contar a quantidade de caracteres
print(len(variavel[6:9]))

#fatiamento passo
#de quantos em quantos caracteres vai mostrar
print(variavel[::-1])
