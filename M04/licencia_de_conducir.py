
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

    # 4. Solicitaremos las multas pendientes (s/n)
    multas_input = input("¿Tiene multas de tránsito pendientes? (s/n): ").strip().lower()
    multas_pendientes = True if multas_input == 's' else False

    print("\n--- Resultado de la Evaluación ---")

    # 5. Ingresamos la Lógica de evaluación con if-elif-else
    if puntaje_examen < 70:
        print (" No aprobo el examen el puntaje es inferior a 70.")
    elif not asistio_clases:
        print("No aprobo no cumplio con la asistencia a clases obligatorias.")
    elif multas_pendientes:
        print("No aprueba: tiene multas pendientes que pagar.")   
    else:
        print("Felicidades cumple con todos los requisitos para obtener su licencia.")      

#¿Cuántos commits hiciste? 28

#¿Qué método te pareció más fácil de usar para guardar y subir tus cambios a GitHub: los comandos en la terminal o la interfaz visual de Visual Studio Code? ¿Por qué?
# me es mas sencillo hacerlo por la interfaz
#¿Para qué sirve ejecutar el comando git status antes de empezar a trabajar y cómo te ayuda a saber qué archivos han sido modificados o están pendientes por guardar?
# ejecutar este comando nos ayuda principalmente como un diagnostico rapido para saber el estados
# actual del repositorio legal.
#¿Por qué es fundamental descargar (git pull) los cambios más recientes del repositorio de la profesora antes de realizar y subir tus propias modificaciones al proyecto?
# este comando git pull descarga los ultimos cambios desde 
# gitHub hacia la computadora.
#¿En tus propias palabras, ¿cuál es la diferencia entre hacer un fork de un repositorio en GitHub y clonar (clone) un repositorio a tu computadora?
# un fork significa crear una copia exacta de un proyecto ajeno, es decir que pertenece a otro usuario
#¿Por qué es una buena práctica escribir mensajes claros y descriptivos en cada commit (por ejemplo: "Agregando mi nombre al proyecto de M4") en lugar de usar palabras vagas como "cambios" o "listo"?
# el poder escribir los mensajes nos aydudara a saber todos los cambios que se estan haciendo en el programa.
#¿Qué tipos de mensajes agregaste?
# se egrego las variables de examenes teoricos, por la validacion de licencia
# se agrego estructuras como if/else
# funciones de cadena de texti como strip() y lower()
#¿Cuál es tu sentencia preferida?
# Estoy aprendiendo estas sentencias, pero  me gustaria aprender bien la sentencia if, elif
#¿Cuándo entra el programa a la segunda sentencia de tu tarea?
# El programa entra a la segunda secuencia es cuandp la condicion de la primera sentencia (if) no se cumple, es decir cuando el resultado de falso.
#¿Qué aprendiste del README.md en tu carpeta M04? No olvides los comentarios!
    