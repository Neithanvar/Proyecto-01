"""Archivo que maneja la logica del menu"""

import time 

# Principalme por decoracion, importa verificaciones
from utils import printColor, eraseWS

# Inicio del juego 
from game import startGame, printCommunities
from load import loadGame

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
        printColor("\t\t ...\t...\t...","yellow")
        startGame()
    elif option == "2":
        printColor("\t\t Cargando Partida","yellow")
        loadGame()
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

    printColor("\t\t Eres una asamblea la cual \n\t\t" \
               " tienes que responsabilisarte por las comunidades","yellow")
    
    time.sleep(3)
    printColor("\t\t Tu mision va a ser -> mantener el bienestar \n\t\t" \
    " tienes dos herramientas para esto:\n","pink")

    time.sleep(3)
    printColor("\t\t -> #1 Apoyar la autonomia de una comunidad \n" \
    "\t\t -> #2 Apoyar el acervo de una comunidad\n\n","blue")

    time.sleep(3)
    printColor("\t\t Se te mostraran las comunidades y tienes que escoger" \
    "\n\t\t a cual apoyar","blue")

    time.sleep(3)
    printCommunities([70,80],[45,95])

    time.sleep(3)
    printColor("\t\t Solo tienes que escoger una comunidad valida","yellow")

    time.sleep(3)
    printColor("\t\t Ten en cuenta que cada vez que apoyes a" \
    "una comunidad, un agente externo atacara otra", "red")

    time.sleep(3)
    printColor("\t\t Buena suerte y manten a todos vivos! ","yellow")


