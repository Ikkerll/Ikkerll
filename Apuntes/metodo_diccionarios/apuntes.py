"""
Los diccionarios en Python son estructuras de datos que almacenan pares clave-valor. Se declaran con {} y permiten acceder a los valores mediante sus claves.

"""

mi_diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}



"""
.get(clave, valor_por_defecto)	Devuelve el valor de la clave. Si no existe, devuelve valor_por_defecto	mi_diccionario.get("edad") → 25

diccionario[clave]	Accede directamente al valor (error si la clave no existe)	mi_diccionario["edad"] → 25

"""

mi_diccionario = {"nombre": "Ana", "edad": 30}

# Usando get()
print(mi_diccionario.get("nombre"))  # Ana
print(mi_diccionario.get("altura", "No disponible"))  # No disponible

# Acceso directo
print(mi_diccionario["edad"])  # 30
