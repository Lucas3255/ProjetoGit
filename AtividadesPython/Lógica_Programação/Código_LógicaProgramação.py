import time

parar = False
while parar == False:
    pergunta = input("--- Um Programa Aí---\n 1 - Rodar de 1 até 10.\n 2 - Personalizado.\n 3 - Encerrar o Programa.\n\n >> ")

    if pergunta == "1":
        print("")
        for i in range(1, 11):
            print(i)
        time.sleep(3)
        parar == True
    elif pergunta == "2":
        num = int(input("\nAté que número você quer que apareça na tela?\n\n >> "))
        for i in range(1, num + 1):
            print(i)
        time.sleep(3)
        parar == True
    elif pergunta == "3":
        print("\nEncerrando programa...")
        time.sleep(3)
        exit()
    else:
        print(f"\nA opção {pergunta} não existe.")
        time.sleep(3)
        parar == True
