import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

from ej1 import simular_lanzamientos


# ejercicio 2
def compare_samples(M1, M2, a = 0.5, label1='Muestra 1', label2='Mestra 2'):
    """
        Compara dos muestras M1 y M2 usando graficas pp, graficas qq y Kolmogórov-Smirnov

        Parámetros:
        -----------
        M1, M2 : array-like
            Muestras de datos a comparar.
        a : float, opcional (por defecto 0.5)
            Significancia para la prueba de Kolmogórov-Smirnov
        label1, label2 : str, opcional
            Etiquetas para identificar las muestras en los gráficos.

        Visualizaciones generadas:
        --------------------------
        1. **Densidad de probabilidad (KDE)**: Estima la densidad de cada muestra y resalta la distancia KS.
        2. **Función de distribución acumulada (CDF)**: Muestra la CDF empírica de ambas muestras y la distancia KS.
        3. **Gráfica PP (Probabilidad-Probabilidad)**: Relaciona las probabilidades acumuladas de ambas muestras.
        4. **Gráfica QQ (Cuantil-Cuantil)**: Compara los cuantiles de ambas distribuciones.
        """
    # Estimación de densidad
    kde1 = stats.gaussian_kde(M1)
    kde2 = stats.gaussian_kde(M2)

    x = np.linspace(min(M1.min(), M2.min()), max(M1.max(), M2.max()), 1000)

    # Función de distribución
    f1 = lambda t: np.mean(M1 <= t)
    f2 = lambda t: np.mean(M2 <= t)

    F1 = np.vectorize(f1)(x)
    F2 = np.vectorize(f2)(x)

    # Distancia KS
    ks_stat, p_value = stats.ks_2samp(M1, M2)
    ks_index = np.argmax(np.abs(F1 - F2))
    ks_x = x[ks_index]
    ks_y1, ks_y2 = F1[ks_index], F2[ks_index]

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    # a) Densidad
    axs[0, 0].plot(x, kde1(x), label=label1)
    axs[0, 0].plot(x, kde2(x), label=label2)
    axs[0, 0].axvline(ks_x, color='lime',  label=f'KS = {ks_stat:.3f}')
    axs[0, 0].legend()
    axs[0, 0].set_title("Densidad de probabilidad")

    # b) Función de distribución
    axs[0, 1].plot(x, F1, label=label1)
    axs[0, 1].plot(x, F2, label=label2)
    axs[0, 1].plot([ks_x, ks_x], [ks_y1, ks_y2], color='lime',  label=f'KS = {ks_stat:.3f}')
    axs[0, 1].legend()
    axs[0, 1].set_title("Función de distribución acumulada")

    # c) Gráfica PP
    axs[1, 0].plot(F1, F2, 'bo')
    axs[1, 0].plot([0, 1], [0, 1], 'r')
    axs[1, 0].set_title("Gráfica PP")

    # d) Gráfica QQ
    q1 = np.percentile(M1, np.linspace(0, 100, 100))
    q2 = np.percentile(M2, np.linspace(0, 100, 100))
    axs[1, 1].plot(q1, q2, 'bo')
    axs[1, 1].plot(q1, q1, 'r')
    axs[1, 1].set_title("Gráfica QQ")

    plt.tight_layout()
    plt.show()

    print(f"Distancia KS: {ks_stat:.4f}, p-valor: {p_value:.4f}")
    if p_value < a:
        print(f"Rechazamos H0: Con una significancia de {a} se puede asegurar que las muestras son significativamente diferentes.")
    else:
        print(f"No se rechaza H0: Con una significancia de {a} No hay evidencia suficiente para afirmar que las muestras son diferentes.")
### probando funcion con resultado del ejercicio 1

resultados1 = np.array(np.random.geometric(0.2, size=1000))

resultados2 = np.array(simular_lanzamientos(0.2))

compare_samples(resultados1,resultados2)

#*******************************************************************************************


# Ejercicio 3


areas = pd.read_csv('areas.csv', sep = ';')
print(areas.shape)
print(areas.columns)
# tomar muesta del primer dígito de los datos de areas de paises
larea = list(areas.get('Area in square kilometres'))

ld1 = [ int(str(a)[0]) for a in larea ]
ld1[-1] = 4
Marea = np.array(ld1)
# genenrar muestra
n = len(ld1)
np.random.seed(313)
Munif = np.random.uniform(0, 1, n)
Mbenford = np.floor(10**Munif).astype(int)
compare_samples(Mbenford, Marea,0.01, label1='Distribucion de Benford', label2='primer dígito der area de paises (m)')
