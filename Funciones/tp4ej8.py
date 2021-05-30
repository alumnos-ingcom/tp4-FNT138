################
# Fede Trujillo - @FNT138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Ordena Una lista De 3 numeros de menor a mayor
    """
    if uno < dos: 
        if dos < tres:
            return uno,dos,tres
        else:
            if uno < tres:
                return uno,tres,dos
            else:
                return tres,uno,dos
    else:
        if uno < tres:
            return dos,uno,tres
        else:
            if dos < tres:
                return dos,tres,uno
            else:
                return tres,dos,uno
        
        
def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Ordena Una lista De 3 numeros de mayor a menor
    """
    if uno > dos:
        if dos > tres:
            return uno,dos,tres
        else:
            if uno > tres:
                return uno,tres,dos
            else:
                return tres,uno,dos
    else:
        if uno > tres:
            return dos,uno,tres
        else:
            if dos > tres:
                return dos,tres,uno
            else:
                return tres,dos,uno

def prueba():
    uno = ingreso_entero("Ingrese un numero: ")
    dos = ingreso_entero("Ingrese otro numero: ")
    tres = ingreso_entero("Ingrese otro numero: ")
    
    menor_a_mayor = ordenar_menor_a_mayor(uno, dos, tres)
    mayor_a_menor = ordenar_mayor_a_menor(uno, dos, tres)
    
    print(f"Menor a mayor {menor_a_mayor}")
    print(f"Mayor a menor {mayor_a_menor}")
    
if __name__ == "__main__":
    prueba()