"""Archivo para manejar las utilidades
   imprimir en color{""} o verificar"""

def isNum(num):
    """Comprueba que todos los caracteres de un string sean numericos
    
        Entradas:
            num: El string a verificar
            
        Salidas:
            Booleano: True si todos los caracteres son numericos,
                      False en caso contrario

        Ejemplos:
            isNum("123") -> True
            isNum("1az7") -> False
            
        Restricciones:
            num: Debe ser un str
    """
    if not isinstance(num,str):
        return "Error01"
    if num == "":
        return False

    return isNumAux(num)

def isNumAux(num):
    """Funcion auxiliar de verificar_todos_numéricos"""
    if num == '':
        return True
    
    if not isValidDigit(num[0]):
        return False
    
    return isNumAux(num[1:])


def isValidDigit(digit):
    """Funcion auxiliar para isNum, verifica
       si un str de len(1) es un numero
       
       Entradas:
            num: El string a verificar
            
        Salidas:
            Booleano: True si el caracter es numerico,
                      False en caso contrario

        Ejemplos:
            isValidDigit('1') -> True
            isValidDigit('a') -> False
            
        Restricciones:
            digit: debe ser un str, len
                   no mayor a 1
    """
    if not isinstance(digit,str):
        return "Error01"
    
    if len(digit) > 1:
        return "Error02"
    
    return isValidDigitAux(digit,['1','2','3','4','5','6','7','8','9'])


def isValidDigitAux(digit,allDigits):
    """Funcion auxiliar de isValidDigit"""
    if allDigits == []:
        return False
    
    if digit == allDigits[0]:
        return True
    
    return isValidDigitAux(digit,allDigits[1:])

def eraseWS(texto):
    """Elimina los espacios de un texto 
    
        Entradas:
            texto: El texto del cual se elimanaran los espacios
            
        Salidas:
            String: El texto sin espacios

        Ejemplos:
            eraseWS("Hola Mundo") -> "HolaMundo"
            eraseWS("  test  ") -> "test"

        Restricciones:
            texto: Debe ser un string
    """
    if not isinstance(texto,str):
        return "Error01"

    return eraseWSAux(texto,"")

def eraseWSAux(text,newText):
    """Funcion auxiliar de eraseWS"""
    if text == "":
        return newText

    if text[0] == " ":
        return eraseWSAux(text[1:],newText)

    return eraseWSAux(text[1:],newText + text[0])

def printColor(text,design):
    """Funcion utiliza para decorar el programa
       
        Entradas:
            text: any
            design: La seleccion de color | puede ser
                    pink, blue, cyan, green, yellow,
                    red o underline, si no se escoge
                    ningun solo se imprime el text
        
        Salidas:
            None
        
        Ejemplos:
            printColor("hola","pink") -> None
            stdout: "hola\n" [en rosado]

        Restricciones:
            text: None
            design: None
    """

    if design == "pink":
        print('\033[95m',text)

    elif design == "blue":
        print('\033[94m',text)

    elif design == "cyan":
        print('\033[96m',text)

    elif design == "green":
        print('\033[92m',text)

    elif design == "yellow":
        print('\033[93m',text)

    elif design == "red":
        print('\033[91m',text)

    elif design == "underline":
        print('\033[4m',text)

    else:
        print(text)

    print("\033[0;0m\033[1m",end="")
