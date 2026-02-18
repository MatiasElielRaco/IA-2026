# Creando diccionarios con dict
diccionario = dict(nombre="Matias", apellido="Raco")

# Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["matias","rancio"]): "jajaja"}

# Creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

# Creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"], "no se")

print(diccionario)