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

def printColor(text,color):

    # Borrar en produccion
    def exampleColors():
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        print(f"{HEADER}This is HEADER color{ENDC}")
        print(f"{OKBLUE}This is OKBLUE color{ENDC}")
        print(f"{OKCYAN}This is OKCYAN color{ENDC}")
        print(f"{OKGREEN}This is OKGREEN color{ENDC}")
        print(f"{WARNING}This is WARNING color{ENDC}")
        print(f"{FAIL}This is FAIL color{ENDC}")
        print(f"{BOLD}This is BOLD text{ENDC}")
        print(f"{UNDERLINE}This is UNDERLINE text{ENDC}")

    pass