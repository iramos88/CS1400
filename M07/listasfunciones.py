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


