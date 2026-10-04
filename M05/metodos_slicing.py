#isaac ramos 02/10/2026
# Conteo descendente
##num = int(input("Introduce el número inicial: "))

#¿Por qué es necesario que el parámetro step (paso) sea un número negativo al realizar un conteo descendente?
#Al poner el parametro step sea un numero negativo en una funcion range para hacer un conteo descendente.
#for i in range(num, 0, -1):
   # print("Conteo:", i)


#Al ingresar el numero comienza a contar de forma descendente
# es decir comienza con 10 y termina en el numero 1
# Inicio: _10_ | Fin: _1_    
#Cambiando el codigo para que pueda decender de 2 en 2
#Respuesta: range( ___num____ , __-1_____ , ___-2____ )
#num indica el numero que ingresa el usuario
#-1 (fin) es indica que debe detenerse justo antes de el -1
#-2 (paso) significa que el conteo va ir hacia atras de 2 en 2
##for i in range(num, -1, -4): 
 ##print("Conteo:", i)

"""
import math

decNum = -34.5678
intNum = 9

print( round(decNum, 2) )   # Línea A
print( round(decNum, 0) )   # Línea B
print( int(decNum) )        # Línea C
print( abs(decNum) )        # Línea D

print( math.pow(intNum, 2) ) # Línea E
print( math.sqrt(intNum) )   # Línea F
"""
# Linea A  -34.57
# Linea B  -35.0
# Linea C  -34 Redondea
# Linea D  34.5678
# Linea E   81.0
# Linea F  3.0
"""
miMax = max("Banano", "manzana", "Zanahoria")
print("El máximo es:", miMax)
"""
# 11. Antes de ejecutar: ¿Cuál crees que será el resultado devuelto por max()?
#Predicción: _Zanahoria_____
# 12. Ejecuta el código. ¿Cuál fue el resultado real devuelto?
#Resultado: ________Manzana____________
#Explicacion; En el la tabla de ASCII las caracteres en mayusculas tiene valores numericos menores que las minusculas es por eso que al 
#ejecutar el programa el resultado me da manzana que que el caracter de inoicio es mayor.


# 14. Cambia la función de max() a min(). ¿Qué valor obtienes ahora y por qué?
#Resultado: __Banano________
"""
miMax = min("Banano", "manzana", "Zanahoria")
print("El máximo es:", miMax)
"""
"""
import math

d = int(input("Ingresa la longitud de la huella de frenado (en metros): "))

# Completa la ecuación usando math.sqrt():
v = math.sqrt(20 * d)

print("Velocidad estimada del auto:", round(v, 2), "km/h")

# 15. Completa la asignación v = en el código superior utilizando la función math.sqrt() y la fórmula entregada. Escribe la línea completa a continuación:
#Respuesta: v = ___ math.sqrt(20 * d)_

#Sección 5: Segmentación de Cadenas (Slicing)
nombre = "Building Puentes"
print("Índice 0:", nombre[0])
print("Segmento:", nombre[8:15])
#print("Índice 0:", nombre[9])
#print("Segmento:", nombre[9:16])

# 16. ¿Qué carácter imprime exactamente nombre[0]? _P______
# 17. ¿En qué posición (índice) exacta se encuentra el espacio en blanco entre ambas palabras? __7
#Modifica los índices en nombre[X:Y] para extraer e imprimir exactamente la palabra "Puentes".

#Opción con 2 valores: nombre[ __9__ : 16___ ]
#Opción con límite implícito: nombre[ ___9_ : ]
"""
"""
texto = input("Ingresa una frase con letras y números: ")
contador_numeros = 0

for caracter in texto:
    if caracter >= "0" and caracter <= "9":
        contador_numeros += 1

print("Total de dígitos numéricos encontrados:", contador_numeros)
"""
# 19. Ejecuta el programa e ingresa el texto "3 tigres en 2 árboles". ¿Qué valor imprime contador_numeros? _2_
#la condicion if compara los caractares bsandose en la tabla ASCII

#Seccion 7

#Método .rfind('a'):
# busca el caracter especifico ('a') dentro de una cadena
# Método .isalpha():#
# Devuelve True únicamente si la cadena no está vacía y todos sus caracteres son letras; si contiene números, espacios o símbolos especiales, devuelve False.
# Método .isdigit():
# Verifica o se asegura que todos los caracteres de la cadena
# son digitos numericos.