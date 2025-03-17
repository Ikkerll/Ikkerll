"""
Crea un diccionario con información de una persona (nombre, edad, ciudad).

Pide al usuario una clave y muestra el valor asociado usando .get().
Si la clave no existe, muestra un mensaje "Clave no encontrada".

"""
persona = {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}

clave =  input("Introduce una clave: ")

if clave in persona :
    print(f"El valor de la clave {clave} es {persona.get(clave)}")
    
else:
    print("Clave no encontrada")



""""
Pide al usuario una frase y cuenta cuántas veces aparece cada palabra. Usa un diccionario donde:

Las claves son las palabras.
Los valores son la cantidad de veces que aparece cada palabra.
Usa .get() para evitar errores al contar.

"""

frase = input("Introduce una frase: ")

palabras = frase.split()

contador_palabras = {}

for palabra in palabras:
    contador_palabras[palabra] = contador_palabras.get(palabra, 0) +1
    
print("Frecuencia de palabras: ", contador_palabras)


"""
Crea un diccionario con tres productos y sus precios. Luego:

Agrega un nuevo producto con su precio.
Pide al usuario el nombre de un producto y elimínalo usando .pop().
Muestra el diccionario actualizado

"""

productos = {"manzana": 1.2, "banana": 0.8, "pera": 1.5}

productos ["limon"] = "1.4"

venta = input("Introduce un producto en venta: ")

if venta in productos:
    productos.pop(venta)

print(f"El producto no se encuentra en esta lista {productos}")
    
