################
# Fede Trujillo - @FNT138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import IngresoIncorrecto, ingreso_entero

def compara(numero, otro_numero):
    """
    La Funcion Compara Dos Valores Dados Por el Usuario,
    Devolviendo -1 Si El Primer Valor Es Menor Que El Segundo,
    1 Si EL Primer Valor Es Mayor Que El Segundo,
    y 0 Si Ambos Valores Son Iguales
    """        
    if numero < otro_numero:
        return -1
    if numero > otro_numero:
        return 1
    if numero == otro_numero:
        return 0
    
def prueba():
    numero = ingreso_entero("Ingrese un numero: ")
    otro_numero = ingreso_entero("Ingrese otro numero: ")    
    comparar = compara(numero, otro_numero)
    
    print (comparar)
    
if __name__ == "__main__":
    prueba()
