"""Escribe un programa que pida un número al usuario y determine si es par o impar."""

#num = int(input("Introduce un numero: "))

#if num %2 == 0:
#    print("El numero es par") 
    
#else:
#    print("El numero es impar")
    
    
""" Pide al usuario dos números y muestra cuál es mayor o si son iguales. """

#num1 = int(input("Introduce el primer número: "))
#num2 = int(input("Introduce el segundo número: "))

#if num1 > num2 :
#    print(f"El numero mayor es {num1}" )

#elif num1 < num2 :
#    print(f"El numero mayor es {num2}")
    
#else:
#    print(f"Los numeros {num1} y {num2} son iguales")


""" Pide al usuario su edad y muestra un mensaje según su etapa de vida: """

""" Menos de 12 años: "Eres un niño """
""" Entre 12 y 17 años: "Eres un adolescente" """
""" Entre 18 y 64 años: "Eres un adulto" """
""" 65 o más: "Eres un adulto mayor" """

#edad = int(input("Introduce tu edad: "))

#if edad < 12:
#    print("Eres un niño")

#elif edad >= 12 and edad <= 17:
#    print("Eres un adolescente")

#elif edad >= 18  and edad <= 64:
#    print("Eres un adulto")

#else:
#    print("Eres un adulto mayor")

"""Pide el precio de un producto al usuario y aplica un descuento según esta tabla:"""

""" Menos de 50€: Sin descuento """
""" Entre 50€ y 100€: 10% de descuento """
""" Más de 100€: 20% de descuento """

precio = float(input("Introduce el precio del producto: "))

if precio < 50:
    print("Sin descuento")
    
elif precio >= 50 and precio <= 100 :
    print(f"10% de descuento")

else:
    print(f"20% de descuento")


