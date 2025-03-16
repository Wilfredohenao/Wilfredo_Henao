import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import gaussian_kde


class actividad_2:
    def __init__(self):
        datos=[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10)]
        self.df=pd.DataFrame(data=datos,columns=['# ejercicio','valor'])
        
        #genera un array de numpy con valores de 10 a 29
        def punto_1(self,inf=10,sup=29):
            array_10_29=np.arange(inf,sup)
            self.df["# ejercicio"]= 1
            self.df["valor"]= str(array_10_29)
            self.df.to_csv("actividad_2.csv")

            # Ejercicio 1
array= [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,]
print(array)

arreglo_anidado = [[10,11],[12,13],[14,15],[16,17],[18,19],[20,21],[22,23],[24, 25],[26,27],[28,29]]
print(arreglo_anidado)

# Ejercicio 2
tabla=np.ones ((10,10))
fila=np.array([1,1,1,1,1,1,1,1,1,1])
columna=np.array([1,1,1,1,1,1,1,1,1,1])
sumar= fila + columna
tabla=sumar
print(tabla)

#Ejercicio 3

tabla1= np.random.randint(1,10, 5)
tabla2= np.random.randint(1,10, 5)
producto=tabla1*tabla2
print(tabla1)
print(tabla2)
print(producto)

#Ejercicio 4

 # punto 4
matriz = np.fromfunction(lambda i, j: i + j, (4, 4), dtype=int)
print(matriz)
determinant = np.linalg.det(matriz)
print("\nDeterminant:", determinant)
if determinant != 0:
    inv_matriz = np.linalg.inv(matriz)
    print("\nInverse Matrix:")
    print(inv_matriz)
else:
    print("\nThe matrix is singular and does not have an inverse.")

#Ejercicio 5
# punto 5
Arreglo= np.random.randint(1,200, 100)
print(Arreglo)
print(np.min(Arreglo))
print(np.max(Arreglo))

# ejercicio 6

# ejercicio 6

tabla1=np.ones ((3,1))
tabla2=np.ones ((1,3))
print(tabla1)
print(tabla2)
result=tabla1+tabla2
print("resultado(broadcasting):\n",result)

# ejercicio 7

matriz= np.random.randint(1,10, size=(5,5))
print(matriz)
res = matriz[np . ix_([ 1 , 2 ],[ 1 , 2 ])]

# Mostrar resultado 
print ( "Submatriz creada: \n " ,res, " \n " )


# ejercicio 8
matriz_10x10= np.zeros((10,10))
print(matriz_10x10)

matriz_10x10[3:7,3:7]=5
print(matriz_10x10)

#EJERCICIO 9

matriz = np.array ([[10,25,30],
              [15,30,35],
               [40,45,50]])

matriz_invertida = matriz[::-1]
print(matriz)
print(matriz_invertida)

# ejercicio 10

arreglo= np.random.randint(20,size=(10)  )
print(arreglo)
mayores= arreglo[arreglo > 0.5]

print("\nValores mayores a 0.5:")
print(mayores)

# Ejercicio 11

x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y)
plt.xlabel("eje x")
plt.ylabel("eje Y")
plt.title("grafico de dispersion")


        
# EJERCICIO N 12

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_true = np.sin(x)
ruido = np.random.normal(0, 0.1, size=x.shape)
y_noisy = y_true + ruido
plt.scatter(x, y_noisy, label='Datos con ruido', color='red', alpha=0.5)

plt.plot(x, y_true, label='y = sin(x)', color='blue', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')

#ejercicio 13
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X) + np.sin(Y)
plt.contour(X, Y, Z, 20, cmap='viridis')

#ejercicio 14
# Generar 1000 puntos aleatorios
np.random.seed(0)
x = np.random.randn(1000)
y = np.random.randn(1000)
positions = np.vstack([x, y])
kde = gaussian_kde(positions)
densities = kde(positions)
plt.scatter(x, y, c=densities, cmap='viridis', s=10, edgecolor='k')

