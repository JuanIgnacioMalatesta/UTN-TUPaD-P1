# TP 4 - Estructuras Repetitivas

# 1) Números del 0 al 100
for i in range(101):
    print(i)

# 2) Cantidad de dígitos
numero = input("Ingrese un número entero: ")
print("Cantidad de dígitos:", len(numero))

# 3) Suma entre dos números, excluyendo los extremos
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print("La suma es:", suma)

# 4) Suma hasta ingresar 0
suma = 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
print("Suma total:", suma)

# 5) Juego de adivinar el número
import random
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
        break

# 6) Números pares del 100 al 0
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7) Suma desde 0 hasta número ingresado
limite = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(limite + 1):
    suma += i
print("Suma total:", suma)

# 8) Contador de tipos de números
pares = impares = positivos = negativos = 0
cantidad = 100  # Cambia este valor para pruebas
for _ in range(cantidad):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("Pares:", pares, "Impares:", impares, "Positivos:", positivos, "Negativos:", negativos)

# 9) Media de 100 números
suma = 0
cantidad = 100  # Cambia este valor para pruebas
for _ in range(cantidad):
    num = int(input("Ingrese un número entero: "))
    suma += num
print("Media:", suma / cantidad)

# 10) Invertir los dígitos de un número
numero = input("Ingrese un número entero: ")
invertido = numero[::-1]
print("Número invertido:", invertido)
