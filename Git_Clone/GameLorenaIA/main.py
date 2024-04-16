import time
import os

# Alteração realizada!!!

################ CORES #################
class colors:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
########################################

############## VARIÁVEIS ###############
corLorena = colors.cyan
corYou = colors.yellow
continuar = f"{corYou} Pressione Enter para continuar "
pacienciaLorena = 0
########################################

def loading():
    for i in range(1, 8):
        print("o", end="", flush = True)
        time.sleep(1)

def animarText(texto):
    for char in texto:
        print(char, end="", flush = True)
        time.sleep(0.05)

def Lorena():
    print(f"""{corLorena}
    ---------------------------------------------
    -------------------:*====*-------------------
    ----------------:###========#=**-------------
    ---------------*#######====####==*-----------
    --------------+########=====#@#=##*----------
    -------------:=#==@@@##===*+::##==#=---------
    -------------*##=#@@@@#*::-----:##=#*--------
    ------------+#@#=#@@@#*:::------:#@=#--------
    -----------+=###=##@####*::::----:@@#--------
    -----------*####=#@##==**==+:::**=@@@*-------
    ----------:=@@##=####==****++*##=@@@@=-------
    ----------:=@@##=##=**+::::::::+=@@@@#-------
    -----------=@@##=@##=*+::::::-::#@@@@#-------
    -----------:#@####@##=*++**+::+@@@@@@=-------
    ----+**#@#####@@@@@@@#*==*+++#@@@@@@#--------
    --******=#@@@WWWW@@#@@@=*++**#@@@@@=---------
    -***======#@@WWW@W@##@WW@@@@@@####=**--------
    #########=#@@WWWWWW@@@@@@@@@@@@@###==*-------
    =======###@@@@WWWWWWW@@@@@@W@W@@@@###=*------
    #@@@#####@@=##@@@@@@@@W@@@@WWWW@@@@@@###=*---
    +*=@W@##@@W@====@@@@@@WW@@@WWWW@@@@@@@@@@@@#*
    +**=@W@#@WW@@@@@@@@@@@@WW@@@WWWW@@@@@@@@@@@@@
    ***=#W@@@@W@@@@@@@@@@@@@WW@WWWWWW@@@@@@@@@###
    **==@W@@@@WW@@@@@@@@@@@WWWWWWWW@@@=@@@@#####@
    ===@W=+@@@WWWWW@@@@W@@WWWWWWWW@#@#*=@@@@@@@@W
    =#W@---@@@WWWWWW@@WW@@@WWWWW@@@###--*@@@@@@W#
    #=------=@@WWWWWWW@@W@@WWWWW@@@@##=--*#@@@W@#
    -------+@@WWWWWWWWWW@@@@WW@@@@@#=------#@@W@#
    --------#@@WWWWWWWW@@@@@@@@@@@@#=-------=@@W@
    --------=@W@@@WWWWW@@@@@@@@@@@@#=----------#W\n""")

#################################################

print("   LOADING    ")
#loading()
os.system("cls")

lorena = " @ Olá! Eu me chamo Lorena, sou uma inteligência\n artificial.\n\n"
Lorena()
animarText(lorena)
input(continuar)
os.system("cls")

lorena = " @ Qual o seu nome?\n\n"
Lorena()
animarText(lorena)

youName = input(f"{corYou} $ ")
os.system("cls")
lorena = f" @ Ohh, é um prazer lhe conhecer {youName}.\n Espero que sejamos melhores amigos.\n\n"
Lorena()
animarText(lorena)
input(continuar)
os.system("cls")

###########################################################
