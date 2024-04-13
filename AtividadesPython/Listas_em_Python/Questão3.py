# 3 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = []
vetor2 = []

for i in range(10):
    elemento1 = int(input(f'Digite o {i+1}º elemento do vetor 1: '))
    elemento2 = int(input(f'Digite o {i+1}º elemento do vetor 2: '))
    vetor1.append(elemento1)
    vetor2.append(elemento2)

vetor_intercalado = [val for pair in zip(vetor1, vetor2) for val in pair]

45print(f'\nVetor 1: {vetor1}')
print(f'Vetor 2: {vetor2}')
print(f'Vetor Intercalado: {vetor_intercalado}')
