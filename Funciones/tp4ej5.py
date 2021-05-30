################
# Fede Trujillo - @FNT138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import IngresoIncorrecto, ingreso_entero

def signo(numero):
    """
    La Funcion signo Devuelve El Signo Del Numero Ingresado,
    Siendo 1 si es positivo, -1 si es negativo y 0 si es igual a cero
    """
    if numero == 0:
        return 0
    if numero > 0:
        return 1
    if numero < 0:
        return -1
    
def prueba():
    numero = ingreso_entero("Ingrese un numero: ")    
    func = signo(numero)
    
    print(func)    
    
if __name__ == "__main__":
    prueba()