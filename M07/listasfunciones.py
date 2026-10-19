# Manejo de textos y listas
"""
mensaje = "bienvenido al curso de python"
comidas = ["aji de gallina", "ceviche", "lomo saltado "]

# Mostrar datos
print(mensaje)
print(comidas[1])

# Ejemplo de modificación:
print(mensaje.upper())
"""
"""
Cambia el índice dentro del corchete comidas[0] para mostrar en pantalla la segunda comida de tu lista. ¿Qué número de índice tuviste que utilizar y por qué?
R.Hice el cambio por el 1, normalmente phyton empieza a contar desde la posicion 0, al poner 1 empieza a contar desde el segundo elemento en este caso seria "pizza"
Modifica la lista comidas para que incluya tres de tus alimentos favoritos reales y vuelve a imprimir únicamente la segunda opción.
R.
Observa las opciones y complete las definiciones. Métodos disponibles: insert, append, remove, pop y clear.
R.
¿Qué método elimina todos los elementos de la lista? RESPUESTA: _Clear___

¿Qué método elimina un elemento de la lista por su valor de índice? RESPUESTA: _Remove_

¿Qué método elimina un elemento de la lista usando el valor del elemento? RESPUESTA: _pop_

¿Qué método agrega un elemento al final de la lista? RESPUESTA:  append_

¿Qué método agrega un elemento en una ubicación específica? RESPUESTA:  _insert__


"""
#codigo 1

playerNames = ["Adam", "Bethanie", "Carrie", "Doug", "Eddie"]
playerNumbers = [5, 2, 6, 13, 0]

# 1. Adam ha dejado el equipo. Use 'remove' para eliminarlo:
playerNames.remove("Adam")
# 2. Elimine el primer número de la lista (5) usando 'pop':
playerNumbers.pop(0)
# 3. Use 'append' para agregar estas variables a sus listas:
playerNames.append("Lucas")
playerNumbers.append(7)


# 4. Use 'insert' para que "Raven" (número 1) sea la primera en la lista:
playerNames.insert(0, "Raven")

print(playerNames)
print(playerNumbers)
"""

#Contadores y Iteradores.
"""
import random

def Generate_Numbers():
    numbers = []
    for i in range(20):
        num = random.randint(1, 50)
        numbers.append(num)
    return numbers

# Llamada a la función
mis_numeros = Generate_Numbers()

print("Numeros genrados:", mis_numeros)

¿Qué tipo de datos se está agregando a la lista numbers? 
RESPUESTA: _Entero_

¿Cuántos números se están agregando exactamente a la lista? 
RESPUESTA: __20 numeros es el rango__

¿Qué devuelve (return) la función al final de su ejecución?
 RESPUESTA: _Devuelve todos los numeros al ejecutarse el sistema.__


#DESAFÍO DE CÓDIGO 2:

def Even_Numbers(lista_origen):
    even = []
    for num in lista_origen:
        if num % 2 ==0:
            even.append(num)
    return even
# TODO: Itere la lista_origen y agregue a 'even' solo los números pares
print(Even_Numbers([1, 2, 3, 4, 5, 6])) 

def Ten_Or_Less(lista_origen):
    # TODO: Cree una lista vacía, busque valores <= 10 y devuélvala
    #ten_or_less = []
    resultado = []
    for num in lista_origen:
        if num <= 10:
            resultado.append(num)
           # ten_or_less.append(num)
    return resultado
#print(Ten_Or_Less([5, 12, 8, 20, 3]))


def Calcular_Diferencias(lista_origen):
    # TODO: Calcule la distancia entre números consecutivos
    diferencias = []
    for i in range(len(lista_origen) - 1):
        diferencia = abs(lista_origen[i] - lista_origen[i + 1])
        diferencias.append(diferencia)
    # Ejemplo: [10, 7, 15] -> [3, 8]
    return diferencias
#print(Calcular_Diferencias([10, 7, 15]))

mis_numeros = Generate_Numbers()
print("Lista original de 20 números:", mis_numeros)
print("Números menores o iguales a 10:", Ten_Or_Less(mis_numeros))
print("Números pares:", Even_Numbers(mis_numeros))
print("Diferencias consecutivas:", Calcular_Diferencias(mis_numeros))
"""
#DESAFÍO DE CÓDIGO 3:

#Observa la siguiente matriz 2D que representa un tablero de Tic-Tac-Toe:

#Python
tictactoe = [
    ["X", "X", "X"],
    ["-", "O", "-"],
    ["O", "-", "-"]
]

# Escriba el 'if' para detectar si la fila superior (índice 0) tiene tres "X":
if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X":
    print(tictactoe[0][0], tictactoe[0][1], tictactoe[0][2])
    print('eres el ganador')
# Pista: Debe revisar las posiciones [0][0], [0][1] y [0][2]

#¿Qué valor devolvería la instrucción tictactoe[1][1] en el tablero anterior? RESPUESTA: ______0__
#¿Para qué sirve un print() vacío que se coloca al final de un bucle que imprime una matriz? RESPUESTA:
#R: Para hacer un salto de línea en la consola (permite que cada fila se imprima de forma separada y ordenada).


