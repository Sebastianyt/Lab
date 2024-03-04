from itertools import combinations  # Importar la función combinations de itertools

# Definir los conjuntos
set1 = {1, 2, 3, 4, 5, 9, 17, 7}
set2 = {4, 5, 6, 7, 8, 1, 15}
set3 = {6, 11, 46, 7, 8, 10, 11}

conjuntos = [set1, set2, set3]  # Lista que contiene los tres conjuntos

# Función para verificar si dos conjuntos son disjuntos
def son_disjuntos(conjunto1, conjunto2):
    return not bool(conjunto1 & conjunto2)  # Verifica si la intersección entre ambos conjuntos es vacía

# Calcular y mostrar los conjuntos disjuntos con su cardinalidad para cada conjunto
for i, conjunto in enumerate(conjuntos, start=1):  # Itera sobre los conjuntos con un índice i
    print(f"Conjunto {i}:")  # Imprime el número de conjunto
    print(f"Cardinalidad de set{i}: {len(conjunto)}")  # Imprime la cardinalidad del conjunto
    print("Conjuntos disjuntos:")  # Encabezado para los conjuntos disjuntos
    for r in range(2, len(conjunto) + 1):  # Itera sobre el rango de 2 a la longitud del conjunto + 1
        for subset in combinations(conjunto, r):  # Itera sobre todas las combinaciones de tamaño r del conjunto
            es_disjunto = True  # Suponemos que el subconjunto actual es disjunto
            for prev_subset in combinations(conjunto, r - 1):  # Itera sobre los subconjuntos previos de tamaño r-1
                if not son_disjuntos(set(subset), set(prev_subset)):  # Verifica si el subconjunto actual es disjunto de los subconjuntos previos
                    es_disjunto = False  # Si no es disjunto, cambia la bandera a False
                    break  # Sal del bucle interno
            if es_disjunto:  # Si el subconjunto es disjunto de todos los subconjuntos previos,
                print(subset)  # Imprime el subconjunto disjunto
    print()  # Imprime una línea en blanco para separar los conjuntos
