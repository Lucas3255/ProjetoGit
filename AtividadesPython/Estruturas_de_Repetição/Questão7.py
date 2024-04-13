# 7 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
# compreendido por eles. Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
soma = 0

for num in range(num1, num2 + 1):
    print(num)
    soma += num

print(f'A soma dos números é: {soma}')
