"""
Pide al usuario su nombre y edad.
Muestra un mensaje como: "Hola Juan, tienes 25 años."

"""

nombre  = input("Introduce tu nombre: ")
edad = int(input("Cual es tu edad: "))

print(f"Hola {nombre}, tienes {edad} años.")


"""
Pide al usuario dos números enteros.
Súmalos e imprime el resultado.

"""

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

suma =  num1 + num2

print(f"La suma de los numeros es {suma}")


"""
Pide al usuario una temperatura en grados Celsius.
Convierte la temperatura a Fahrenheit con la fórmula:
F=(C*9/5)+32

"""

grados_C = float(input("Introduce la temperatura actual en grados Celsius: "))

formula = grados_C *9 / 5 + 32

print(f"Los grados en Fahrenheit es: {formula} ")


"""
Pide al usuario que introduzca tres palabras separadas por espacios.
Guarda cada palabra en una variable distinta.
Imprime cada palabra en una línea diferente.

"""

palabra1, palabra2, palabra3 = input("Introuduce tres palabras separados con espacios: ").split()

print(f"Primera palabra: {palabra1}")
print(f"Segunda palabra: {palabra2}")
print(f"Tercera palabra: {palabra3}")


"""

Pide al usuario el precio original de un producto.
Pide el porcentaje de descuento.
Calcula el precio final con la fórmula:

Precio final=Precio−(Precio×Descuento/100)

Muestra el precio con descuento.

"""

precio = float(input("Dime el precio del producto: "))
descuento = int(input("Dime el porcentaje de descuento: "))

precio_final = precio - (precio*descuento/100)

print(f"El precio final del producto es: {precio_final}")

