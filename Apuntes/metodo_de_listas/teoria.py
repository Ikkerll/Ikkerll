"""
.append(x)	Agrega un elemento al final de la lista	mi_lista.append(5) → [1, 2, 3, 4, 5]

.insert(i, x)	Inserta el elemento x en la posición i	mi_lista.insert(1, "nuevo") → [1, "nuevo", 2, 3]

"""

mi_lista = [1, 2, 3]
mi_lista.append(4)  # Añade 4 al final
print(mi_lista)  # [1, 2, 3, 4]

mi_lista.insert(1, "nuevo")  # Inserta "nuevo" en la posición 1
print(mi_lista)  # [1, 'nuevo', 2, 3, 4]


"""
.remove(x)	Elimina el primer elemento con valor x	mi_lista.remove(2) → [1, 3, 4]

.pop([i])	Elimina el elemento en la posición i y lo devuelve. Si no se pasa i, elimina el último	mi_lista.pop(1) → 2, mi_lista.pop() → 4

.clear()	Elimina todos los elementos de la lista	mi_lista.clear() → []

"""

mi_lista = [1, 2, 3, 4]
mi_lista.remove(2)  # Elimina el primer "2"
print(mi_lista)  # [1, 3, 4]

# Elimina y devuelve el último elemento
ultimo = mi_lista.pop()
print(ultimo)  # 4
print(mi_lista)  # [1, 3]

mi_lista.clear()  # Elimina todos los elementos
print(mi_lista)  # []


"""
.index(x)	Devuelve la posición del primer elemento con valor x	mi_lista.index(3) → 1
.count(x)	Devuelve el número de veces que x aparece en la lista	mi_lista.count(3) → 1

"""

mi_lista = [1, 2, 3]
print(mi_lista.index(3))  # 2 (posición del primer "3")
print(mi_lista.count(2))  # 2 (aparece dos veces)


"""
.sort()	Ordena la lista en orden ascendente	mi_lista.sort() → [1, 2, 3]

.reverse()	Invierte el orden de la lista	mi_lista.reverse() → [3, 2, 1]

sorted(lista)	Devuelve una nueva lista ordenada (sin modificar la original)	sorted(mi_lista) → [1, 2, 3]

"""

mi_lista = [3, 1, 2]
mi_lista.sort()  # Ordena la lista en orden ascendente
print(mi_lista)  # [1, 2, 3]

mi_lista.reverse()  # Invierte el orden
print(mi_lista)  # [3, 2, 1]

# sorted devuelve una nueva lista ordenada
mi_lista = [3, 1, 2]
ordenada = sorted(mi_lista)
print(ordenada)  # [1, 2, 3]


"""
.copy()	Crea una copia superficial de la lista	mi_lista.copy()
list()	Crea una nueva lista a partir de otra	list(mi_lista)

"""

mi_lista = [1, 2, 3]
copia_lista = mi_lista.copy()
print(copia_lista)  # [1, 2, 3]

# Otra forma de copiar
nueva_lista = list(mi_lista)
print(nueva_lista)  # [1, 2, 3]


"""
+	Concatena dos listas	[1, 2] + [3, 4] → [1, 2, 3, 4]
.extend(lista)	Agrega todos los elementos de una lista a la otra	mi_lista.extend([4, 5])

"""

mi_lista = [1, 2]
otra_lista = [3, 4]
print(mi_lista + otra_lista)  # [1, 2, 3, 4]

mi_lista.extend([4, 5])  # Añade los elementos de otra lista
print(mi_lista)  # [1, 2, 4, 5]


"""
len(lista)	Devuelve el tamaño de la lista	len(mi_lista) → 3
lista[i]	Accede a un elemento específico	mi_lista[1] → 2

"""

mi_lista = [1, [2, 3], 4]
print(len(mi_lista))  # 3 (porque hay 3 elementos)

# Accede al segundo elemento (que es una lista)
print(mi_lista[1])  # [2, 3]

# Accede al primer elemento dentro de la sublista
print(mi_lista[1][0])  # 2
