################
# Federico Trujillo - @FNT138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def factores_primos(numero):
    """
    La Funcion Imprime Los Factores Primos De El Numero
    Ingresado Por El Usuario
    """    
    factor = 2 #establece el factor en 2 ya que es el primer N primo
    factores = list() #Crea una lista para guardar los valores de factor
    
    while factor <= numero:
        if (numero % factor == 0):
            numero = numero/factor
            factores.append(factor)        
        else:
            factor = factor+1
    return factores

def prueba():
    factor = ingreso_entero("Ingrese un numero:")
    num = factores_primos(factor)
    
    print(num)

if __name__ == "__main__":
    prueba()