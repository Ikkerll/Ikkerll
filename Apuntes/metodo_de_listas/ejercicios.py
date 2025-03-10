"""
Pide al usuario una lista de números (como una cadena de texto separada por comas). Luego:

Ordena la lista en orden ascendente.
Busca el número 50 en la lista. Si está, muestra su posición, si no, muestra que no está

"""

entrada = input("Introduce una lista de números (separados por comas): ")

mi_lista = [int(num) for num in entrada.split(",")]

mi_lista.sort()

if 50 in mi_lista:
    print(f"El numero 50 esta en la posición: {mi_lista.index(50)}")
else:
    print("El numero 50 no esta en la lista")
    
print(f"Lista ordenada {mi_lista}")

"""
Crea una lista con 5 elementos. Luego:

Pide al usuario un número.
Si ese número está en la lista, elimínalo. Si no, muestra un mensaje de error.
Imprime la lista final.

"""

mi_lista = [10, 20, 30, 40, 50]

numero = int(input("Introduce un numero para eliminar de la lista: "))

if numero in mi_lista:
    mi_lista.remove(numero)
    print(f"El numero {numero} ha sido eliminado")
    
else:
    print(f"El numero {numero} no esta en la lista")

print(mi_lista)



"""Tienes dos listas:"""

""" Combínalas usando + y imprime el resultado.
   
    Usa .extend() para combinar las listas de nuevo y muestra el resultado.
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print (lista1 + lista2)

lista1.extend([4,5,6])

print(lista1)



"""  
Crea una lista con algunos elementos repetidos.

Pide al usuario un valor.
Cuenta cuántas veces aparece ese valor en la lista y muestra el resultado.

"""

mi_lista = [1, 2, 3, 4, 1, 5, 1]

valor = int(input("Introduce un valor numérico: "))

contador = mi_lista.count(valor)

print (f"El valor {valor} aparece {contador} veces en la lista")


"""
Pide al usuario una lista de palabras (separadas por espacios).

Convierte la entrada en una lista.
Invierte la lista y muestra el resultado.

"""

entrada = input("Introduce una lista de palabras separadas por espacio: ")

mi_lista2 = entrada.split()

mi_lista2.reverse()

print("Lista invertida", mi_lista2)