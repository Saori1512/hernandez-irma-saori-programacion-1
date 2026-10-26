## Irma Saori Hernandez Salas
## Codigo de estudiante: 221144843

## Ejercicio 1: clasificar la edad del usuario :3

edad = int(input("¡Hola! Por favor, ingresa tu edad owo: "))
if edad < 13:
    print("Eres un niño.")  
elif edad < 18:  
    print("Eres adolescente.")
else:
    print("Eres adulto.")
    

## Ejercicio 2: :Validar acceso (usuario y contraseña) O.O

Usuario = input("Ingrese su nombre de usuario: ")
Contraseña = input("Ingrese su contraseña: ")
if Usuario == "admin" and Contraseña == "123456":
    print("Acceso concedido. ¡Bienvenido!")
elif Usuario == "admin":
    print("Acceso denegado. Contraseña incorrecta.")
else:   
    print("Acceso denegado. Usuario o contraseña incorrectos.")

## Ejercicio 3: Calculadora de envío D:

input("Hoy Freddy Fazbear's Pizza tiene un descuento de 10% en los productos que superen los 10kg de peso. agrega el pruducto")
peso = int(input("Ingrese el peso del producto en kg para calcular el costo de envío: "))
if peso == 1:
    print("El costo de envío es de $50 fazpesos.")
elif peso <= 5:
    print("El costo de envío es de $90 fazpesos.")