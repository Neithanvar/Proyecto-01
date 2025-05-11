"""Archivo para manegar la logica del juego
   tanto los turnos como el trabajo con numeros
   que se puede llegar a dar con los aleatorios"""

# Manejar los numeros aleatorios
from random import randint

# Para verificaciones y decoracion
from utils import *

def startGame():
    """Inicializa el juego, creando comunidades"""

    communitiesSize = eraseWS(input("\t Cuantas comunidades deseas crear?[1,100] \t => "))

    if isNum(communitiesSize) and not generateCommunities(communitiesSize):
        generateCommunities(communitiesSize)
        
    else:
        printColor("\t\t\t Escoge entre 1 y 100 comunidades porfavor","cyan")
        startGame()

def generateCommunities(num):
    """Genera las comunidades, segun la 
       cantidad indicada por el usuario 
       previamente

       Entradas:
            num: Un entero con la cantidad de comunidades

        Salidas:
            str: Un error si la operacion no se puede completar,
                 "" de otra manera

        Ejemplos:
            generateCommunities(2) -> ""
            autonomy -> [55,70], culture -> [80,90]

            generateCommunities(101) -> "Error02"

        Restricciones:
            num: debe ser un entero, entre 1 y 100
        
    """
    if not isinstance(num,int):
        return "Error01"
    if num < 0 or num > 100:
        return "Error02"
    
    autonomy = generateRandomValues(num,20)
    culture = generateRandomValues(num,20)
    playTurn(autonomy,culture)
    return ""

def generateRandomValues(size,range):
    """Funcion que genera valores aleatorios 
       para las comunidades, solo genera una 
       lista a la vez
       
       Entradas:
            size: La cantidad de comunidades que
                  vaya a tener el juego
            range: El valor minimo con el que van
                   a generrse los valores[enteros]
       
       Salidas:
            List: La lista con los valores generados
       
       Ejemplos:
            generateRandomValues(10,20) -> [36,80,20,70,51,63,91,68,33,58]
            El valor maximo que aparecera en la lista puede ser de 100
       
       Restricciones:
            size: Debe ser un entero, mayor a 0 y menor o igual a 100
            range: Debe ser un entero positivo, mayor a 20 y menor o igual a 100
    """
    if not isinstance(size,int) or not isinstance(range,int):
        return "Error01"
    if size > 100:
        return "Error02"
    if range > 100 or range < 20:
        return "Error03"
    
    return generateRandomValuesAux(size,range,0)

def generateRandomValuesAux(size,range,index):
    """Funcion auxiliar de generateRandomValues"""
    if size == index:
        return []
    
    return [randint(range,100)] + generateRandomValuesAux(size,range,index+1)

def playTurn():
    """
    """
    culture = generateChanges()
    autonomy, culture = updateCommunities(autonomy,cultures)
    


"""
-> Implementar, validar y documentar programas

Cantidad de comunidades: debe decidir la cantidad de comunidades con las que estarán trabajando este 
debe  ser un número variable que  se  solicita  al usuario del  programa 

-Comunidad: Cada  comunidad tendrá  dos  
valores relacionados con el trabajo del consejo, a saber:  autonomía y de acervo cultural
de forma aleatoria en rangos definidos por ustedes.
    -Durante la ejecución del programa estos valores(AMBOS) se deben mantener por encima de 0 ya que si alguno de 
los dos valores llega a cero  la comunidad se disuelve

-Turnos
EN CADA TURNO 
UN POSITIVO: 
El   consejo   ejecutará   un   proyecto   en   una   comunidad   que   el   usuario   del   programa   debe 
seleccionar. Cada proyecto estará dirigido a aumentar la autonomía o el acervo cultural de la  
comunidad: el número preciso será seleccionado de forma aleatoria 
EN NEGATIVO:
Agentes externos a las comunidades misioneros o compañías mineras se acercarán a estas y  
realizarán   acciones   que   reducen   su   autonomía   (las   mineras)   o   su   acervo   cultural   (los 
misioneros).   el valor de impacto en el rubro de la comunidad será seleccionado de forma 
aleatoria 

Adicionalmente,   si   todas   las   comunidades   a   cargo   de   un   consejo   se   disuelven.   Se   considera   que   el  
consejo falló en su labor y el programa se cierra. <- acaba ddel juego
"""