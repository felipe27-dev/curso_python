"""
VARIÁVEIS COM LETRA MAISCÚLA PARA QUAIS NÃO VÃO MUDAR
Letra minuscúla pras que mudam

CÓDIGOS COM MUITO IF DENTRO DE IF (RUIM)
QUANTO MAIS SIMPLES MELHOR O CÓDIGO
"""

velocidade = 61
km_carro = 100

RADAR_1 = 60
KM_LOCAL = 100
RANGE_RADAR = 1
#Verificações
vel_maior_q_radar = velocidade > RADAR_1

range_radar_menor = km_carro >= (KM_LOCAL-RANGE_RADAR)
range_radar_maior = km_carro <= (KM_LOCAL+RANGE_RADAR)

km_no_range = range_radar_menor and range_radar_maior

carro_multado = vel_maior_q_radar and km_no_range

if vel_maior_q_radar:
    print("O carro passou da velocidade")

if carro_multado:
    print("Está na faixa do radar, carro foi multado") 
else: 
    print("Não está na faixa do radar")


