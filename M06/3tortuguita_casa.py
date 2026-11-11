# ==========================================
#Isaac Ramos
# TAREA Turtle 🐢
# ==========================================
# En esta actividad aprenderás a:
# 1. Mover la tortuga hacia adelante.
# 2. Girarla usando grados.
# 3. Dibujar un cuadrado.
# 4. Usar un bucle para repetir instrucciones.
#
# IMPORTANTE:
# - Un giro completo es de 360 grados.
# - Un cuadrado tiene 4 lados iguales.
# - Cada esquina de un cuadrado mide 90 grados.
#
# Completa todos los TODO.

# ------------------------------------------
# Importaciones necesarias
# ------------------------------------------

import turtle
# La siguiente linea agrega funciones para realizar la tarea en nuestro programa
#from turtle import make_turtle, forward, left


# ------------------------------------------
# Crear la ventana y la tortuga
# ------------------------------------------

# TODO 1
#  Iniciar ventana y objeto de tortuga y agregar el speed o velocidad. Pista: Mira la Tarea 1turtle.py

# Escribe aquí tu código
pantalla = turtle.Screen()
pantalla.bgcolor("lightgreen")
pantalla.title("Tortuga de Isaac")
#pantalla.setup(width=400, height=400)
tortuga = turtle.Turtle()
tortuga.speed(2)
# TODO 2
#  Crea la tortuga usando make_turtle().
tortuga = turtle.Turtle()
tortuga.shape("turtle")  # Puedes cambiar la forma de la tortuga si deseas
tortuga.color("orange")  # Color es opcional.

#  La ventana debe tener 400 de alto y 400 de ancho.

# Escribe aquí tu código
pantalla.setup(width=400, height=400)
# Captura de Pantalla, nombralo "TUNOMBRE_1_2" y guardalo en la carpeta M06

# ------------------------------------------
# Dibujar una línea
# ------------------------------------------

# TODO 3:
# Mueve la tortuga hacia adelante 100 pasos.
# Observa qué sucede.

# Escribe aquí tu código
tortuga.forward(100)
tortuga.left(90)  # Gira la tortuga 90 grados a la izquierda
# ------------------------------------------
# Girar la tortuga
# ------------------------------------------

# TODO 4:
# Gira la tortuga 90 grados hacia la izquierda.
# Luego avanza otros 100 pasos.

# Escribe aquí tu código
for _ in range(3):  # Repite 4 veces para completar el cuadrado
    tortuga.forward(100)
    tortuga.left(90)

# ------------------------------------------
# Dibujar un cuadrado 
# ------------------------------------------
# Un cuadrado tiene:
# - 4 lados
# - 4 giros de 90 grados

print("Dibujando un cuadrado...")

# TODO 5:
# Completa los movimientos necesarios
# para dibujar un cuadrado de lado 100.
# Debes usar forward() y left() varias veces.
# La tortuga debe terminar donde empezó.

# Escribe aquí tu código
for _ in range(1):  # Repite 4 veces para completar el cuadrado
    tortuga.forward(100)
    tortuga.left(90)

# ------------------------------------------
# Paso EXTRA (opcional)
# ------------------------------------------ aqui.....
# ¿Puedes agregar un triángulo? y un rectangulo? Dibuja una casita.

for _ in range(lados):
    tortuga.forward(tamaño)
    tortuga.left(angulo)

tortuga.end_fill()

for _ in range(2): 
    tortuga.forward(100)
    tortuga.left(90)
    tortuga.penup()
    tortuga.goto(-150, 0)
    tortuga.pendown()
# mover(-150, 0)
#dibujar_figura(lados=3, tamaño=80,
   # mover(-150, 0)
#dibujar_figura(lados=3, tamaño=80,
#color_borde="darkgreen", color_relleno="lightgreen")
# Pista:
# - Un triángulo tiene 3 lados.
# - Un giro completo es 360 grados.
# - ¿Cuánto debe girar en cada esquina?
#def dibujar_figura(lados, tamaño, color_borde, color_relleno):
# 

# Mantiene la ventana abierta hasta que hagas clic en ella
pantalla.exitonclick()