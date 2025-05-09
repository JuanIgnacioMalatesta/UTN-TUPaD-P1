
# Trabajo Práctico 5 - Listas

# 1) Lista de múltiplos de 4 del 1 al 100
multiplos_de_4 = list(range(4, 101, 4))
print("1) Múltiplos de 4 del 1 al 100:", multiplos_de_4)

# 2) Lista con cinco elementos y mostrar el penúltimo
gustos = ["pizza", "chocolate", "playa", "libros", "música"]
print("2) Penúltimo elemento:", gustos[-2])

# 3) Lista vacía, agregar tres palabras con append
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("3) Lista resultante:", lista_vacia)

# 4) Reemplazar valores en la lista animales
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("4) Lista modificada:", animales)

# 5) Explicación del programa (no se da el código exacto en el PDF, se omite)

# 6) Lista con números del 10 al 30, saltos de 5, mostrar los dos primeros
numeros_saltos = list(range(10, 31, 5))
print("6) Dos primeros números:", numeros_saltos[:2])

# 7) Reemplazar valores centrales en lista autos
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["civic", "focus"]
print("7) Autos modificados:", autos)

# 8) Lista vacía, agregar dobles de 5, 10 y 15
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8) Lista de dobles:", dobles)

# 9) Modificar lista de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")  # a)
compras[1][1] = "tallarines"  # b)
compras[0].remove("pan")  # c)
print("9) Lista de compras modificada:", compras)

# 10) Crear lista anidada con estructura específica
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("10) Lista anidada:", lista_anidada)
