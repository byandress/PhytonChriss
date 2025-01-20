# Ejemplo básico de String en Python

# Declaración de un String
mi_string = "Hola, ¿cómo estás?"
print(mi_string)  # Imprime: Hola, ¿cómo estás?

# Concatenación de Strings
saludo = "Hola"
nombre = "Andrés"
mensaje = saludo + " " + nombre
print(mensaje)  # Imprime: Hola Andrés

# Repetición de un String
texto = "Python " * 3
print(texto)  # Imprime: Python Python Python 

# Acceso a caracteres individuales dentro de un String
palabra = "Python"
print(palabra[0])  # Imprime: P
print(palabra[1])  # Imprime: y

# Métodos comunes con Strings

# Convertir a mayúsculas
texto = "hola"
print(texto.upper())  # Imprime: HOLA

# Convertir a minúsculas
texto = "HOLA"
print(texto.lower())  # Imprime: hola

# Reemplazar parte de un String
texto = "Hola Mundo"
texto_modificado = texto.replace("Mundo", "Python")
print(texto_modificado)  # Imprime: Hola Python

# Dividir un String en una lista usando un delimitador
texto = "manzana,banana,pera"
frutas = texto.split(",")
print(frutas)  # Imprime: ['manzana', 'banana', 'pera']

# Eliminar espacios al principio y al final de un String
texto = "  Hola Mundo  "
print(texto.strip())  # Imprime: Hola Mundo

# Obtener la longitud de un String
texto = "Python"
print(len(texto))  # Imprime: 6

# Escapando caracteres especiales dentro de un String
texto = "Ella dijo: \"Hola, ¿cómo estás?\""
print(texto)  # Imprime: Ella dijo: "Hola, ¿cómo estás?"

# Crear un String multilínea
texto_multilinea = """Este es un texto
que ocupa varias
líneas."""
print(texto_multilinea)
# Imprime:
# Este es un texto
# que ocupa varias
# líneas.

# Uso de Strings para generar contenido HTML dinámico

titulo = "Bienvenido a mi página web"
contenido = "<h1>" + titulo + "</h1>"
print(contenido)  # Imprime: <h1>Bienvenido a mi página web</h1>
