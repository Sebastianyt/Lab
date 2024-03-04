# Importar las librerías necesarias
from matplotlib import pyplot as plt
from matplotlib_venn import venn3  # Importar la función venn3 para diagramas de Venn
from itertools import combinations  # Importar la función combinations para generar combinaciones de conjuntos

# Definir los conjuntos
set1 = {1, 2, 3, 4, 5, 9,17,7}
set2 = {4, 5, 6, 7, 8, 1,15}
set3 = {6, 11, 46, 7, 8, 10,11}

# Función para calcular la unión de los conjuntos
def calcular_union(conjuntos):
    union = set()  # Inicializar un conjunto vacío para almacenar la unión
    for conjunto in conjuntos:
        union |= conjunto  # Realizar la unión de los conjuntos usando el operador '|'
    return union

# Función para calcular la intersección de los conjuntos
def calcular_interseccion(conjuntos):
    interseccion = set(conjuntos[0])  # Inicializar con el primer conjunto
    for conjunto in conjuntos[1:]:
        interseccion &= conjunto  # Calcular la intersección usando el operador '&'
    return interseccion

# Función para calcular la diferencia de los conjuntos
def calcular_diferencia(conjuntos):
    diferencia = set(conjuntos[0])  # Inicializar con el primer conjunto
    for conjunto in conjuntos[1:]:
        diferencia -= conjunto  # Calcular la diferencia usando el operador '-'
    return diferencia

# Función para calcular todas las combinaciones de los conjuntos dados
def calcular_combinacion(conjuntos):
    combinaciones = []  # Inicializar una lista vacía para almacenar las combinaciones
    # Generar todas las combinaciones posibles de los conjuntos
    for r in range(2, len(conjuntos) + 1):
        for combo in combinations(conjuntos, r):  # Iterar sobre todas las combinaciones posibles
            combinaciones.append(combo)  # Agregar la combinación a la lista
    resultados = {}  # Inicializar un diccionario para almacenar los resultados de cada combinación
    # Calcular la unión, intersección y diferencia para cada combinación
    for idx, combo in enumerate(combinaciones, start=1):
        nombre = f"Combinación {idx}"  # Generar un nombre para la combinación
        union = calcular_union(combo)  # Calcular la unión de los conjuntos en la combinación
        interseccion = calcular_interseccion(combo)  # Calcular la intersección
        diferencia = calcular_diferencia(combo)  # Calcular la diferencia
        # Almacenar los resultados en el diccionario
        resultados[nombre] = {
            'Conjuntos': combo,
            'Unión': union,
            'Intersección': interseccion,
            'Diferencia': diferencia
        }
    return resultados

# Calcular la cardinalidad de los conjuntos
cardinalidad_set1 = len(set1)
cardinalidad_set2 = len(set2)
cardinalidad_set3 = len(set3)

# Calcular todas las combinaciones entre los conjuntos
resultados_combinacion = calcular_combinacion([set1, set2, set3])

# Calcular la diferencia de los conjuntos
diferencia_set = calcular_diferencia([set1, set2, set3])

# Calcular la intersección de los conjuntos
interseccion_set = calcular_interseccion([set1, set2, set3])

# Calcular la unión de los conjuntos
union_set = calcular_union([set1, set2, set3])

# Imprimir la cardinalidad de los conjuntos
print("Cardinalidad de set1:", cardinalidad_set1)
print("Cardinalidad de set2:", cardinalidad_set2)
print("Cardinalidad de set3:", cardinalidad_set3)

# Imprimir la intersección de los conjuntos
print("Intersección de los conjuntos:", interseccion_set)

# Imprimir la unión de los conjuntos
print("Unión de los conjuntos:", union_set)

# Imprimir la diferencia de los conjuntos
print("Diferencia de los conjuntos:", diferencia_set)

# Imprimir los resultados de las combinaciones por consola
for nombre, resultado in resultados_combinacion.items():
    print(f"{nombre}:")
    print(f"Conjuntos: {resultado['Conjuntos']}")
    print(f"Unión: {resultado['Unión']}")
    print(f"Intersección: {resultado['Intersección']}")
    print(f"Diferencia: {resultado['Diferencia']}")
    print()

# Función para dibujar el diagrama de Venn con etiquetas 
def dibujar_venn_y_union(set1, set2, set3):
    # Dibujar el diagrama de Venn con etiquetas 
    venn3([set1, set2, set3], set_labels=('Set 1\n' + str(set1), 'Set 2\n' + str(set2), 'Set 3\n' + str(set3)))
    # Mostrar el gráfico
    plt.title('Diagrama de Venn: Unión de Conjuntos')
    plt.show()

# Llamar a la función para dibujar el diagrama de Venn con la unión de los conjuntos
dibujar_venn_y_union(set1, set2, set3)
