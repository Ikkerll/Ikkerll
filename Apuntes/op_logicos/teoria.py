""" Los operadores lógicos en Python permiten combinar condiciones en expresiones if, elif y else. """

# and	Devuelve True si ambas condiciones son verdaderas	x > 5 and y < 10
# or	Devuelve True si al menos una condición es verdadera	x > 5 or y < 10
# not	Invierte el valor lógico	not(x > 5)

""" ✔ Usando and (ambas condiciones deben ser verdaderas) """
""" Si edad >= 18 y tiene_licencia == True, el resultado es True """

#edad = 25
#tiene_licencia = True

#if edad >= 18 and tiene_licencia:
#    print("Puedes conducir")
#else:
#    print("No puedes conducir")


""" Usando or (basta con que una condición sea verdadera) """
""" 🔹 Si al menos una de las condiciones es True, el resultado es True. """

#tiene_permiso_padres = False
#mayor_edad = True

#if mayor_edad or tiene_permiso_padres:
#    print("Puedes entrar al cine")
#else:
#    print("No puedes entrar")
    

""" ✔ Usando not (niega el valor lógico) """
"""🔹 not llueve invierte False a True, por lo que imprime "Puedes salir sin paraguas". """

#llueve = False

#if not llueve:
#    print("Puedes salir sin paraguas")
#else:
#    print("Lleva un paraguas")
    