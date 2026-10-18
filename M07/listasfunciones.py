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