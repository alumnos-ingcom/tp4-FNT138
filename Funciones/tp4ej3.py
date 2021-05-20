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
            centigrados = float(input("Dame Tus Grados en °C: "))
            fahrenheit = (centigrados * 9/5) + 32
        except ValueError as err:
            raise IngresoIncorrecto ("Valor Invalido") from err
        return(f"Tus {centigrados}°C Equivalen a {fahrenheit} °F")
        
    
    
def convertir_a_centigrados(fahrenheit):
    """
        La funcion Transforma los grados Fahrenheit ingresados por consola
        a centigrador mediante la formula (°F-32)*5/9 = °C
                                                                                        """
    try:
        fahrenheit = float(input("Dame Tus Grados en °F : "))
        centigrados = (fahrenheit - 32)*5/9
    except ValueError as err:
        raise IngresoIncorrecto ("Valor Invalido") from err
    return (f"Tus {fahrenheit}°F Equivalen a {centigrados} °C")
    

def prueba():
    C = convertir_a_centigrados(0)
    F = convertir_a_fahrrenheit(0)
    print(C)
    print(F)
    

if __name__ == "__main__":
    prueba()
