""" .lower()	Convierte todo a minúsculas	"Hola".lower() → "hola"
    
    .upper()	Convierte todo a mayúsculas	"Hola".upper() → "HOLA"
    
    .capitalize()	Primera letra en mayúscula	"hola".capitalize() → "Hola"
    
    .title()    Primera letra de cada palabra en mayúscula	"hola mundo".title() → "Hola Mundo"
   
    .casefold()	Convierte a minúsculas (más fuerte que .lower()) "MÜLLER".casefold() → "müller" 
"""

#texto = "Hola Mundo"
#print(texto.lower())  # hola mundo
#print(texto.upper())  # HOLA MUNDO
#print(texto.capitalize())  # Hola mundo
#print(texto.title())  # Hola Mundo



""" .strip()	Elimina espacios al inicio y final	" hola ".strip() → "hola"
    .lstrip()	Elimina espacios a la izquierda	" hola".lstrip() → "hola"
    .rstrip()	Elimina espacios a la derecha	"hola ".rstrip() → "hola"
"""

#texto = "  hola  "
#print(texto.strip())   # "hola"
#print(texto.lstrip())  # "hola "
#print(texto.rstrip())  # " hola"


"""
    .replace(a, b)	Reemplaza a por b	"Hola Mundo".replace("Mundo", "Python") → "Hola Python"

    .split(sep)	Divide en una lista por sep	"a,b,c".split(",") → ["a", "b", "c"]

    .join(lista)	Une lista con un separador	"-".join(["a", "b", "c"]) → "a-b-c"
"""


#texto = "Hola Mundo"
#print(texto.replace("Mundo", "Python"))  # Hola Python

#lista = "a,b,c".split(",")
#print(lista)  # ['a', 'b', 'c']

#print("-".join(lista))  # a-b-c

"""
    .startswith(sub)	¿Empieza con sub?	"Python".startswith("Py") → True
    
    .endswith(sub)	¿Termina con sub?	"Hola.txt".endswith(".txt") → True
    
    .find(sub)	Posición de sub (-1 si no existe)	"Hola".find("o") → 1
    
    .count(sub)	Cuenta ocurrencias de sub	"Hola Hola".count("Hola") → 2
"""

#texto = "Python es genial"

#print(texto.startswith("Py"))  # True
#print(texto.endswith("genial"))  # True
#print(texto.find("es"))  # 7
#print(texto.count("Python"))  # 1

"""
    .isalpha()	¿Solo letras?	"Python".isalpha() → True
    .isdigit()	¿Solo números?	"123".isdigit() → True
    .isalnum()	¿Letras y/o números?	"Python3".isalnum() → True
    .isspace()	¿Solo espacios?	" ".isspace() → True
"""

#print("Python".isalpha())  # True
#print("123".isdigit())  # True
#print("Python3".isalnum())  # True
#print("   ".isspace())  # True
