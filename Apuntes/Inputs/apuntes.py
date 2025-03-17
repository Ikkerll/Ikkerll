
"""
Por defecto, input() devuelve texto (str), pero si necesitas números, conviértelos:

Tipo de dato	Conversión
Entero (int)	int(input("Introduce un número: "))
Decimal (float)	float(input("Introduce un número decimal: "))
Booleano (bool)	bool(int(input("Introduce 0 o 1: ")))

"""

edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuánto mides en metros? "))

print(f"Tienes {edad} años y mides {altura} metros.")


"""

Si el usuario debe ingresar varios datos en una línea, podemos separarlos con split():

¿Qué hace map(int, valores)?
Convierte cada elemento de la lista valores en un número entero.


"""


valores = input("Introduce tres números separados por espacios: ").split()
num1, num2, num3 = map(int, valores)

print("Números ingresados:", num1, num2, num3)


"""
Podemos asignar un valor por defecto si el usuario no escribe nada:

"""

nombre = input("Introduce tu nombre (por defecto 'Anónimo'): ") or "Anónimo"
print("Hola,", nombre)
