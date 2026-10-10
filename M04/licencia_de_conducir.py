
"""
TODO
Crea un programa interactivo que evalúe si una persona mayor de edad está en
condiciones de conducir. Usa como referencia lo visto en la M3 Tarea de Sentencias.
Requisitos:
Entrada de datos: Solicita la edad del usuario y al menos 2 o 3 condiciones
 adicionales.
Sentencias de control: Usa estructuras condicionales (if, else if, else)
 y operadores lógicos (AND, OR, NOT) para evaluar la combinación de datos.
Salida clara: Muestra un mensaje personalizado indicando si la persona puede
 conducir o si debe entregar las llaves inmediatamente.
¡Usa tu creatividad! 
 Piensa en situaciones cómicas o extremas de la vida real.
   ¿Qué imprudencia o descuido no le permitirías a tu abuela antes de subirse al auto?
     (Ejemplo: "¿Olvidó los lentes en la cocina?")
"""
#Isaac Ramos
#Evaluacion de examen teorico para obtner licencia de conducir
"""
test = int (input("que puntaje obtuviste? (0 - 100): "))
asistencia = input("¿Asististe a las clases de manejo? (si/no): ").strip().lower()
tiene_multas = input("¿Tienes multas de tránsito sin pagar? (si/no): ").strip().lower()
#int(input (" que porcentaje obtuvite "))

#convertimos las respuestas a booleanos

asistio_clases = (asistencia == "si")
multas_pendientes = (tiene_multas == "si")

if test >= 80 and asistio_clases and not multas_pendientes:
  print(" fantastico Licencia aprobada, obtuviste un puntaje alto aprobaste podrar obtner tu licencia ")

elif test >= 70 or (asistio_clases and not multas_pendientes):  
  print("Aprobaste el test obtendras tu licencia")
elif not (asistio_clases and multas_pendientes):
  print("Denegado: no asististe a clases y tambien tienes multas pendientes, no podras conducir")
else:
  print ("No cumples con el puntaje minimo ") 
#elif test >= 50:
 # print("Desaprobaste el test no alcansaste al puntaje minimo intentalo en otra oportunidad")
"""
 #Isaac Ramos
# 1. Solicitar y validar la edad (mayor de 18 años)
edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Lo sentimos, tiene que ser mayor de 18 años para tramitar la licencia.")
else:
    # Haremos la Solicitud del puntaje del examen teórico
    # Ingresaremos la variable puntaje examen que sera float, el float hara que el resultado sea entero o decimal
    puntaje_examen = float(input("Ingrese su puntaje en el examen teórico (0-100): "))
    
    # 3. Solicitar asistencia a clases (s/n)
    asistio_input = input("¿Asistió a todas las clases obligatorias? (s/n): ").strip().lower()
    asistio_clases = True if asistio_input == 's' else False

    # 4. Solicitar multas pendientes (s/n)
    multas_input = input("¿Tiene multas de tránsito pendientes? (s/n): ").strip().lower()
    multas_pendientes = True if multas_input == 's' else False

    print("\n--- Resultado de la Evaluación ---")

    # 5. Lógica de evaluación con if-elif-else simplificada
    if puntaje_examen < 70:
        print("No aprobado: Su puntaje en el examen es inferior a 70.")
    elif not asistio_clases:
        print("No aprobado: No cumplió con la asistencia a las clases obligatorias.")
    elif multas_pendientes:
        print("No aprobado: Tiene multas de tránsito pendientes por resolver.")
    else:
        print("¡Felicidades! Cumple con todos los requisitos para obtener su licencia.")