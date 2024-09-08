nomes = ["Fleipe","Rebeca","Carol","Ivan"]
nome1,nome2,nome3,nome4 = nomes #desempacotamento
print(nome2)

nome1, *_ = ["Fleipe","Rebeca","Carol","Ivan"]     #peguei apenas um valor 
print(_)#['Rebeca','Carol','Ivan']                 #e o resto ficou empacotado
#! NORMALMENTE O RESTO NÃO É USADO E POR CONVENÇÃO, É UTILIZADO O _ (UNDERLINE)