#---------------------------------PUTRINO AGUSTIN----------------------------------------
#Parte 1: Menú de ingreso de compras y verificiacion de cantidad 

import sys

def menuIngresoDeCompras():
    calculoCompra = 0
    cantidadArticulos = 0
    i = 0
    precioUnitario = 0
    validarCantidad = False
    validarPrecio = False

    print("\n       <<<<<<<< DETALLE DEL TOTAL DE TU COMPRA >>>>>>>>>  \n")
    while not validarCantidad:
        try:
            cantidadArticulos = int(input("  * CANTIDAD DE ARTÍCULOS QUE LLEVAS: "))
            validarCantidad = validacionCantidadArticulos(cantidadArticulos)  # Validar la cantidad de artículos ingresada
        except ValueError:
            print("__________________________________")
            print("    ERROR: CANTIDAD NO VÁLIDA")
            print("__________________________________\n")

    i = 0
    calculoCompra = 0

    while i != cantidadArticulos:
        try:
            precioUnitario = float(input(f"  * PRECIO DEL ARTÍCULO {i+1}°: "))
            validarPrecio = validacionPrecioArticulo(precioUnitario)  # Validar el precio del artículo ingresado
        except ValueError:
            print("__________________________________")
            print("      ERROR: PRECIO NO VÁLIDO")
            print("__________________________________\n")
        
        if validarPrecio:
            calculoCompra += precioUnitario
            i += 1

    print("____________________________________________________")
    print(f"   EL IMPORTE TOTAL DE TU COMPRA ES ${calculoCompra}")
    print("____________________________________________________")

    menuDeConfirmacion(calculoCompra)  # Llamar a la función del menú de confirmación

#----------------------------------COSTILLA CELINA-----------------------------------------------
#Parte 2: Menú de confirmación y descuentos

#CODIGO:

def menuDeConfirmacion(calculoCompra):
    opcionDeseada = 0

    while opcionDeseada != 1 and opcionDeseada != 2 and opcionDeseada != 3:
        try:
            print("__________________")
            print("     VERIFICAR SI TU COMPRA TIENE DESCUENTO")
            print("               INGRESA UNA OPCIÓN       ")
            print("__________________\n")
            print(" 1) IR A PANTALLA DE DESCUENTOS. 2) VOLVER AL MENÚ DE COMPRAS. 3) SALIR DEL PROGRAMA")
            opcionDeseada = int(input())
        except ValueError:
            continue

        if opcionDeseada == 1:
            menuDescuento(calculoCompra)
        elif opcionDeseada == 2:
            menuIngresoDeCompras()
        elif opcionDeseada == 3:
            print("__________________")
            print("            GRACIAS POR UTILIZAR EL PROGRAMA")
            print("__________________\n")
            sys.exit()

def menuDescuento(calculoCompra):
    opcionDia = 0

    print("__________________")
    print("        VERIFICADOR DE DESCUENTO SEMANAL       ")
    print("__________________")
    while opcionDia < 1 or opcionDia > 7:
        try:
            print("SELECCIONA QUÉ DÍA ES HOY PARA VER LOS DESCUENTOS:\n")
            print(" 1) LUNES. 2) MARTES. 3) MIÉRCOLES. 4) JUEVES. 5) VIERNES.")
            print(" 6) SÁBADO. 7) DOMINGO.")
            opcionDia = int(input())
        except ValueError:
            continue

    if opcionDia >= 1 and opcionDia <= 4:
        calcularDescuento(calculoCompra, 10)
    elif opcionDia == 5:
        calcularDescuento(calculoCompra, 20)
    elif opcionDia == 6 or opcionDia == 7:
        calcularDescuento(calculoCompra, 30)

def calcularDescuento(calculoCompra, porcentajeDescuento):
    descuento = (calculoCompra * porcentajeDescuento) / 100
    totalConDescuento = calculoCompra - descuento

    print("__________________")
    print(f"     EL TOTAL DE TU COMPRA ES ${calculoCompra}")
    print(f"          DESCUENTO DEL {porcentajeDescuento}%: ${descuento}")
    print(f"      TOTAL A PAGAR: ${totalConDescuento}")
    print("__________________\n")

    menuDeConfirmacion(calculoCompra)

if _name_ == "_main_":
    menuDeConfirmacion(calculoCompra)
    
#------------------AGUSTIN SABA------------------
#Parte 3: Función principal y punto de entrada:

def validacionCantidadArticulos(cantidad):
    return cantidad > 0  # Validar que la cantidad de artículos sea mayor a 0

def validacionPrecioArticulo(precio):
    return precio > 0  # Validar que el precio del artículo sea mayor a 0

from menu_compras import menuIngresoDeCompras

if _name_ == "_main_":
    menuIngresoDeCompras()
