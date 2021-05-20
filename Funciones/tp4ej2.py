################
# Fede Trujillo - @FNT138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import IngresoIncorrecto

def suma_lenta(numero, otro_numero):
    try:
        numero = int (input("Ingrese Un numero: # "))
        otro_numero = int (input("Ingrese Otro numero: # "))
        suma = ""
    except ValueError as err:
        raise IngresoIncorrecto ("Valor No Valido") from err
    resultado = (f"={numero+otro_numero}")
    
    if otro_numero > 0:
        while otro_numero > 0:
            suma = suma+"+1"
            otro_numero = otro_numero-1
        return str(numero)+suma+ resultado
    
    else:
        while otro_numero < 0:
            suma = suma+"-1"
            otro_numero = otro_numero +1
        return str(numero) + suma+ resultado    

def prueba():
    num = suma_lenta( 0, 0)
    print(num)

if __name__ == "__main__":
    prueba()