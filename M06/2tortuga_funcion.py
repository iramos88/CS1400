"""
====================================================================
Mi Primera Función en Turtle
====================================================================
NOMBRE: Isaac Ramos
FECHA: 26/10/2026
Objetivo:
Entender cómo encapsular código en una función para reutilizarlo y 
dibujar figuras personalizadas de manera sencilla.

Corre este programa y toma captura del resultado
====================================================================
"""

import turtle

# ==================================================================
# 1. Configuración de la Pantalla y Tortuga
# ==================================================================
pantalla = turtle.Screen()
pantalla.bgcolor("lightyellow")
pantalla.title("Funciones y Figuras")

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)


# ==================================================================
# 2. DEFINICIÓN DE LA FUNCIÓN
# ==================================================================

# Función para 
def dibujar_figura(lados, tamaño, color_borde, color_relleno):
    """
    Dibuja cualquier polígono regular basado en el número de lados.
    
    Parámetros:
    - lados: Número de lados que tendrá la figura (ej. 3 para triángulo, 5 para pentágono).
    - tamaño: Longitud de cada lado en píxeles.
    - color_borde: Color de las líneas.
    - color_relleno: Color del interior de la figura.
    """
    
    # La suma de los ángulos exteriores de cualquier polígono es 360 grados.
    angulo = 360 / lados

    # Configuración de colores
    t.color(color_borde, color_relleno)
    t.begin_fill()

    # Un bucle 'for' que repita el avance y el giro 'lados' veces.
    for _ in range(lados):
        t.forward(tamaño)
        t.left(angulo)

    t.end_fill()


# Función auxiliar para 
def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# ==================================================================
# 3. DEMOSTRACIÓN / PRUEBAS (Demuestra el poder de la función)
# ==================================================================

# Dibujar una estrella/triángulo (3 lados)
mover(-150, 0)
dibujar_figura(lados=3, tamaño=80, color_borde="darkgreen", color_relleno="lightgreen")

# Dibujar un pentágono (5 lados)
mover(0, 0)
dibujar_figura(lados=5, tamaño=60, color_borde="purple", color_relleno="plum")

# Dibujar un hexágono (6 lados)
mover(150, 0)
dibujar_figura(lados=6, tamaño=50, color_borde="darkblue", color_relleno="skyblue")

#Dibujar un octagono (8 Lados)
mover(-150, -100)
dibujar_figura(lados=8, tamaño=30, color_borde="darkred", color_relleno="lightcoral")

#Nueva figura cuadrada sin el uso de la funcion dibujar_figura

mover(50, -100)
t.color("orange", "yellow")
t.begin_fill()

for _ in range(4):
    t.forward()
    t.left(90)
t.end_fill()

# ==================================================================
# 4. PREGUNTAS
# ==================================================================
"""
1.  ¿Cuantas funciones hay en este programa? Que proposito tienen? En tus propias palabras agrega comentario completo.
 En este programa hay dos funciones principales, la primera es la funcion dibujar_figura, que la funcion principal es dibujar cualquier poligono,
 La segunda funcion es mover, que su proposito es mover la tortuga a una posicion especifica sin dibujar, para poder dibujar otras figuras.
2.  ¿Qué parámetro de la función 'dibujar_figura' tendrías que cambiar para hacer un octágono (8 lados)?
 Para hacer un octágono, tendrías que cambiar el parámetro 'lados' a 8., se hara un ejemplo de un octagono para ver si funciona correctamente.
3 ¿En que numero de linea termina la funcion mover?
Con el ejemplo que agregue del octagono terminara en la linea 84.

4. Bajo la seccion de pruebas, intenta hacer una nueva figura sin el uso de la funcion dibujar_figura.

5. Guarda una captura de pantalla con las 4 figuras en la carpeta M06.
      
"""


pantalla.exitonclick()