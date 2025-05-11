"""Archivo que maneja la logica del menu"""

# Principalme por decoracion, importa verificaciones
from utils import printColor, eraseWS

def start():
    """Funcion que maneja las entrada principal del programa,
    Imprime el menu y tiene el hilo principal[Se repite]
    """
    printColor("","bold")
    printColor("\t1 => Iniciar Partida\n","blue")
    printColor("\t2 => Restablecer Partida\n","blue")
    printColor("\t3 => Tutorial\n","green")
    printColor("\t4 => Salir\n","red")

    option = eraseWS(input("\t Escoge una opcion:\t=> "))
    
    if option == "1":
        print("Iniciando partida")
    elif option == "2":
        print("Cargando Partida")
    elif option == "3":
        playTutorial()
    elif option == "4":
        print("Gracias por Jugar...")
        return
    else:
        print("\t\t\tOpcion no valida\n")

    start()


def playTutorial():
    """Funcion que imprime el tutorial al usuario,
    donde se le guia como funciona el juego
    """
    pass