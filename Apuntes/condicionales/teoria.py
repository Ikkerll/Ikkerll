#El if se usa para ejecutar un bloque de código solo si una condición es verdadera.

edad = 18
if edad >= 18:
    print("Eres mayor de edad")


#Si la condición del if es falsa, el código dentro de else se ejecuta.

edad = 16
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
    
#Cuando hay múltiples condiciones, se usa elif (else if).

nota = 75

if nota >= 90:                          # Se evalúa if primero.
    print("Tu calificación es A")               
elif nota >= 80:                        # Si es falso, evalúa elif.
    print("Tu calificación es B")
elif nota >= 70:
    print("Tu calificación es C")
else:                                   # Si ninguna condición es verdadera, se ejecuta else.
    print("Has reprobado")


#Podemos combinar condiciones con and, or, y not.

edad = 20
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
else:
    print("No puedes conducir")


