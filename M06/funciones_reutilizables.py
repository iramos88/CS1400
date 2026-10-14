#Funciones Reutilizables
#Isaac Ramos. 
#Tarea M6
#Parte 1: Funciones sin retorno (Acciones directas)

def mostrar_bienvenida(Nombre):
    print(f"¡Hola, {Nombre}! Bienvenido a clase hoy.")

# PREGUNTAS:
# 1. En la función mostrar_bienvenida(nombre), ¿cómo se llama la variable "nombre" dentro de los paréntesis? 
# Respuesta. Ana
# 2. ¿Qué le falta al código para ser completamente reutilizable?
# Respuesta. Pienso que le faltaria la instruccion retur en lugar de solo mostrarlo con el print, al hacer 
# el texto procesado se podra reutilizar en cualquier contexto.

# =============================================================
# Parte 2: Funciones con retorno (Procesamiento de datos)
# =============================================================

def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

def es_par(numero):
    return numero % 2 == 0
# PREGUNTAS:
# 3. ¿Qué palabra clave (keyword) de Python se utiliza para indicar que estamos definiendo una función?
# Respuesta. La palabra clave es "def" con esto indicamos que estamos en una funcion.
# 4. Escribe los nombres de las dos funciones definidas arriba.
# Respuesta. calcular_descuento, es_par
# 5. ¿Qué sucede cuando llamas a la función pasando solo un argumento, como calcular_descuento(100)?
# Respuesta. si entiendo bien la funcion asigna automaticamente el valor asignado al porcentaje que en este 
# ejemplo es 10% de decuento sobre 100 y retorna 90.
# 6. ¿Qué ocurre si pasas dos argumentos, como calcular_descuento(200, 20)?
# Respuesta. En este caso sobreescribe el valor del segundo parametro asigna el 200 como precio y 20 como el porcentaje de esta manera
# pienso que hace el calculo de un 20% de descuento de 200 y retorna 160.

# =============================================================
# Parte 3: Pruebas de ejecución
# =============================================================

print("--- PRUEBA 1: Mostrar Bienvenida ---")
mostrar_bienvenida("Ana")
mostrar_bienvenida("Carlos")

print("\n--- PRUEBA 2: Cálculo de Descuentos ---")

compra_1 = calcular_descuento(100)
print(f"Precio con descuento por defecto: ${compra_1}")


compra_2 = calcular_descuento(200, 20)
print(f"Precio con 20% de descuento: ${compra_2}")

# PREGUNTAS:
# 7. Escribe el pseudocódigo de las funciones en la Parte 2.
"""
 #def calcular_descuento(precio, porcentaje=10):
    #descuento = precio * (porcentaje / 100)
    #precio_final = precio - descuento
    #return precio_final

 #def es_par(numero):
    #return numero % 2 == 0
"""
# 8. Explícale una de las dos a tu compañera(o) de al lado e incluye el propósito del programa. Tu compañera(o) te debe explicar lo siguiente. Lleguen a un acuerdo para agregar lo esencial como comentarios.
#  El proposito del programa es automatizar el calculo de precios aplicando un porcentaje de descuento.
# 9. Cambia las funciones para que acepten decimales en el precio.
# con el float nos aseguramos que el previo acepte decimales.
def calcular_descuento(precio, porcentaje =10):
    descuento = float(precio) * (porcentaje / 100)
    precio_final = float(precio) - descuento
    return precio_final

# =============================================================
# Parte 4: Alcance (Scope) y Retorno
# =============================================================

# La función mostrar_bienvenida() usa print(), mientras que calcular_descuento() usa return.
# Si asignas la llamada de la bienvenida a una variable:

resultado = mostrar_bienvenida("Julio")
print(resultado)
#print(descuento)

# PREGUNTAS:
# 10. ¿Qué valor se guarda en la variable 'resultado' y por qué?
#  Se guarda el valor none por la funcion mostrar bienvenida no tiene la instruccion
# return por lo que no devuelve ningun dato al ser llamada.
# 11. ¿Por qué es necesario usar return en calcular_descuento() para poder guardar el precio final en compra_1 y compra_2?
# esto nos permite sacar el resultado procesado fuera de la funcion
# 12. Intenta ejecutar la siguiente línea al final del documento: print(descuento) ¿Qué error muestra Python?
# NameError: name 'descuento' is not defined.
# 13. ¿Por qué la variable 'descuento' no es accesible fuera de la función?
# esto ocurre debido al scope local las variables que se crean dentro de la funcion solo existen mientras esta se ejecuta. 
# 14. ¿Qué ocurre si dentro de calcular_descuento cambias 'return precio_final' por 'print(precio_final)' e intentas sumar 'compra_1 + 5'?
# nos mostrara un TypeError, ya que "compra_1" almacenará "None" (porque la función 
# ya no retorna nada
# 15. Investiga: ¿Cómo podrías llamar a la función 'calcular_descuento' asignando el porcentaje mediante su nombre de parámetro (keyword argument)?
# compra_prueba = calcular_descuento(precio=150, porcentaje=15), en este caso se indica explicitamente el nombre del parametro seguido del valor. no importa el orden.
# 16. Añade un "docstring" (comentario multilínea con """) dentro de cada función para explicar brevemente qué hace.

"""
def mostrar_bienvenida(nombre):
nos muestra un mensaje de bienvenidad para cada estudiante
print (f"hola, {nombre}! bienvenido a la clase hoy.")

def calcular_descuento (precio, porcentaje=10):
calculando el precio final un porcentaje de descuento.
descuento = precio * (porcentaje / 100)
precio_final = precio - descuento
retur precio_final

def es par (numero):
verifica si un numero ingresado es par y devuelve true o false 
retur numero % 2 == 0

"""
