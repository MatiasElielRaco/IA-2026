usuario = {
    "nombre": "Matias",
    "rol": "admin",
    "intentos": 3
}

# Devuelve las llaves del diccionario
claves = usuario.keys()

# Devuelve el valor de la llave
valores = usuario.get("intentos")

# Elimina todo del diccionario
# usuario.clear()

# Eliminar un elemento del diccionario
# usuario.pop("rol")

# Obtener un elemento dict_items iterable
usuario_iterable = usuario.items()

print(usuario_iterable)
print(usuario)