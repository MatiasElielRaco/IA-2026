# Se le pide al usuario la frase
frase = input("Decime algo loco, que te calculo cuanto tardarias en decirlo: ")

# Se separa las palabras por espacios
palabras = frase.split(" ")

# Se calcula la cantidad de palabras
cantidad_palabras = len(palabras)

# En caso de que sean mas de 120 palabras se le dice esto
if cantidad_palabras > 120: 
    print("Para loco tampoco te pedi un testamento")

# Se calcula cuanto tardaria en decir las palabras y se lo decimos
print(f"Dijiste {cantidad_palabras} palabras, y tardarias {cantidad_palabras/2} segudnos en decirlo")
print(f"Dalto lo diria en {cantidad_palabras * 100 // 2 * 1.3 / 100} segundos ")