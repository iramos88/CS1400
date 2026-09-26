
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
test = int (input("que puntaje obtuviste? (0 - 100): "))
asistencia = input("¿Asististe a las clases de manejo? (si/no): ").strip().lower()
tiene_multas = input("¿Tienes multas de tránsito sin pagar? (si/no): ").strip().lower()
#int(input (" que porcentaje obtuvite "))

#convertimos las respuestas a booleanos

asistio_clases = (asistencia == "si")
multas_pendientes = (tiene_multas == "si")

if test >= 80: and asistio_clasesand and not multas_pendientes
  print(" fantastico Licencia aprobada, obtuviste un puntaje alto aprobaste podrar obtner tu licencia ")
elif test >= 70:
 print("Aprobaste el test obtendras tu licencia")
elif test >= 50:
  print("Desaprobaste el test no alcansaste al puntaje minimo intentalo en otra oportunidad")
else:
  print ("puntaje muy bajo, tiene otra oportunidad para dar el test hasta la proxima")  


