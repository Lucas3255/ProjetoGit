# 2 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
# F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Informe qual o sexo (F - Feminino | M - Masculino): ')
if sexo == 'F' or sexo == 'f':
  print('O genêro é Feminino.')
elif sexo == 'm' or sexo == 'M':
  print('O genêro é Masculino.')
else:
  print('Informe uma resposta válida.')
