################
# Fede Trujillo - @FNT138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import IngresoIncorrecto

def convertir_a_fahrrenheit(centigrados):
    """
        Convierte Grados Centigrados a Fahrenheit mediante la formula
        (C°*9/5) + 32 = F°
    """
    try:
        centigrados = float(centigrados)
        centigrados = (centigrados * 9/5) + 32
    except ValueError as err:
        raise IngresoIncorrecto ("Valor Invalido") from err
    return centigrados

def convertir_a_centigrados(fahrenheit):
    """
        La funcion Transforma los grados Fahrenheit ingresados por consola
        a centigrador mediante la formula (°F-32)*5/9 = °C
    """
    try:
        fahrenheit = float(fahrenheit)
        fahrenheit = (fahrenheit - 32)*5/9
    except ValueError as err:
        raise IngresoIncorrecto ("Valor Invalido") from err
    return fahrenheit
    
def prueba():
    fahrenheit = input("Ingrese Sus °F: ")
    centigrados = input("Ingrese Sus °C: ")
    
    C = convertir_a_centigrados(fahrenheit)
    F = convertir_a_fahrrenheit(centigrados)
    
    print(f"tus {fahrenheit}°F equivalen a {C} °C")
    print(f"tus {centigrados}°C equivalen a {F} °F")
    
if __name__ == "__main__":
    prueba()
