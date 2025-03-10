"""
Pide al usuario una contraseña y verifica que cumpla estas condiciones:
✅ Debe tener al menos 8 caracteres
✅ Debe contener al menos una letra y un número

"""

#contraseña = input("Introduce una contraseña: ")

#es_larga = len(contraseña) >= 8

#tiene_letra = any(caracter.isalpha() for caracter in contraseña)
#tiene_numero = any(caracter.isdigit() for caracter in contraseña)

#if es_larga and tiene_letra and tiene_numero:
#    print("Contraseña válida ✅")
#else:
#    print("Contraseña inválida ❌")


"""
Pide al usuario una frase y haz lo siguiente:

Elimina espacios extra al inicio y final.
Convierte todo el texto a minúsculas.
Reemplaza todas las "a" por "@".

"""


#frase = input("Introduce una frase: ")

#frase = frase.strip()
#frase = frase.lower()
#frase = frase.replace("a", "@")

#print (f"Texto Normalizado {frase}")


"""
Pide al usuario que introduzca una dirección de correo y verifica:
✅ Si empieza con "admin"
✅ Si termina en "@gmail.com"
"""

#correo = input("Introduce tu correo: ").lower().strip()

#if correo.startswith("admin") and correo.endswith("@gmail.com"):
#    print("Verificado")
#else:
#    print("Erroneo")


"""
Pide al usuario una frase y cuenta cuántas veces aparece la palabra "python", sin importar si está en mayúsculas o minúsculas.
"""

#frase = input("Escribe una frase: ").lower()

#contador = frase.count("python")

#print(f"La palabara 'python' aparace {contador} veces")


"""
Pide al usuario un texto que contenga números y extrae solo los números en una nueva cadena.
"""

texto = input("Introduce un texto con números: ")

numeros = "".join(caracter for caracter in texto if caracter.isdigit())

print(f"Numeros Extraidos {numeros}")