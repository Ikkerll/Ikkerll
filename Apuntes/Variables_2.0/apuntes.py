"""
En Python, las variables no tienen un tipo fijo. Esto significa que puedes cambiar el tipo de una variable en cualquier momento:

"""

dato = 10       # Es un número entero (int)
print(type(dato))  # <class 'int'>

dato = "Hola"   # Ahora es una cadena de texto (str)
print(type(dato))  # <class 'str'>


"""
Puedes asignar varios valores a varias variables en una sola línea:

"""

a, b, c = 10, 20, 30
print(a, b, c)  # 10 20 30


"""
También puedes asignar un mismo valor a varias variables:

"""

x = y = z = "Python"
print(x, y, z)  # Python Python Python


"""
Las variables pueden tener diferentes ámbitos (scope), es decir, pueden ser locales o globales.

"""

"""  Variable Local (solo existe dentro de una función) """

def saludar():
    mensaje = "Hola"  # Variable local
    print(mensaje)

saludar()
# print(mensaje)  # ❌ ERROR: No existe fuera de la función


"""  Variable Global (puede usarse en todo el código) """

mensaje = "Hola desde afuera"

def mostrar():
    print(mensaje)  # Sí funciona porque es global

mostrar()

