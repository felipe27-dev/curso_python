# Exercício - sistema de perguntas e respostas
import os
import time
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
lista_opcoes = ['A','B','C','D']
os.system("cls") or None
while True:
    i = 1
    acertos = 0
    for pergunta in perguntas:
        
        #Mostra a pergunta
        pergunta_atual = pergunta.get("Pergunta")
        resposta_correta_atual = pergunta.get("Resposta")
        print(f"Pergunta {i}:",pergunta_atual)
        
        #Mostra as opções	
        print("Opções:")
        for indice,opcao in enumerate(lista_opcoes):
            opcao_atual = pergunta.get("Opções")[indice]
            print(f'{opcao})',opcao_atual)
            
            #Selecionando letra correta
            if opcao_atual == pergunta.get("Resposta"):
                letra_correta = opcao
                
        #Recebe as repostas 
        resposta_usuario = input("\nDigite a letra correta: ").upper()
        
        #Verifica se a resposta é valida
        if resposta_usuario not in lista_opcoes:
            print("Digite uma opção válida")
            time.sleep(3)
            os.system("cls") or None
            break
        
        #Verifica erro ou acerto
        if resposta_usuario == letra_correta:
            print("Você acertou! Parabéns🎉🎉🎉\n")
            print("Carregando próxima pergunta")
            time.sleep(3)
            os.system("cls") or None
            acertos += 1
        else:
            print(f"Você errou ❌. A reposta era: {letra_correta}) {resposta_correta_atual}\n")
            print("Carregando próxima pergunta")
            time.sleep(4)
            os.system("cls") or None
        i += 1
    #Mostra resultado final
    print(f"Você acertou {acertos} de {len(perguntas)} perguntas")
    time.sleep(6)
    os.system("cls") or None
    