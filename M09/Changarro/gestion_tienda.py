
#Isaac Ramos 
# gestion_tienda.py

# Este módulo contiene las funciones para gestionar el inventario de la tienda.
# Crear las 3 funciones que se describen a continuación:
# Una para agregar un producto, debe recibir inventario, nombre y precio.
# Esta debe tener un try except ValueError para manejar el error si el precio no es un número.
# Otra para buscar el precio de un producto, debe recibir inventario y nombre. Utiliza .get()
# Y una última función para listar todos los productos, debe recibir el inventario.
# Tener una opcion por si esta vacio el inventario.

# TODO #3 Agregar comenantarios a cada función explicando qué hace y cómo funciona.

#from M07 import diccionarios

def agregar_producto(inventario, nombre, precio):
    """
    Agrega o actualiza un producto en el diccionario de inventario.
    
    Parámetros:
        inventario (dict): Diccionario donde se almacena el inventario (producto: precio).
        nombre (str): Nombre del producto a agregar.
        precio (str|float|int): Precio del producto (recibido como texto o número).
        
    Retorna:
        bool: True si el precio es válido y se agregó con éxito, False si ocurre un error.
    """
    try:
        # Convertimos a float para asegurar que sea un número válido
        precio_num = float(precio)
        inventario[nombre] = precio_num
        return True
    except ValueError:
        # Si no se puede convertir a número, devolvemos False
        return False


def buscar_precio(inventario, nombre):
    """
    Busca y retorna el precio de un producto específico en el inventario.
    
    Parámetros:
        inventario (dict): Diccionario con el inventario actual.
        nombre (str): Nombre del producto a buscar.
        
    Retorna:
        float o None: El precio del producto si existe, o None si no se encuentra.
    """
    # Usamos .get() para evitar que el programa falle si la llave no existe
    return inventario.get(nombre, None)


def listar_productos(inventario):
    """
    Muestra en pantalla todos los productos y precios registrados en el inventario.
    Muestra un mensaje si el inventario está vacío.
    
    Parámetros:
        inventario (dict): Diccionario con el inventario a listar.
    """
    if not inventario:
        print("\n> El inventario está vacío.")
    else:
        print("\n--- Inventario Actual ---")
        for producto, precio in inventario.items():
            print(f"• {producto}: ${precio:.2f}")


# ==========================================
# Zona de pruebas (Ejecución principal)
# ==========================================
if __name__ == "__main__":
    # Creamos el diccionario vacío donde se guardarán los datos
    inventario = {}

    # Ejecutamos las llamadas abajo, totalmente fuera de las funciones:
    agregar_producto(inventario, "Manzana", 1.50)
    agregar_producto(inventario, "Pan", 2.00)

    listar_productos(inventario)