################
# Fede Trujillo - @FNT138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from random import randint
from tp4ej1 import ingreso_entero

def lista_random(cantidad, minimo, maximo):
    """
    La Funcion Genera Una Lista Con Valores random
    (obtenidos de random-->randint).
    Con La Cantidad De Valores Que El Usuario Desea y
    Entre los Limites Que el Quiera
    """
    milista = list()
    for i in range(cantidad):
        milista.append(randint(minimo, maximo))
    return milista

def num_minimo(lista):
    """
    La Funcion Devuelve El Menor Valor De Una Lista
    """
    minimo = lista[0]
    for i in lista:
        if (minimo > i):
            minimo = i
    return minimo

def num_maximo(lista):
    """
    La Funcion Devuelve El Mayor Valor De Una Lista
    """
    maximo = lista[0]
    for i in lista:
        if (maximo < i):
            maximo = i
    return maximo

def prueba():
    cantidad = ingreso_entero("Ingrese la cantidad de valores de la lista: ")
    minimo = ingreso_entero("Ingrese el valor minimo de la lista: ")
    maximo = ingreso_entero("Ingrese el valor maximo de la lista: ")    
    lista = lista_random(cantidad, minimo, maximo)    
    print(lista)
    
    menor = num_minimo(lista)
    print(f"El menor es: {menor}")
    
    mayor = num_maximo(lista)
    print(f"El mayor es: {mayor}")
    
if __name__ == "__main__":
    prueba()