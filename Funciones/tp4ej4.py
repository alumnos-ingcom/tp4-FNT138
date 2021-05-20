################
# Fede Trujillo - @FNT-138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import IngresoIncorrecto

def compara(numero):
    try:
        numero = (int(input("Ingrese Un Numero Para Comparar: #")))
        otro_numero = (int(input("Ingrese Otro Numero Para Comparar: #")))
    except ValueError as err:
        raise IngresoIncorrecto ("Valor no Permitido")
    
    if numero < otro_numero:
        return -1
    if numero > otro_numero:
        return 1
    if numero == otro_numero:
        return 0



def prueba():
    comparar = compara(1)
    print (comparar)
if __name__ == "__main__":
    prueba()
