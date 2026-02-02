# Condicionales
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


# Condicional else if
nota = 30
if nota >= 90:
    print("Sobresaliente")
elif nota >= 80:
    print("Notable")
elif nota >= 70:
    print("Bien")
elif nota >= 60:
    print("Suficiente")
else:
    print("Insuficiente")

# Condicional anidado
num = 10
if num > 0:
    if num % 2 == 0:
        print("El número es positivo y par.")
    else:
        print("El número es positivo e impar.")

# Condicional con operador lógico
hora = 14
if hora >= 6 and hora < 12:
    print("Buenos días")
elif hora >= 12 and hora < 18:
    print("Buenas tardes")
else:
    print("Buenas noches")

# Condicional con operador or
dia = "sábado"
if dia == "sábado" or dia == "domingo":
    print("Es fin de semana")
else:
    print("Es día laborable")

# Condicional con operador not
luz_encendida = True
if not luz_encendida:
    print("La luz está apagada")
else:
    print("La luz está encendida")