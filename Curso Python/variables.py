# Ejemplo completo con los tipos de variables en Python

# 1. Tipo entero (int)
# Las variables de tipo int representan números enteros.
edad = 25
print("Edad (int):", edad)

# 2. Tipo flotante (float)
# Las variables de tipo float representan números con decimales.
altura = 1.75
print("Altura (float):", altura)

# 3. Tipo cadena (str)
# Las variables de tipo str representan cadenas de texto (strings).
nombre = "Carlos"
print("Nombre (str):", nombre)

# 4. Tipo booleano (bool)
# Las variables de tipo bool pueden tener dos valores: True o False.
es_estudiante = True
es_mayor_de_edad = False
print("Es estudiante (bool):", es_estudiante)
print("Es mayor de edad (bool):", es_mayor_de_edad)

# 5. Tipo lista (list)
# Una lista en Python puede contener múltiples elementos, y estos pueden ser de diferentes tipos.
colores = ["rojo", "verde", "azul"]
print("Colores (list):", colores)

# 6. Tipo tupla (tuple)
# Una tupla es similar a una lista, pero es inmutable, es decir, no puede modificarse después de su creación.
punto = (10, 20)
print("Punto (tuple):", punto)

# 7. Tipo conjunto (set)
# Un conjunto es una colección no ordenada de elementos únicos.
frutas = {"manzana", "banana", "cereza"}
print("Frutas (set):", frutas)

# 8. Tipo diccionario (dict)
# Un diccionario es una colección de pares clave-valor.
persona = {"nombre": "Ana", "edad": 30, "altura": 1.68}
print("Persona (dict):", persona)

# 9. Tipo None
# El tipo None representa la ausencia de un valor o un valor nulo.
nada = None
print("Nada (None):", nada)

# 10. Asignación múltiple
# Puedes asignar valores a varias variables en una sola línea.
x, y, z = 10, 20, 30
print("x:", x)
print("y:", y)
print("z:", z)

# 11. Modificación de variables
# Las variables pueden cambiar de tipo a lo largo de la ejecución del programa.
mi_variable = 5  # Inicialmente es un int
print("mi_variable (antes):", mi_variable)

mi_variable = "Hola, soy una cadena"  # Ahora es un str
print("mi_variable (después):", mi_variable)

# 12. Tipos de variables dentro de una lista
# Las listas pueden contener diferentes tipos de datos al mismo tiempo.
mi_lista = [10, "texto", 3.14, True]
print("Lista con varios tipos:", mi_lista)

# 13. Verificando el tipo de una variable
# Puedes usar la función type() para verificar el tipo de una variable.
print("Tipo de edad:", type(edad))      # <class 'int'>
print("Tipo de altura:", type(altura))  # <class 'float'>
print("Tipo de nombre:", type(nombre))  # <class 'str'>
print("Tipo de es_estudiante:", type(es_estudiante))  # <class 'bool'>
print("Tipo de colores:", type(colores))  # <class 'list'>

