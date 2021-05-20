################
# Fede Trujillo - @FNT-138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import IngresoIncorrecto
def signo(numero):
    try:
        numero = (int(input("Ingrese Un Numero Para Saber Si Es"
                                        "Positivo, Negativo o Cero: #")))
    except ValueError as err:
        raise IngresoIncorrecto ("Valor invalido")
    
    if numero == 0:
        return(f"El numero {numero} Es 0")
    if numero > 0:
        return(f"El Numero {numero} Es Positivo")
    if numero < 0:
        return(f"El Numero {numero} Es Negativo")



def prueba():
    print(signo("Ingrese Un Numero Para Saber Si es Positivo, Negativo o Cero"))
    
if __name__ == "__main__":
    prueba()