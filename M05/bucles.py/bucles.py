#Isaac Ramos

#Analiza el siguiente código para comprender la necesidad de los bucles.

#Código 1:

# Impresión manual repetitiva
"""
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
"""
# 1. Si quisieras saludar a 100 estudiantes, ¿qué problema presenta el enfoque mostrado en el Código 1?
#Si quisiera saludar a 100 alumnos y sigo la secuencia de la linea del primer codigo tendria que repitir el 
#print 100 veces.

# 2. el codigo escrito de forma secuencial es estatico  eso quiere decir que el programa se ejecuta
#tal cual fueron escritas antes de correr el programa.

#Codigo2
# Intento de repetición con if
"""
respuesta = input("¿Deseas repetir el proceso? (si/no): ")
while respuesta == "si":
#if respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")
"""
# Ejecuta el programa e introduce "si" en la primera pregunta y "si" en la segunda. ¿El programa preguntó una tercera vez o finalizó?
# El programa finalizó y no preguntó una tercera vez. Esto sucede porque una estructura condicional 'if' evalúa la condición una sola vez
# Al reemplazar la condicion IF por while el proceso se repite consecutivamente

#¿Es posible saber con exactitud de antemano cuántas veces el usuario escribirá "si" antes de ejecutar el programa?
#No es posible saberlo debido a que depende del usuario en el tiempo de ejecucion.
# Al usar un while se produce un bucle Infinito.
# Respuesta ctrl+c

#Código 3:
#Python
# Ejemplo de range() simple
"""
num = int(input("Introduce un número límite: "))

for i in range (2, 11, 2):
#for i in range (1 , num + 1):
#for i in range (1 , num):
#for i in range (0,10):
#for i in range(10):
    print("Iteración:", i)
"""
# 8 Respuesta: La palabra "Iteración" se imprimió 10 veces (del 0 al 9)
# 9. Observa la salida numéricas de i. ¿Cuál es el valor inicial y cuál es el valor final impreso?

#Valor inicial: 0
#Valor final: 9
# 10. ¿Se llegó a imprimir el número 10 en la consola? Explica por qué Python excluye el límite superior en range().
# Respuest. En phyton no incluye el numero 10 en el programa debido a que le estamos pidiendo que nos muestra el rango
# de 10, es decir que phyton tomara el primer digito el 0 haasta el 9 ahi te genera 10 numeros.
# 11. Cambia range(10) por range(0, 10). ¿Existe alguna diferencia en el resultado obtenido?
# no cambia en nada ejecuta el mismo patron.

# Modificación 2A (Rango con Variable Límite):

# Cambia la línea del rango para usar la variable num: range(1, num).

# 12 Respuesta. el conteo se detiene en 19
# 13 Respuesta. (1 , num + 1):
# 14 Respuesta. Los valores que se imprimieron fueron 2,4,6,8,10

# Código 4:

# Iteración sobre una cadena de texto
"""
palabra = "Python"

print("--- Letras de la palabra ---")
for letra in palabra:
    print(letra)

# Iteración sobre una lista
frutas = ["manzana", "banana", "cereza"]

print("--- Lista de frutas ---")
for fruta in frutas:
    print(fruta)
"""
# 15 Respuesta. La variable 'letra' 
# representa un carácter individual de la cadena de texto en cada iteración.
# 16 Respuesta. La iteración directa (for fruta in frutas:) resulta mucho más legible para poder aprenderlo.
# 
# Código 5:
# Uso de break y continue
"""
print("Demostración de continue:")
for num in range(1, 6):
    if num == 3:
        continue
    print("Número:", num)

print("\nDemostración de break:")
for num in range(1, 6):
    if num == 3:
        break
    print("Número:", num)
"""
# 17 Respuesta. Falta el numero 3 en la demostracion continua
# El bloque de código contenía una estructura condicional (como un if (i == 3)).
# Al cumplirse esa condición, se ejecutó la instrucción continue.
# Esta sentencia interrumpe inmediatamente la iteración actual del bucle y salta directamente a la siguiente.

# 18 Respuesta. 1 , 2
# La instrucción break sirve para finalizar e interrumpir por completo la ejecución del bucle
# 19 Respuesta Break

# Código 6:
# Acumulador de suma y contador de coincidencias
"""
numeros = [4, 7, 2, 9, 10, 5]
suma_total = 0
mayores_a_cinco = 0

for num in numeros:
    suma_total += num  # Acumula la suma
    if num > 5:
        mayores_a_cinco += 1  # Incrementa el contador

print("Suma total:", suma_total)
print("Cantidad de números mayores a 5:", mayores_a_cinco)
"""
# 20 Respuesta.Debe Empezar en 0 (cero), ya que es el elemento neutro de la suma y acumulará los valores.
# 21 Respuesta. 
# (CONTADOR) Siempre aumenta en una cantidad fija (generalmente 1).
# (ACUMULADOR) Aumenta en una cantidad variable

# Sección 7. 
sujeto1 = "Python"
sujeto2 = "python"
if sujeto1.lower() == sujeto2.lower():
#if sujeto1 == sujeto2:
    print("Iguales")
else:
    print("Diferentes")

# Cuál es la diferencia visual entre ambos textos y cuál es el resultado de la comparación inicial?
# 22 Respuesta. que sujeto 1 la primera letra esta en mayuscula y sujeto 2 la primera letra en minuscula
# 23 Respuesta. al modificar la condicion con el lower, al ejecutar el programa
# el resultado es igual ya que lo convierte automaticamente en minuscula y esto hace que sean iguales.
# 24 Respuesta. Es útil porque evita errores lógicos o fallas en el flujo del programa.