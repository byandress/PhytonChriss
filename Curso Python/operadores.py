# Ejemplo completo con operadores en Python

# 1. Operadores aritméticos
# Definimos dos variables para realizar operaciones aritméticas
a = 15
b = 4

# Suma
suma = a + b  # 15 + 4 = 19
print("Suma:", suma)

# Resta
resta = a - b  # 15 - 4 = 11
print("Resta:", resta)

# Multiplicación
multiplicacion = a * b  # 15 * 4 = 60
print("Multiplicación:", multiplicacion)

# División (siempre devuelve un número decimal)
division = a / b  # 15 / 4 = 3.75
print("División:", division)

# División entera (devuelve solo la parte entera)
division_entera = a // b  # 15 // 4 = 3
print("División entera:", division_entera)

# Módulo (el resto de la división)
modulo = a % b  # 15 % 4 = 3
print("Módulo (resto):", modulo)

# Exponentiación (potencia)
potencia = a ** b  # 15 ** 4 = 50625
print("Exponente:", potencia)

# 2. Operadores de comparación
# Comparamos los valores de a y b
print("a == b:", a == b)  # Verifica si a es igual a b
print("a != b:", a != b)  # Verifica si a es diferente de b
print("a > b:", a > b)    # Verifica si a es mayor que b
print("a < b:", a < b)    # Verifica si a es menor que b
print("a >= b:", a >= b)  # Verifica si a es mayor o igual a b
print("a <= b:", a <= b)  # Verifica si a es menor o igual a b

# 3. Operadores lógicos
x = True
y = False

# Operadores lógicos: 'and', 'or', 'not'
print("x and y:", x and y)  # True and False -> False
print("x or y:", x or y)    # True or False -> True
print("not x:", not x)      # Invertir True -> False

# 4. Operadores de asignación
z = 10
z += 5  # Equivalente a z = z + 5, ahora z es 15
print("z después de += 5:", z)

z -= 3  # Equivalente a z = z - 3, ahora z es 12
print("z después de -= 3:", z)

z *= 2  # Equivalente a z = z * 2, ahora z es 24
print("z después de *= 2:", z)

z /= 4  # Equivalente a z = z / 4, ahora z es 6.0 (un float)
print("z después de /= 4:", z)

# 5. Operadores de identidad
# Usamos las funciones id() para ver si dos variables son el mismo objeto
a = [1, 2, 3]
b = a  # b apunta al mismo objeto que a
c = [1, 2, 3]  # c es una lista diferente pero con los mismos valores

print("a is b:", a is b)       # True, a y b son el mismo objeto
print("a is c:", a is c)       # False, a y c son objetos distintos
print("a is not c:", a is not c)  # True, a y c son diferentes

# 6. Operadores de pertenencia
# Verificamos si un valor está presente en una secuencia
frutas = ["manzana", "banana", "cereza"]

print("'manzana' in frutas:", "manzana" in frutas)   # True
print("'naranja' in frutas:", "naranja" in frutas)   # False
print("'naranja' not in frutas:", "naranja" not in frutas)  # True

# 7. Operador condicional (ternario)
edad = 18
resultado = "Mayor de edad" if edad >= 18 else "Menor de edad"
print("Resultado de la evaluación condicional:", resultado)

# 8. Operadores de bits
# Realizamos operaciones bit a bit con enteros
a = 5  # bin(5) = 101
b = 3  # bin(3) = 011

# Operación AND bit a bit
and_bits = a & b  # 101 & 011 = 001
print("a & b (AND):", and_bits)

# Operación OR bit a bit
or_bits = a | b  # 101 | 011 = 111
print("a | b (OR):", or_bits)

# Operación XOR bit a bit
xor_bits = a ^ b  # 101 ^ 011 = 110
print("a ^ b (XOR):", xor_bits)

# Operación NOT bit a bit (invierte los bits)
not_bits = ~a  # NOT 101 (invertido en complemento a dos)
print("~a (NOT):", not_bits)

# Desplazamiento a la izquierda
shift_left = a << 1  # Desplaza los bits de 5 (101) a la izquierda -> 1010 (10 en decimal)
print("a << 1 (desplazamiento izquierda):", shift_left)

# Desplazamiento a la derecha
shift_right = a >> 1  # Desplaza los bits de 5 (101) a la derecha -> 10 (2 en decimal)
print("a >> 1 (desplazamiento derecha):", shift_right)

