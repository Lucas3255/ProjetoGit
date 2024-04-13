# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# - O produto do dobro do primeiro com metade do segundo .
# - A soma do triplo do primeiro com o terceiro.
# - O terceiro elevado ao cubo.

int1 = int(input('Digite um número inteiro: '))
int2 = int(input('Digite outro número inteiro: '))
real = float(input('Digite um número real, pode ser um quebrado mesmo: '))

produto = (int1 * 2) * (int2 / 2)
soma = (int1 * 3) + real
elevado = (real ** 3)

print(f'Produto = {produto}')
print(f'Soma = {soma}')
print(f'terceiro calculo = {elevado}')
