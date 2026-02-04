# Crear una lista
lista = list([False, True, 18])

# Agrega elemntos a la lista
lista.append(250)

# Agregar elemento a la lista en un elemento especifico
lista.insert(2, "buenas")

# Agregar elementos con extend, se agregan al final
lista.extend([True, 230])

# Eliminar un elemento de la lista, poniendo -1 se elimina el ultimo elemento
lista.pop(2)

# Remueve el elemento por su valor
lista.remove(18)

# Elimina todos los elementos
# lista.clear()

# Ordena los elementos (con el parametro reverse=true lo ordena de forma descendente) (No admite cadena de texto)
lista.sort()

# Invierte los elementos de la lista
lista.reverse()

# Buscar un elemento en la lista
buscarEliemnto = lista.index(230)

print(buscarEliemnto)