################
# Federico Trujillo - @FNT138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def es_palindromo(texto):
    """
    La Funcion Indica Si Una expresion Ingresada Por El Usuario Es
    Un Palindromo o No
    """   
    texto = str(texto).upper()
    
    if texto == texto[::-1]:
        return True
    else:
        return False
        
def prueba():
    palabra = str(input("Ingrese una palabra: "))
    ej = es_palindromo(palabra)
    
    print(ej)

if __name__ == "__main__":
    prueba()