"""Archivo para manegar la logica del juego
   tanto los turnos como el trabajo con numeros
   que se puede llegar a dar con los aleatorios"""

# Manejar los numeros aleatorios
from random import randint
from save import saveGame

# Para verificaciones y decoracion
from utils import *

def startGame():
    """Inicializa el juego, creando comunidades"""

    communitiesSize = eraseWS(input("\t Cuantas comunidades deseas crear? [1,100]\t => "))

    if isNum(communitiesSize) and not generateCommunities(int(communitiesSize)):
        printColor("\t\t\tGracias por jugar","underline")
        
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
    if num < 1 or num > 100:
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
                   a generarse los valores[enteros]
       
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

def playTurn(autonomy,culture):
    """Sigue la mecanica del juego de turnos,
       le pregunta al usuario cual comunidad 
       quiere proponer cambios y que tipo

       Entradas:
            culture: La lista con los valores
                     de acervo cultural de las
                     comunidades
            autonomy: La lista con los valores
                      de autonomia de las 
                      comunidades

        Salidas:
            None

        Restricciones:
            culture:
            autonomy
    """
    if not isinstance(culture,list) or not isinstance(autonomy,list):
        return "Error01"
    
    playTurnAux(autonomy,culture)

def playTurnAux(autonomy,culture):
    """Funcion auxiliar de playTurn"""
    if culture and autonomy:

        saveGame(autonomy,culture)

        printCommunities(autonomy,culture)

        printColor("\t\t 1 - Mejorar Autonomia ", "yellow")
        printColor("\t\t 2 - Mejorar Acervo Cultural", "yellow")

        option = eraseWS(input("\t\t Que proyecto quieres realizar:  => "))

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

            # Seleccionar comunidad a atacar
            community = randint(1, len(autonomy))
            debuff = randint(25, 25 + 5 * len(autonomy))

            printCommunities(autonomy,culture)

            if option == 1:

                printColor("\t\t Una minera ha atacado a la comunidad #"+str(community),"red")
                printColor("\t\t Reduciendo su autonomia por " +str(debuff),"red")


                if stopsExisting(autonomy,debuff,community):

                    printColor("\t\t La comunidad #"+str(community) + " ha dejado de existir","red")
                    autonomy = eraseCommunity(autonomy,community)
                    culture = eraseCommunity(culture,community)
                else:
                    autonomy = updateCommunity(autonomy,debuff,community)
            else:
                
                printColor("\t\t Unos misioneros han atacado a la comunidad #"+str(community),"red")
                printColor("\t\t Reduciendo su acervo Cultural por "+str(debuff),"red")

                if stopsExisting(culture,debuff,community):

                    printColor("\t\t La comunidad #"+str(community) + " ha dejado de existir","red")
                    autonomy = eraseCommunity(autonomy,community)
                    culture = eraseCommunity(culture,community)
                else:
                    culture = updateCommunity(culture,debuff,community)
    


        playTurnAux(autonomy,culture)

def printCommunities(autonomy,culture):   
    """
        Funcion que imprime la informacion
        de las comunidades de una manera 
        visualmente placentera

        Entradas:
            autonomy: lista de autonomia
            culture: lista de acervo
        
        Salidas:
            None
        
        Ejemplos:

        printCommunites([66,40],[45,44]) ->
               _| |_____________________________________________________________| |_
               _   _____________________________________________________________   _
                | |    Comunidad #1:    Autonomia: 66   Aciervo Cultural: 45    | |
                | |    Comunidad #2:    Autonomia: 40   Aciervo Cultural: 44    | |
               _| |_____________________________________________________________| |_
               _   _____________________________________________________________   _
                | |                                                             | | 
        
        printCommunites([20],[11]) ->
               _| |_____________________________________________________________| |_
               _   _____________________________________________________________   _
                | |    Comunidad #1:    Autonomia: 20   Aciervo Cultural: 11    | |
               _| |_____________________________________________________________| |_
               _   _____________________________________________________________   _
                | |                                                             | | 

        Restricciones:
            autonomy: Debe ser una lista de numeros
            culture: Debe ser una lista de numeros
                     Deben ser del mismo len
    """

    printTop()
    printMiddle(autonomy,culture)
    printBottom()

