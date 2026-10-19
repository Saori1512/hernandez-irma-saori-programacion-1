## Nombre: Irma Saori Hernandez Salas
## Descripción: Consola que registra productos de Variedad
## Codigo de estudiante: 221144843

TASA_IVA = 0.16

print("Registro de compra en Freddy Fazbear's Pizza")

# Captura de datos del producto
Cantidad_de_productos = input("¿Cuántos productos desea registrar? ")

while not Cantidad_de_productos.isdigit() or int(Cantidad_de_productos) <= 0:
    print("Por favor, ingrese un número válido mayor que cero.")
    Cantidad_de_productos = input("¿Cuántos productos desea registrar? ")

    total_productos = int(Cantidad_de_productos)

    # lista de productos
    productos = []

    # Captura de datos de cada producto
    for number in range(1,total_productos): 
        print(f"\nProducto {numero} de {total_productos} ---")
        # No dejar que el usuario deje el nombre del producto vacío
        nombre_producto = input("Ingrese el nombre del producto: ").strip()