## Nombre: Irma Saori Hernandez Salas
## Descripción: Consola que registra productos de Variedad
## Codigo de estudiante: 221144843

TASA_IVA = 0.16

print("Registro de compra en Freddy Fazbear's Pizza")

# Captura de datos del producto
cantidad_texto = input("¿Cuántos productos desea registrar? ")
while not cantidad_texto.isdigit() or int(cantidad_texto) <= 0:
    print("Por favor, ingrese un número válido mayor que cero.")
    cantidad_texto = input("¿Cuántos productos desea registrar? ")

total_productos = int(cantidad_texto)
productos = []

# Captura de datos de cada producto
for numero in range(1, total_productos + 1):
    print(f"\nProducto {numero} de {total_productos} ---")

    nombre_producto = input("Ingrese el nombre del producto: ").strip()
    while not nombre_producto:
        print("El nombre no puede estar vacío.")
        nombre_producto = input("Ingrese el nombre del producto: ").strip()

    precio_producto = None
    while precio_producto is None:
        try:
            precio_ingresado = float(input("Ingrese el precio del producto: "))
            if precio_ingresado < 0:
                print("El precio no puede ser negativo. Intente nuevamente.")
            else:
                precio_producto = precio_ingresado
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")

    # Cantidad debe ser mayor que cero
    cantidad_producto = 0
    while cantidad_producto <= 0:
        entrada_cantidad = input("Ingrese la cantidad del producto: ")
        if entrada_cantidad.isdigit() and int(entrada_cantidad) > 0:
            cantidad_producto = int(entrada_cantidad)
        else:
            print("Error: La cantidad debe ser un número entero mayor que cero. Intente nuevamente.")

    subtotal = precio_producto * cantidad_producto
    productos.append((nombre_producto, precio_producto, cantidad_producto, subtotal))

subtotal_general = sum(producto[3] for producto in productos)
iva = subtotal_general * TASA_IVA
total_a_pagar = subtotal_general + iva

# Impresión final
ancho = 50
print("=" * ancho)
print("Recibo de compra en Freddy Fazbear's Pizza".center(ancho))
print("=" * ancho)
print(f"{'Producto':<22}{'Cant.':>6}{'Precio':>10}{'Subtotal':>12}")
print("-" * ancho)
for nombre, precio, cantidad, subtotal in productos:
    print(f"{nombre:<22}{cantidad:>6}{precio:>10.2f}{subtotal:>12.2f}")
print("-" * ancho)
print(f"{'Subtotal general:':<38}{subtotal_general:>12.2f}")
print(f"{'IVA (16%):':<38}{iva:>12.2f}")
print(f"{'Total a pagar:':<38}{total_a_pagar:>12.2f}")
print("=" * ancho)
