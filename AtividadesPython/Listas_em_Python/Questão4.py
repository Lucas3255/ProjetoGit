# 4 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    elemento1 = int(input(f'Digite o {i+1}º elemento do vetor 1: '))
    elemento2 = int(input(f'Digite o {i+1}º elemento do vetor 2: '))
    elemento3 = int(input(f'Digite o {i+1}º elemento do vetor 3: '))
    vetor1.append(elemento1)
    vetor2.append(elemento2)
    vetor3.append(elemento3)

vetor_intercalado = [val for triple in zip(vetor1, vetor2, vetor3) for val in triple]

print(f'\nVetor 1: {vetor1}')
print(f'Veetor 2: {vetor2}')
print(f'Veetor 3: {vetor3}')
print(f'Vetor Intercalado: {vetor_intercalado}')
