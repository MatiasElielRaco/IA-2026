# Promedio de duracion
otrosCursosMin = 2.5
otrosCursosMax = 7
otrosCursosProm = 4
daltoCurso = 1.5

# Duración de crudos
crudoProm = 5
crudoDalto = 3.5

# Diferencias de duracion 
diferenciaMin = 100 - daltoCurso / otrosCursosMin * 100
diferenciaMax = 100 - daltoCurso * 1000 // otrosCursosMax / 10
diferenciaProm = 100 - daltoCurso / otrosCursosProm * 100

# Porcentaje de tiempo vacio removido
tiempoVacioPromedio = 100 - otrosCursosProm * 1000 // crudoProm / 10
tiempoVacioDalto = 100 - daltoCurso * 1000 // crudoDalto / 10


# Cnatidad de duración
print("---------------")
print(f"El curso de dalto dura: {diferenciaMin}% menos que el más rapido")
print(f"El curso de dalto es: {diferenciaMax}% menos que el más lento")
print(f"El curso de dalto es: {diferenciaProm}% menos que el promedio")

# Tiempo Vacio
print("---------------")
print(f"Un curso promedio elimina un: {tiempoVacioPromedio}% de tiempo vacio")
print(f"Un curso promedio elimina un: {tiempoVacioDalto}% de tiempo vacio")

# Diferencias si los cursos duraran 10 horas
print("---------------")
print(f"Ver 10 hotas de este curso equivale a ver {otrosCursosProm * 100 // daltoCurso / 10} horas de otros cursos")
print(f"Ver 10 hotas de otros cursos equivale a ver {daltoCurso * 100 // otrosCursosProm / 10} horas de este cursos")
print("---------------")
