# === archivo1.py ===
print("Hola Mundo!")

# === archivo2.py ===
nombre = input("Por favor, ingresa tu nombre: ")
print(f"¡Hola {nombre}!")

# === archivo3.py ===
nombre = input("ingresa tu nombre: ")
apellido = input("ingresa tu apellido: ")
edad = input("ingresa tu  edad: ")
pais = input("ingrese tu pais: ")
print(f"{nombre} {apellido} {edad} {pais}: ")

# === archivo4.py ===
radio = float(input("Ingresa el radio del círculo: "))
print(f"\nÁrea: {3.1416 * radio ** 2:.2f}")
print(f"Perímetro: {2 * 3.1416 * radio:.2f}")

# === archivo5.py ===
segundos = int(input("ingrese cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

# === archivo6.py ===
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))
print(f"\nTabla del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# === archivo7.py ===
    print("Ingrese dos números distintos de cero")
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print("\nResultados:")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} × {num2} = {multiplicacion}")
print(f"División: {num1} ÷ {num2} = {division:.2f}")

# === archivo8.py ===
print("Calculadora de Índice de Masa Corporal (IMC)")

# Solicitar datos al usuario
altura = float(input("Ingresa tu altura en metros :"))
peso = float(input("Ingresa tu peso en kilogramos :"))

# Calcular IMC
imc = peso / (altura ** 2)

# Mostrar resultado
print(f"\nTu IMC es: {imc:.2f}")

# === archivo9.py ===
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C equivalen a {fahrenheit:.1f}°F")
# === archivo10.py ===
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print(f"\nEl promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

