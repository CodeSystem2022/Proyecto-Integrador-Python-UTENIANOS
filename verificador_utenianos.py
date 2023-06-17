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

def validacionCantidadArticulos(cantidad):
    return cantidad > 0  # Validar que la cantidad de artículos sea mayor a 0

def validacionPrecioArticulo(precio):
    return precio > 0  # Validar que el precio del artículo sea mayor a 0

if __name__ == "__main__":
    menuIngresoDeCompras()  # Llamar a la función principal del programa

