# Creando un conjuntos con set
conjunto = set(["dato1", "dato2"])

# Metiendo un conjunto dentro de otr conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)

# Teoria de Conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)

# Verificando si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)

# Verificar si algún número en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)