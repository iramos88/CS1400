
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

# 1. Solicitar y validar la edad (mayor de 18 años)
edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Lo sentimos, tiene que ser mayor de 18 años para tramitar la licencia.")
else:
    # Haremos la Solicitud del puntaje del examen teórico
    # Ingresaremos la variable puntaje examen que sera float, el float hara que el resultado sea entero o decimal
    puntaje_examen = float(input("Ingrese su puntaje en el examen teórico (0-100): "))
    
    # Haremos la solicitud de asistencia a clases (s/n)
    asistio_input = input("¿Asistió a todas las clases obligatorias? (s/n): ").strip().lower()
    asistio_clases = True if asistio_input == 's' else False
    # Strip Elimina todos los espacios en blanco (así como saltos de línea o tabulaciones) que estén al principio y al final de la cadena de texto.
    # Lower Convierte todas las letras de la cadena a minúsculas.

    # 4. Solicitar multas pendientes (s/n)
    multas_input = input("¿Tiene multas de tránsito pendientes? (s/n): ").strip().lower()
    multas_pendientes = True if multas_input == 's' else False

    print("\n--- Resultado de la Evaluación ---")

    # 5. Lógica de evaluación con if-elif-else simplificada
    if puntaje_examen < 70:
        print("No aprueba el examen es inferior a 70.")
    elif not asistio_clases:
        print("No aprueba No cumplió con la asistencia a las clases.")
    elif multas_pendientes:
        print("No aprueba: Tiene multas de tránsito pendientes por resolver.")
    else:
        print("¡Felicidades! Cumple con todos los requisitos para obtener su licencia.")