cadena1 = "Hola todo bien?"
cadena2 = "Que onda kpo"

mayusc = cadena1.upper()

minusc = cadena1.lower()

primeraMayus = cadena1.capitalize()

# Si no encuentra coincidencias devuelve un -1
busqueda = cadena1.find("a")

# Si no encuentra coincidencias devuelve un error
busquedaFind = cadena1.index("a") 

# Si no es numerico devuelve false, si lo es devuelve true
numerico = cadena1.isnumeric() 

# Si no es alfanumerico devuelve false, si lo es devuelve true
alfanumerico = cadena1.isalpha() 

# Contar coincidencias
contar = cadena1.count("a")

# Contar caracteres
contarCaracteres = len(cadena1)

# Verificar con que empiza una cadena. Devuelve True o False
empieza_con = cadena1.startswith("H")

# Verificar con que termina una cadena. Devuelve True o False
termina_con = cadena1.endswith("H")

# Remplaza un valor de la cadena por otra
reemplazar = cadena1.replace("Hola", "Buenas")

# Separa cadena por lo que se le pase
separar = cadena1.split(" ")

print(separar) 