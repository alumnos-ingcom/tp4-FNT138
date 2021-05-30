################
# Federico Trujillo - @FNT138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def es_primo(numero):
    """
    La Funcion Indica Si El Numero Ingresado Pertenece A
    Los Numero Primos
    """   
    if numero < 1:
        return false
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True
    
def prueba():
    numero = ingreso_entero("Ingrese un numero para ver si es primo:")
    primo = es_primo(numero)
    
    print(primo)

if __name__ == "__main__":
    prueba()