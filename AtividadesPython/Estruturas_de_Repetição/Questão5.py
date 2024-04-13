# 5 - Faça um programa que leia 5 números e informe a soma e a média dos números.

for i in range(5):
    num = float(input(f'Digite o {i + 1}º número: '))
    soma += num

media = soma / 5

print(f'A soma dos números é: {soma}')
print(f'A média dos números é: {media}')
