from itertools import chain, combinations

# Definir los conjuntos
set1 = {1, 2, 3, 4, 5, 9, 17, 7}
set2 = {4, 5, 6, 7, 8, 1, 15}
set3 = {6, 11, 46, 7, 8, 10, 11}

conjuntos = [set1, set2, set3]

# Calcular y mostrar los subconjuntos con su cardinalidad para cada conjunto
for i, conjunto in enumerate(conjuntos, start=1):
    print(f"Conjunto {i}:")
    print(f"Cardinalidad de set{i}: {len(conjunto)}")
    print("Subconjuntos:")
    for r in range(1, len(conjunto) + 1):
        for subset in combinations(conjunto, r):
            print(subset)
    print()