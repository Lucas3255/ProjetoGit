# 12 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável (peso de peixes)
# e calcule o excesso. Gravar na variável a quantidade de quilos além do limite e na variável o valor da multa que João deverá 
# pagar. Imprima os dados do programa com as mensagens adequadas.

peso_peixe = float(input('Informe o peso dos peixes (em quilos): '))
limite_peso = 50
if peso_peixe > limite_peso:
  excesso = peso_peixe - limite_peso
  multa = excesso * 4
  print(f'Peso dos peixes: {peso}')
