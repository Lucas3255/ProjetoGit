# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor = float(input("Digite quanto você ganha por hora: "))
horas = float(input("Digite o número de horas trabalhadas no mês: "))
salario = valor * horas
print(f"Seu salário no mês é: R$ {salario}")
