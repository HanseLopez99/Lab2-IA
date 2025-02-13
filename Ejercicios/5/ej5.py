import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Cargar los datos
file_path = 'Ejercicios/5/weather.csv'  # Ruta relativa desde la raíz del proyecto
df = pd.read_csv(file_path)

# Separar los nombres de estaciones y los datos de temperatura
stations = df.iloc[:, -1]  # Última columna contiene los nombres de estaciones
temperatures = df.iloc[:, :-1]  # Todas las demás columnas son temperaturas mensuales

# Estandarizar los datos
scaler = StandardScaler()
temperatures_scaled = scaler.fit_transform(temperatures)

# Aplicar PCA
pca = PCA(n_components=2)
pca_components = pca.fit_transform(temperatures_scaled)

# Extraer los dos primeros componentes principales
p1 = pca_components[:, 0]
p2 = pca_components[:, 1]

# Graficar las curvas de los primeros dos componentes principales
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(p1) + 1), p1, marker='o', linestyle='-', label='Componente Principal 1')
plt.plot(range(1, len(p2) + 1), p2, marker='s', linestyle='--', label='Componente Principal 2')
plt.xlabel('Índice de estación')
plt.ylabel('Valor del componente')
plt.legend()
plt.title('Curvas de los primeros dos componentes principales')
plt.show()

# Crear el biplot para visualizar la agrupación de estaciones
plt.figure(figsize=(10, 7))
plt.scatter(p1, p2, alpha=0.7)
for i, station in enumerate(stations):
    plt.text(p1[i], p2[i], station, fontsize=8, alpha=0.7)
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('Biplot de estaciones basado en PCA')
plt.grid(True)
plt.show()
