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
    intentos = cantidad_reintentos
    
    while intentos > 0:
        try:
            return ingreso_entero(mensaje)
        except IngresoIncorrecto as err:            
            intentos = intentos -1            
    raise IngresoIncorrecto(f"Luego de {cantidad_reintentos} intentos")  
#RESTRINGE LOS VALORES A INGRESAR
def ingreso_entero_restringido(mensaje,valor_minimo, valor_maximo):
    if valor_minimo >= valor_maximo:
        """
        Intercambia los Valores Para que La Expresion Sea Valida
        """
#         try:
#             minimo = valor_minimo
#             valor_minimo= valor_maximo
#             valor_maximo = minimo
#             print("Se Intercambiaron Los Valores")
#         except ValueError as err:
        raise IngresoIncorrecto (f" '{valor_minimo}';'{valor_maximo}'"
                                 "No era un rango valido")
        
    msg = f"{mensaje}entre {valor_minimo} y {valor_maximo}"
    num = ingreso_entero(msg)
    
    if (num >= valor_minimo) and num <= valor_maximo:
        return num
    else:
        print (f"el ingreso no era un valor entre"
             "{valor_minimo} y {valor_maximo}")
        raise IngresoIncorrecto(msg) 
#INICIA LA FUNCION
def prueba():
    msg = ("Dame Un Numero ")
    
    num = ingreso_entero(msg)
    print(f"El numero es: #{num}")
    
    intentos = input(f" Cantidad de Intentos: #")    
    try:
        intentos = int(intentos)
    except ValueError as err:
        raise IngresoIncorrecto(f"'{intentos}'"
                "No era Un Valor Permitido") from err
    
    num = ingreso_entero_reintento(msg, intentos)
    print(f"El numero es: #{num}")        
    minimo = input(f"{msg} Para Valor Minimo: #")
    maximo = input(f"{msg} Para Valor Maximo: #")
    
    try:
        minimo = int(minimo)
        maximo = int(maximo)
    except ValueError as err:
        raise IngresoIncorrecto (f" '{minimo}' o '{maximo}' No era "
                                 "un Valor Permitido") from err
    
    num = ingreso_entero_restringido (msg, minimo, maximo)
    print(f"El numero es: #{num}")
    

if __name__ == "__main__":
    prueba()

