# 3 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')
if letra in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
  print(f'"{letra}" é vogal.')
else:
  print(f'"{letra}" é uma consoante')
