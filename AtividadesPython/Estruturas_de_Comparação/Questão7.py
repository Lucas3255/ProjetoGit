# 7 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

preco_produto1 = float(input('Digite o preço do primeiro produto: '))
preco_produto2 = float(input('Digite o preço do segundo produto: '))
preco_produto3 = float(input('Digite o preço do terceiro produto: '))

if preco_produto1 < preco_produto2 and preco_produto1 < preco_produto3:
    produto_mais_barato = "Produto 1"
    preco_mais_barato = preco_produto1
elif preco_produto2 < preco_produto1 and preco_produto2 < preco_produto3:
    produto_mais_barato = "Produto 2"
    preco_mais_barato = preco_produto2
else:
    produto_mais_barato = "Produto 3"
    preco_mais_barato = preco_produto3

print(f'O produto mais barato é {produto_mais_barato} com preço de R${preco_mais_barato:.2f}')