def generateChanges(values):
    """
        Funcion que maneja la logica
        para ser la asamblea
        Significa: donde se pide
        que comunidad beneficiar
    """
    if not isinstance(values,list):
        return "Error01"
    
    option = eraseWS(input("\t\t Que comunidad quieres apoyar: \t => "))

    if isNum(option):
        if int(option) > len(values) or int(option) < 1:
            printColor("\t\t Debes seleccionar una comunidad valida","red")
            return generateChanges(values)
        
        return generateChangesAux(values,int(option),1,len(values))
    
    printColor("\t\t Debes seleccionar una comunidad valida","red")
    return generateChanges(values)

def generateChangesAux(values,community,index,amt):
    """Funcion auxiliar de generateChanges"""
    if not values:
        return []
    
    if index == community: 

        buff = randint(20, 20 + 3 * amt)
        printColor("\n\t\t Haz apoyado a la comunidad con " +str(buff) + " puntos\n","cyan")


        if values[0] + buff > 100:
            return [100] + values[1:]
        
        return [values[0] + buff] + values[1:]
    
    return [values[0]] + generateChangesAux(values[1:],community,index+1,amt)

def eraseCommunity(values,community):
    """
        Funcion que elimina una comunidad
        de la lista [ya sea de autonomia
        o de culture]

        Entradas:
            values: La lista con los valores
                    de las comunidades
            community: Entero con la comunidad
                       a eliminar

        Salidas:
            list: values sin la comunidad escogida

        Ejemplos:
            eraseCommunity([1,5,10],2) ->
                [1,10]
            eraseCommunity([70,59,33],1) ->
                [59,33]

        Restricciones:
            values: Debe ser una lista de
                    enteros
            community: Debe ser un entero
                       dentro del rango de la lista
    """
    if not isinstance(values,list):
        return "Error01"
    if not isinstance(community,int):
        return "Error02"
    if community > len(values):
        return "Error03"

    return eraseCommunityAux(values,community,1)

def eraseCommunityAux(values,community,index):
    """Funcion auxiliar de eraseCommunity"""
    if not values:
        return []
    if index == community:
        return values[1:]
    return [values[0]] + eraseCommunityAux(values[1:],community,index+1)
    
def updateCommunity(values,debuff,community):
    """
        Funcion que cambia un valor en
        un arreglo, en un indice especifico

        Entradas:
            values: La lista con los valores
                    de la comunidad
            debuff: Entero con el valor a restar
            community: Entero con la comunidad
                       a restar

        Salidas:
            lista: la lista modificada

        Ejemplos:
            updateCommunity([20,30,40],5,2) ->
                [20,25,40]
            updateCommunity([10,9,8],1,1) ->
                [9,9,8]

        Restricciones:
            values: Debe ser una lista
                    con valores numericos
            debuff: Debe ser un entero positivo
            community: Debe ser un entero dentro
                       del rango de la lista
    """
    if not isinstance(values,list):
        return "Error01"
    if not isinstance(debuff,int):
        return "Error02"
    if not isinstance(community,int):
        return "Error03"
    if community > len(values):
        return "Error04"
    
    return updateCommunityAux(values,debuff,community,1)

def updateCommunityAux(values,debuff,community,index):
    """Funcion auxiliar de updateCommunity"""
    if not values:
        return []
    if community == index:
        return [values[0] - debuff] + values[1:]
    
    return [values[0]] + updateCommunityAux(values[1:],debuff,community,index+1)

def stopsExisting(values,debuff,community):
    """
        Comprueba si una comunidad deja de existir

        Entradas:
            values: La lista de valores
            debuff: Entero a restar a una
                    comunidad
            community: El indice de la comunidad
                       a restar el valor

        Salidas:
            bool: True si la comunidad deja de
                  existir, False si no

        Ejemplos:
            stopsExisting([10,20,30],35,3) ->
                True
            stopsExisting([60,70,80],20,1) ->
                False

        Restricciones:
            values: Debe ser una lista de valores
            debuff: Debe ser un entero positivo
            community: Debe ser un entero dentro
                       del rango de la lista

    """
    if not isinstance(values,list):
        return "Error01"
    if not isinstance(debuff,int):
        return "Error02"
    if not isinstance(community,int):
        return "Error03"
    if community > len(values):
        return "Error04"
    
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

