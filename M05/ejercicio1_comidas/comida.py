"""
Este programa debe darle al usuario la opción de elegir una comida de una lista.
El código asegura que lo ingresado sea legible (en minúsculas) y lo compara con una lista usando lógica if/else.
Al final, muestra un mensaje explicando de dónde es originaria esa comida.
"""

# TODO #1:
# Imprime un mensaje de bienvenida al programa de comidas de Latinoamérica.
print("Bienvenido al programa de comidas de Latinoamérica.")
# TODO #2:
#Declarando las 5 variables con 5 platos
# Muestra al usuario una lista de al menos 5 opciones de comidas para elegir.
print("Menu")
print("Arroz $15")
print("Lomo $18")
print("Ceviche $20")
print("Aji de Gallina $22")
print("Tallirenes verdes $21")

# TODO #3:
# Guarda lo que el usuario escribió en una variable llamada `comida`.
#Agrgando la variable comida con la funcion Lower
comida = input("¿que plato deseas?").lower()
#print(comida)
# TODO #4:
# Convierte lo ingresado a minúsculas para asegurar la comparación correcta.

# TODO #5:
# Usa una estructura if / elif / else para verificar la comida elegida.
# Imprime un mensaje con el país de origen para cada comida.
#Agregando las condifiones if, elif, 

if comida == "arroz con pollo":
    print("El mejor plato del dia.")
elif comida == "lomo saltado":
    print("Una buena decision.")
elif comida == "ceviche":
    print("El mejor del mundo.") 
elif comida == "aji de gallina":
    print("excelente.")
elif comida == "tallarines verdes":
    print("Great.")
else:
    print("No Tenemos ese plato")

## Ejemplo de salida esperada:
"""
Bienvenido al programa de comidas de Latinoamérica.
Opciones: tacos, arepas, ceviche, pupusas, empanadas
¿Qué comida quieres conocer? Tacos
Los tacos son típicos de México.
"""
