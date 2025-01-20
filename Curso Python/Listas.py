# Ejemplo de listas en Python

# 1. Crear una lista simple
mi_lista = [1, 2, 3, 4]
print("Lista inicial:", mi_lista)  # Imprime: [1, 2, 3, 4]

# 2. Acceder a los elementos de la lista por índice
# Recordemos que el índice comienza desde 0
print("Primer elemento de la lista:", mi_lista[0])  # Imprime: 1
print("Último elemento de la lista:", mi_lista[-1])  # Imprime: 4

# 3. Modificar un elemento de la lista
# Cambiar el valor en el índice 2
mi_lista[2] = 100
print("Lista después de modificar un elemento:", mi_lista)  # Imprime: [1, 2, 100, 4]

# 4. Agregar elementos a la lista
# Usamos `append` para agregar un elemento al final
mi_lista.append(5)
print("Lista después de agregar un elemento:", mi_lista)  # Imprime: [1, 2, 100, 4, 5]

# Usamos `insert` para agregar un elemento en un índice específico
mi_lista.insert(1, 50)  # Inserta el valor 50 en el índice 1
print("Lista después de insertar un elemento:", mi_lista)  # Imprime: [1, 50, 2, 100, 4, 5]

# 5. Eliminar elementos de la lista
# Usamos `remove` para eliminar un elemento específico
mi_lista.remove(50)  # Elimina el primer 50 que encuentre
print("Lista después de eliminar un elemento:", mi_lista)  # Imprime: [1, 2, 100, 4, 5]

# Usamos `pop` para eliminar un elemento en un índice específico (por defecto elimina el último)
elemento_eliminado = mi_lista.pop(2)  # Elimina el elemento en el índice 2
print("Elemento eliminado con pop:", elemento_eliminado)  # Imprime: 100
print("Lista después de hacer pop:", mi_lista)  # Imprime: [1, 2, 4, 5]

# 6. Comprobar si un valor está en la lista usando `in`
print("¿Está el número 4 en la lista?", 4 in mi_lista)  # Imprime: True
print("¿Está el número 10 en la lista?", 10 in mi_lista)  # Imprime: False

# 7. Ordenar la lista
mi_lista.sort()  # Ordena la lista de menor a mayor
print("Lista ordenada:", mi_lista)  # Imprime: [1, 2, 4, 5]

# 8. Invertir el orden de los elementos con `reverse`
mi_lista.reverse()  # Invierte el orden de los elementos
print("Lista invertida:", mi_lista)  # Imprime: [5, 4, 2, 1]

# 9. Obtener la longitud de la lista usando `len()`
longitud = len(mi_lista)
print("Longitud de la lista:", longitud)  # Imprime: 4

# 10. Listas anidadas (listas dentro de listas)
# Creamos una lista que contiene otras listas
mi_lista_anidada = [[1, 2], [3, 4], [5, 6]]
print("Lista anidada:", mi_lista_anidada)  # Imprime: [[1, 2], [3, 4], [5, 6]]

# Acceder a un elemento dentro de una lista anidada
print("Primer elemento de la primera lista interna:", mi_lista_anidada[0][0])  # Imprime: 1
print("Segundo elemento de la tercera lista interna:", mi_lista_anidada[2][1])  # Imprime: 6

# 11. Trabajar con listas de diferentes tipos de datos
lista_mixta = [1, "Hola", 3.14, True]
print("Lista con diferentes tipos de datos:", lista_mixta)  # Imprime: [1, 'Hola', 3.14, True]

# 12. Hacer una lista con rangos de números
# Usamos `range` para crear una lista de números consecutivos
lista_rango = list(range(1, 6))  # Crea una lista de 1 a 5
print("Lista creada con range:", lista_rango)  # Imprime: [1, 2, 3, 4, 5]

# 13. Copiar una lista
copia_lista = mi_lista[:]
print("Copia de la lista:", copia_lista)  # Imprime: [5, 4, 2, 1]

# 14. Eliminar todos los elementos de la lista
mi_lista.clear()
print("Lista después de borrar todos los elementos:", mi_lista)  # Imprime: []
