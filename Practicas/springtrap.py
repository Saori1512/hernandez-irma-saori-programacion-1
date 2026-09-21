# Traducción de una porción del proyecto Springtrap de Scratch a Python

vida = 50
puntos = 0
x = 0
y = -145

print("Vida:", vida)
print("Puntos:", puntos)
print("Posición inicial:", x, y)

while True:
    tecla = input("Presiona A para izquierda, D para derecha o Q para salir: ").lower()

    if tecla == "d":
        x += 8
    elif tecla == "a":
        x -= 8
    elif tecla == "q":
        break

    print("Posición X:", x)

print("Programa terminado.")
