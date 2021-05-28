################
# Fede Trujillo - @FNT138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def cociente_calc(num1, num2):
    """
    La funcion Calcula El cociente de dos numero mediante restas sucesivas
    """
    cociente = 0
    while num1 >= num2:
        num1 = num1 - num2
        cociente = cociente +1
    return cociente
    
def resto_calc(num1, num2):
    """
    La Funcion Calcula El Resto De Dos Numeros Mediante Restas Sucesivas
    """
    resto = 0
    while num1 >= num2:
        num1 = num1 - num2
        resto = num1
    return resto

def prueba():
    num1 = ingreso_entero("Ingrese un numero:")
    num2 = ingreso_entero("Ingrese otro numero:")    
    cocient_ = cociente_calc(num1, num2)
    rest_ = resto_calc(num1, num2)
    
    print(f"El cociente de {num1} y {num2} es {cocient_}")
    print(f"El resto de {num1} y {num2} es {rest_}")

if __name__ == "__main__":
    prueba()