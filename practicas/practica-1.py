# # Calculadora simple en Python
# a = 10 
# b = 5

# print("Suma:", type(a + b), a + b)
# print("Resta:", type(a - b), a - b)
# print("Multiplicación:", type(a * b), a * b)
# print("División:", type(a / b), a / b)


# # Conversion de tipos
# edad = "25"

# edad = int(edad) + 5
# print(edad)

# # Area de rectángulo
# base = 7.5
# altura = 3.2

# area = base * altura
# print(type(area), area)

# # mayor o menor 
# mayor_de_edad = 13

# if(mayor_de_edad >= 18):
#     print("Es mayor de edad")
# else: 
#     print("Es menor de edad")

# # Acceso al sistema
# usuario = "admin"
# contraseña = "1256"

# if (usuario == "admin" and contraseña == "1234"):
#     print("acceso aprobado")
# else:
#     print("acceso denegado")

# # Descuento en compra
# total_compra = 12000

# if(total_compra > 10000):
#     total_compra = total_compra * 10 / 100
#     print(total_compra)
# else:
#     print(total_compra)


# Ejercicios

# 1
numeros = [3, 7, 10, 2, 8]

suma = numeros[0] + numeros[4]
print(suma, numeros[0], numeros[4])

# 2
coordenadas = (10, -20)

x = coordenadas[0]
y = coordenadas[1]

if( x > 0 and y > 0):
    print("punto valido")
else :
    print("punto no valido")

# 3
persona = { 
    "nombre": "Juan",
    "edad": 20,
    "activo": False
}

print(persona["nombre"]) 
if(persona["edad"] >= 18 and persona["activo"]):
    print("Acceso permitido")
else:
    print("Acceso denegado")

# 4
notas = [8, 6, 9]

promedio = (notas[0] + notas[1] + notas[2]) / len(notas)
if(promedio >= 7):
    print(f"Tu promedio es: {promedio}. Aprobado")
else:
    print(f"Tu promedio es: {promedio}. Desaprobado")

# 5
sensor = {
    "temperatura": 39,
    "presion": 120,
}

if(sensor["temperatura"] >= 38):
    print("Alerta")
else:
    print("Normal")

# 6
usuario = {
    "nombre": "Matias",
    "rol": "admin",
    "intentos": 3
}

if(usuario["rol"] == "admin" and usuario["intentos"] <= 3):
    print("Acceso Total")
elif(usuario["rol"] != "admin" and usuario["intentos"] <= 3):
    print("Acceso Limitado")
else:
    print("Acceso Denegado")