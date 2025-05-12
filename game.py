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

    if isNum(communitiesSize) and not generateCommunities(int(communitiesSize)):
        print("ASd")
        
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

def playTurn(culture,autonomy):
    """Sigue la mecanica del juego de turnos,
       le pregunta al usuario cual comunidad 
       quiere proponer cambios y que tipo

       Entradas:
            culture:
            autonomy:

        Salidas:
            None

        Restricciones:
            culture:
            autonomy
    """
    if not isinstance(culture,list) or not isinstance(autonomy,list):
        return "Error01"
    
    if culture and autonomy:

        printCommunities(culture,autonomy)

        printColor("\t\t 1 - Mejorar Autonomia ", "yellow")
        printColor("\t\t 2 - Mejorar Acervo Cultural", "yellow")
        option = eraseWS(input("\t\t Que proyecto quieres realizar: \t => "))

        if option == "1":
            autonomy = generateChanges(autonomy)
        elif option == "2":
            culture = generateChanges(culture)
        else:
            printColor("\t\t Haz seleccionado un proyecto invalido ","red")

            
        # Realizar el cambio de agentes externos

        if option == "1" or option == "2":
            # Reutilizar la variable para seleccionar
            # Que evento se dara por los agentes
            option = randint(1, 2)
            # Seleccionar comunidad
            community = randint(1, len(autonomy))
            debuff = randint(25, 25 + 5 * len(autonomy))
            if option == 1:
                if stopsExisting(autonomy,debuff,community):
                    autonomy = eraseCommunity(autonomy,community)
                    culture = eraseCommunity(culture,community)
                else:
                    autonomy = updateCommunity(autonomy,debuff,community)
            else:
                if stopsExisting(culture,debuff,community):
                    autonomy = eraseCommunity(autonomy,community)
                    culture = eraseCommunity(culture,community)
                else:
                    culture = updateCommunity(culture,debuff,community)


        playTurn(culture,autonomy)


def printCommunities(culture,autonomy):   
    """"""
    for cul in culture:
        print(cul, " ")
    for asd in autonomy:
        print(asd, " ")

def generateChanges(values):
    """"""
    if not isinstance(values,list):
        return "Error01"
    
    option = eraseWS(input("\t\t Que comunidad quieres apoyar: \t => "))

    if isNum(option):
        if int(option) > len(values) or int(option) < 1:
            printColor("\t\t Debes seleccionar una comunidad valida")
            return generateChanges(values)
        
        return generateChangesAux(values,int(option),0,len(values))
    
    printColor("\t\t Debes seleccionar una comunidad valida")
    return generateChanges(values)

def generateChangesAux(values,community,index,amt):
    """Funcion auxiliar de generateChanges"""
    if not values:
        return []
    
    if index == community: 
        buff = randint(20, 20 + 3 * amt)

        if values[0] + buff > 100:
            return [100] + values[1:]
        
        return [values[0] + buff] + values[1:]
    
    return [values[0]] + generateChangesAux(values[1:],community,index+1,amt)

def eraseCommunity(values,community):
    """"""
    if not isinstance(values,list):
        return "Error01"
    if not isinstance(community,int):
        return "Error02"
    
    return eraseCommunityAux(values,community,1)

def eraseCommunityAux(values,community,index):
    """Funcion auxiliar de eraseCommunity"""
    if not values:
        return []
    if index == community:
        return values[1:]
    return [values[0]] + eraseCommunityAux(values[1:],community,index+1)
    
def updateCommunity(values,debuff,community):
    """"""
    if not isinstance(values,list):
        return "Error01"
    if not isinstance(debuff,int):
        return "Error02"
    if not isinstance(community,int):
        return "Error03"
    
    return updateCommunityAux(values,debuff,community,1)

def updateCommunityAux(values,debuff,community,index):
    """Funcion auxiliar de updateCommunity"""
    if not values:
        return []
    if community == index:
        return [values[0] - debuff] + values[1:]
    
    return [values[0]] + updateCommunityAux(values[1:],debuff,community,index+1)

def stopsExisting(values,debuff,community):
    """"""
    if not isinstance(values,list):
        return "Error01"
    if not isinstance(debuff,int):
        return "Error02"
    if not isinstance(community,int):
        return "Error03"
    
    return stopsExistingAux(values,debuff,community,1)

def stopsExistingAux(values,debuff,community,index):
    """Funcion auxiliar de stopsExisting"""
    if not values:
        return False
    if community == index:
        if values[0] - debuff < 1:
            return True
        return False
        
    return stopsExistingAux(values[1:],debuff,community,index+1)


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