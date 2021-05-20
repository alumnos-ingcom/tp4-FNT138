################
# Federico Trujillo - @FNT138
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################




#EXCEPCION
class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

#INGRESO DE VALORES ENTEROS
def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto(f"'{ingreso}' no era un número!") from err
    return entero



#REINTENTA EL INGRESO DE VALORES DESP DE VALORES INCORRECTOS
def ingreso_entero_reintento(mensaje, cantidad_reintentos):
    cantidad_reintentos = int(input("Ingrese la cantidad de reintentos"))
    intentos = cantidad_reintentos
    
    while intentos > 0:
        try:
            return ingreso_entero(mensaje)
        except IngresoIncorrecto as err:            
            intentos = intentos -1
            
    raise IngresoIncorrecto(f"Luego de {cantidad_reintentos} intentos")  

#RESTRINGE LOS VALORES A INGRESAR
def ingreso_entero_restringido(mensaje,valor_minimo, valor_maximo):    
    print("Establezca los limites")
    valor_minimo = int(input("Valor minimo Permitido: # "))
    valor_maximo = int(input("Valor maximo Permitido: # "))    
    msg = f"{mensaje} entre {valor_minimo} y {valor_maximo}"
    num = ingreso_entero(msg)
    
    if (num >= valor_minimo) and num <= valor_maximo:
        return num
    else:
        print (f"el ingreso no era un valor entre"
             "{valor_minimo} y {valor_maximo}")
        raise IngresoIncorrecto(msg)
    
    
#INICIA LA FUNCION
def prueba():
    msg = ("Dame Un Numero: ")
    
    num = ingreso_entero(msg)
    print(f"El numero es: #{num}")
    
    num = ingreso_entero_reintento(msg, 0)
    print(f"El numero es: #{num}")
    
    num = ingreso_entero_restringido (msg, 0, 0)
    print(f"El numero es: #{num}")
    

if __name__ == "__main__":
    prueba()

