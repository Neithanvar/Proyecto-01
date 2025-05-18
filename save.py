"""Archivo donde se maneja la logica
para almacenar los datos del juego
"""

def saveGame(autonomy,culture):
    """
        Funcion para almacenar
        los datos del juego

        Entradas:
            autonomy: Lista de la autonomia de cada
                    comunidad
            culture: Lista de la cultura de
                      cada comunidad
        Salidas:
            None

        Restricciones:
            autonomy: Debe ser una lista
            culture: Debe ser una lista
                     ambas tener tener 
                     el mismo len
    """

    with open("game.chocobollo","w") as file:
        file.write("")

    saveGameAux(autonomy,culture)

def saveGameAux(autonomy,culture):
    """Funcion auxiliar de saveGame"""
    if autonomy:

        with open("game.chocobollo","a") as file:   
            file.write(str(autonomy[0]) + "|" +str(culture[0])+'\n')

        saveGameAux(autonomy[1:],culture[1:])
