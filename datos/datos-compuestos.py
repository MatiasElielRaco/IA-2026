# Datos compuestos en Python

# Lista (list) (mutable, se puede modificar después de creada)
lista = ["manzana", "banana", "cereza"]

lista[2] = "naranja"  # Modificando un elemento de la lista

# Tupla (tuple) (inmutable, no se puede modificar después de creada)
tupla = ("rojo", "verde", "azul")

# Conjunto (set) (no se accede por índice y no permite elementos duplicados)
conjunto = {"perro", "gato", "pez"}

# Diccionario (dict) (pares clave-valor)
diccionario = {
    "nombre": "Ana", 
    "edad": 25, 
    "ciudad": "Madrid"
}

print(diccionario["nombre"])
print(lista[1])
