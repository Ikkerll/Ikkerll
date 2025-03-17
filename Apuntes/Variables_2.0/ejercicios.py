"""
Crea una variable llamada dato que inicialmente sea un número entero.
Cambia el tipo de la variable a cadena de texto y muestra su tipo con type().
Luego, cambia el tipo a decimal y muestra el valor.

"""

dato = 5

print(f"Numero original: {dato}")
print("Tipo original", type(dato))


dato = "palabras"

print("Nuevo valor:", dato)
print("Nuevo tipo:", type(dato))


dato = 12.5
print("Nuevo valor:", dato)
print("Nuevo tipo:", type(dato))


"""
Asigna tres valores enteros a tres variables: x, y y z en una sola línea.
Muestra las tres variables en una sola línea con print().

"""

x,y,z = 1,5,6

print(x,y,z)



"""
Crea una variable global llamada mensaje con el valor "¡Hola Mundo!".
Crea una función que imprima mensaje.
Modifica el valor de mensaje dentro de la función utilizando global y muestra el resultado.

"""

mensaje = "¡Hola Mundo!"
   
def enseñar():
    print(mensaje)
enseñar()
        


"""
Crea una lista llamada numeros con los valores [10, 20, 30].
Asigna numeros a otra variable llamada alias.
Modifica alias añadiendo un número a la lista.
Muestra tanto numeros como alias para verificar si ambas listas se modificaron.

"""

lista = [10,20,30]

alias = [4,6,3]

print(alias)

numero = int(input("Introduce un numero de la lista anterior: "))

if numero in alias:
        alias.remove(numero)
        lista.append(numero)
else:
    print("Te he dicho que pongas un numero de la lista anterior")

print(alias)
print(lista)


"""
Crea una variable llamada edad con un valor de 30.
Elimina la variable edad con del.
Intenta imprimir edad y observa qué sucede.

"""

edad = 30
print(f"La edad del año pasado es {edad}")

del edad

try:
    print(f"Edad despues de eliminar {edad}")

except NameError:
    print("La variable 'edad' ya no existe")
