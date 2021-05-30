################
# Fede Trujillo - @FNT138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import IngresoIncorrecto, ingreso_entero

def suma_lenta(numero, otro_numero):
    """
    Suma Dos Numeros Enteros Sin Hacer La Operacion Directa
    ej:
        4 + 2 = 4+1+1
    """
    num1 = numero
    num2 = otro_numero
    suma = " "
        
    if  num2 > 0:
        while num2 > 0:
            suma = suma+"+1"
             num2 = num2 - 1
        return suma
    
    else:
        while num2 < 0:
            suma = suma+"-1"
            num2 = num2 + 1
        return suma   

def prueba():
    numero = ingreso_entero("Ingrese un numero: ")
    otro_numero = ingreso_entero("Ingrese otro numero: ")
    a_sumar = suma_lenta(numero, otro_numero)
    
    print(f"{numero}{a_sumar} = {numero+otro_numero}")

if __name__ == "__main__":
    prueba()