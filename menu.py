# Mainly for asthethic purpose
from utils import *

def start():
    listMenu = ["\t1 => Iniciar Partida",
                "\t2 => Restablecer Partida",
                "\t3 => Tutorial",
                "\t4 => Salir"]

    option = eraseWS(input("\033[1m\t Escoge una opcion:\t=> "))

    if isNum(option):

        if int(option) == 1:
            print("Iniciando partida")
        elif int(option) == 2:
            print("Cargando Partida")
        elif int(option) == 3:
            playTutorial()
        elif int(option) == 4:
            print("Gracias por Jugar...")
            return
        else:
            print("Escogiste una opcion no valida")

    else:
        print("Opcion no valida, digita un numero valido")
        
    start()


def playTutorial():
    pass