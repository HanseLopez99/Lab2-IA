# **Laboratorio 2 - Inteligencia Artificial (2025)**
### Universidad del Valle de Guatemala

## **Integrantes**
- Hansel López - 19026  
- Juan Luis Solórzano - 201598  
- Gabriel Paz González - 221087  

## **Descripción**
Este laboratorio explora diversos experimentos estadísticos y probabilísticos, incluyendo simulaciones de distribuciones, pruebas de hipótesis y técnicas de reducción de dimensionalidad.  

## **Contenido del Laboratorio**
### **I. Simulación de Lanzamientos de Moneda**  
Se implementó un modelo para simular lanzamientos de una moneda con probabilidad \( p \) de éxito. Se obtuvo la distribución del número de lanzamientos requeridos para el primer éxito y se generaron visualizaciones con diferentes valores de \( p \).

### **II. Comparación de Muestras**  
Se desarrolló una función para comparar dos muestras utilizando:
- **Funciones de densidad estimadas** mediante Kernel Density Estimation (KDE).
- **Gráficas PP y QQ** para evaluar similitudes entre distribuciones.
- **Prueba de Kolmogorov-Smirnov (KS)** para cuantificar diferencias estadísticas.

### **III. Ley de Benford**  
Se analizó la distribución de los primeros dígitos en datos reales de áreas geográficas para verificar su ajuste a la **Ley de Benford**. Se realizaron pruebas estadísticas y visualizaciones para evaluar el cumplimiento de la ley.

### **IV. Generación de Muestra Gaussiana Multivariada**  
Se generó una muestra aleatoria de una distribución gaussiana multivariada de dimensión \( n \geq 4 \) con media \( \mu \) y covarianza \( \Sigma \) definidas por el usuario. Se analizaron las densidades marginales y relaciones bivariadas mediante un **pairplot** y se verificó la similitud entre valores muestrales y teóricos.

### **V. Análisis de Componentes Principales (PCA)**  
Se aplicó PCA para analizar datos funcionales de temperaturas mensuales en estaciones meteorológicas de Canadá. Se interpretaron los primeros dos componentes y se utilizó un **biplot** para identificar agrupaciones en los datos.

### **VI. PCA para Compresión de Imágenes**  
Se implementó un algoritmo de **compresión de imágenes** basado en PCA. Se evaluó el impacto del número de componentes en la calidad de la reconstrucción, analizando la pérdida de información con diferentes valores de \( k \).

## **Repositorio del Proyecto**
El código fuente y los experimentos se encuentran disponibles en el siguiente repositorio de GitHub:  
🔗 **[Repositorio en GitHub](https://github.com/HanseLopez99/Lab2-IA)**

## **Instrucciones de Uso**
1. Clonar el repositorio:
   \`\`\`bash
   git clone https://github.com/HanseLopez99/Lab2-IA.git
   cd Lab2-IA
   \`\`\`
2. Instalar dependencias necesarias (si aplica):
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`
3. Ejecutar cada experimento desde Jupyter Notebook o Python.

## **Conclusión**
Este laboratorio permitió explorar la aplicación de distribuciones estadísticas, pruebas de hipótesis y reducción de dimensionalidad en análisis de datos. Los resultados obtenidos confirman la aplicabilidad de estos métodos en problemas reales.

---
📅 **Fecha de entrega:** Febrero 2025  
📌 **Curso:** Inteligencia Artificial  
📚 **Institución:** Universidad del Valle de Guatemala 