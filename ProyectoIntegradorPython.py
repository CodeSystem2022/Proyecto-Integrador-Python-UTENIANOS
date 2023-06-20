



----------------------------------COSTILLA CELINA-----------------------------------------------------------------------------------------
Parte 2: Menú de confirmación y descuentos

CODIGO:

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
