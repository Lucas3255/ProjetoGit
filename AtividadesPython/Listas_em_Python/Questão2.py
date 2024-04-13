# 2 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor_A = [10]

for i in range(10):
  numero = int(input(f'Digite o {i+1} numero inteiro para o vetor A: '))
  vetor_A.append (numero)


  soma_quadrados = sum(x**2 for x in vetor_A)

print(f'\nSoma dos quadrados dos elementos do vetor A:{soma_quadrados}  ')
