from itertools import chain, combinations  # Importar las funciones chain y combinations de itertools

# Definir los conjuntos
set1 = {1, 2, 3, 4, 5, 9, 17, 7}
set2 = {4, 5, 6, 7, 8, 1, 15}
set3 = {6, 11, 46, 7, 8, 10, 11}

conjuntos = [set1, set2, set3]  # Crear una lista que contiene los conjuntos definidos

# Calcular y mostrar los subconjuntos con su cardinalidad para cada conjunto
for i, conjunto in enumerate(conjuntos, start=1):  # Iterar sobre los conjuntos numerándolos
    print(f"Conjunto {i}:")  # Imprimir el número del conjunto
    print(f"Cardinalidad de set{i}: {len(conjunto)}")  # Imprimir la cardinalidad del conjunto
    print("Subconjuntos:")  # Imprimir el encabezado para los subconjuntos
    for r in range(1, len(conjunto) + 1):  # Iterar sobre el rango de 1 a la cardinalidad del conjunto
        for subset in combinations(conjunto, r):  # Generar todas las combinaciones de tamaño r del conjunto
            print(subset)  # Imprimir cada subconjunto generado
    print()  # Imprimir una línea en blanco para separar los conjuntos

