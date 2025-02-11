import numpy as np
import matplotlib.pyplot as plt

def simular_lanzamientos(p, N=1000):
    """
    Simula lanzamientos de una moneda hasta obtener el primer éxito.
    
    Parámetros:
    - p: Probabilidad de éxito en un solo lanzamiento (0 < p < 1).
    - N: Número de experimentos a realizar.
    """
    resultados = np.random.geometric(p, N)
    
    # Graficar la distribución de los lanzamientos necesarios hasta el éxito
    plt.hist(resultados, bins=range(1, max(resultados) + 1), density=True, alpha=0.6, color='b', edgecolor='black')
    plt.xlabel('Número de lanzamientos hasta el primer éxito')
    plt.ylabel('Densidad')
    plt.title(f'Distribución geométrica (p={p})')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

# Ejecutar la simulación con distintos valores de p
for p in [0.2, 0.5, 0.8]:
    simular_lanzamientos(p)