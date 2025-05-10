# Main file !!

from menu import start

if __name__ == "__main__":
    start()

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