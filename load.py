"""Archivo para almacenar la logica
de cargar los datos
"""

from game import playTurn,startGame
from utils import printColor

def loadGame():
    """
    """
    # Que no salte error si no existe el archivo
    with open("game.chocobollo","a") as file:
        print()
            

    with open("game.chocobollo") as file:
        data = file.read()
        if data:

            autonomy = readData(data,True)
            culture = readData(data,False)
            printColor("\t\t Se ha cargado la partida","yellow")
            playTurn(autonomy,culture)

        else: 

            printColor("\t\t No se ha encontrado una partida","red")
            startGame()


def readData(data,check):

    return readDataAux(data,check,0,[])

def readDataAux(data,check,num,arr):
    if not data:
        return arr
    if data[0] == "|":
        if not num == 0:
            return readDataAux(data[1:],not check,0,arr + [num])
        return readDataAux(data[1:],not check,0,arr)
    elif data[0] == "\n":
        if not num == 0:
            return [num] + readDataAux(data[1:],not check,0,arr +[num])
        return readDataAux(data[1:],not check,0,arr)
        
    if check:
        num = num * 10 + int(data[0])
        return readDataAux(data[1:],check,num,arr)

    return readDataAux(data[1:],check,num,arr)

    