#ejercicio 15      
# # Definir el rango para x (entre -2pi y 2pi)
x = np.linspace(-2*np.pi, 2*np.pi, 100)
ruido = np.random.normal(0, 0.2, size=x.shape)
y = np.sin(x) + ruido
X, Y = np.meshgrid(x, np.linspace(-2, 2, 100))  # Malla para el contorno
Z = np.sin(X) + ruido[:, None]  # Función sin(x) con ruido añadido
plt.figure(figsize=(10, 6))
plt.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.6)  

#ejercicio 16
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_true = np.sin(x)

y_noisy = y_true + ruido
plt.scatter(x, y_noisy, label='Datos con ruido', color='red', alpha=0.5)
plt.plot(x, y_true, label='y = sin(x)', color='blue', linewidth=2)
plt.xlabel('x')
ruido = np.random.normal(0, 0.1, size=x.shape)
plt.ylabel('y')
plt.title(r'Gráfico de Dispersión', fontsize=14)
plt.xlabel(r"Eje X:, fontsize=12")
plt.ylabel(r"Eje Y:, fontsize=12")

#ejercicio 17
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.title("histograma 17")

#ejercicio 18
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 2, 1000)
plt.hist(data1, bins=30, alpha=0.6, label='Distribución Normal 1 (Media=0, Desviación Estándar=1)', edgecolor='black')
plt.hist(data2, bins=30, alpha=0.6, label='Distribución Normal 2 (Media=2, Desviación Estándar=2)', edgecolor='black')

#ejercicio 19
#bins10
plt.subplot(1, 3, 1)
plt.hist(data, bins=10, alpha=0.7, edgecolor='black')
plt.title('10 Bins')
#bins30
plt.subplot(1, 3, 2)
plt.hist(data, bins=30, alpha=0.7, edgecolor='black')
plt.title('30 Bins')
#bins50
plt.subplot(1, 3, 3)
plt.hist(data, bins=50, alpha=0.7, edgecolor='black')
plt.title('50 Bins')

#ejercicio 20
# Generar un set de datos con una distribución normal (media = 0, desviación estándar = 1)
data = np.random.normal(0, 1, 1000)
# Calcular la media de los datos
mean_value = np.mean(data)
plt.figure(figsize=(12, 6))
# Histograma con 10 bins
plt.subplot(1, 3, 1)
plt.hist(data, bins=10, alpha=0.7, edgecolor='black')
plt.axvline(mean_value, color='yellow', linestyle='dashed', linewidth=2, label=f'Media = {mean_value:.2f}')
plt.title(' 10 Bins')
# Histograma con 30 bins
plt.subplot(1, 3, 2)
plt.hist(data, bins=30, alpha=0.7, edgecolor='black')
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label=f'Media = {mean_value:.2f}')
plt.title('30 Bins')
# Histograma con 50 bins
plt.subplot(1, 3, 3)
plt.hist(data, bins=50, alpha=0.7, edgecolor='black')
plt.axvline(mean_value, color='green', linestyle='dashed', linewidth=2, label=f'Media = {mean_value:.2f}')
plt.title(' 50 Bins')

#ejercicio 21
# La media es 0 y la desviación estándar es 1
data = np.random.normal(0, 1, 1000)

# Crear el histograma
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.title("histograma del 17")
# Crear el histograma superpuesto para ambos sets de datos
plt.figure(figsize=(10, 6))

# Histograma para el primer set de datos (data1)
plt.hist(data1, bins=30, alpha=0.6, color='blue', edgecolor='black', label='Distribución Normal 1 (Media=0, Desviación Estándar=1)')

# Histograma para el segundo set de datos (data2)
plt.hist(data2, bins=30, alpha=0.6, color='red', edgecolor='black', label='Distribución Normal 2 (Media=2, Desviación Estándar=2)')