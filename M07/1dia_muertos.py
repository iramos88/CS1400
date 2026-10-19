"""Tarea 1: Preparando la Oferta (Listas y Tuplas)
#Isaac Ramos
"""

# Tarea 1: Lista de elementos para el altar de muertos

# Lista de ofrendas editables (pueden agregarse o quitarse elementos)
ofrendas = ["Pan de muerto", "Flor de cempasúchil", "Velas", "Calaverita de azúcar"]
ofrendas.append("Incienso copal")
ofrendas.sort()
print(ofrendas)
# Tupla con los niveles tradicionales del altar (constante, no debe cambiar)

NIVELES_ALTAR = ("Cielo", "Tierra", "Inframundo")
#NIVELES_ALTAR[0] = "Gloria"  # Esto generará un error porque las tuplas son inmutables

# Mostrar la segunda ofrenda (índice 1)
print("Segunda ofrenda:", ofrendas[1])

for posicion, ofrenda in enumerate(ofrendas):
    print(f"{posicion}: {ofrenda}")
"""
Ejecuta el código. Observa qué elemento se imprime al pedir el índice 1.
R: Al pedir el indice 1 ejecuta la segunda opción de la lista, en esta caso es la flor de cempasuchil.
#1. Modificación 1 (Listas): Agrega un nuevo elemento a la lista ofrendas usando
 .append("Incienso copal") y luego ordena la lista alfabéticamente usando
 la función .sort().  ¿Qué notas del variable en linea #12?
R: se agrego el elemento "Incienso copal" con la funcion append que al hacer esto la nueva variable al ejecutar se vera en la ultima posicion de la lista,
pero al usar la funcion sort() se ordena alfabeticamente y se muestra en la segunda posicion de la lista. 

#2. Modificación 2 (Tuplas): Intenta modificar el primer elemento de la tupla escribiendo
 NIVELES_ALTAR[0] = "Gloria".
 ¿Qué sucede al ejecutar el código y por qué no permite realizar este cambio?
R: Al ejecutar el codigo se genera un error, ya que las tuplas son inmutables y no se pueden modificar una vez creadas.

#3. Utiliza la función enumerate() dentro de un bucle for para imprimir cada ofrenda
 de tu lista junto con su número de posición en el altar.

0: Calaverita de azúcar
1: Flor de cempasúchil
2: Incienso copal
3: Pan de muerto
4: Velas

"""

