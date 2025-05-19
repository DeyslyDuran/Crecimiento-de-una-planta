import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Datos
x = np.array([0, 1,180,360,540,720])       # días
y = np.array([0,8,9,8,9,8])  # temperatura
z = np.array([0.0, 0.05,0.08,0.17,0.25,0.33])  # altura

# Combinar x e y en una sola matriz
X = np.column_stack((x, y))

# Crear características polinomiales hasta grado 3
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

# Ajustar modelo
model = LinearRegression()
model.fit(X_poly, z)

# Crear malla para graficar
x_range = np.linspace(min(x), max(x), 30)
y_range = np.linspace(min(y), max(y), 30)
x_mesh, y_mesh = np.meshgrid(x_range, y_range)
X_mesh = np.column_stack((x_mesh.ravel(), y_mesh.ravel()))
X_mesh_poly = poly.transform(X_mesh)
z_pred = model.predict(X_mesh_poly).reshape(x_mesh.shape)

# Gráfico 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, color='red', label='Datos reales')
ax.plot_surface(x_mesh, y_mesh, z_pred, cmap='viridis', alpha=0.7)

ax.set_xlabel('Día')
ax.set_ylabel('Temperatura (°C)')
ax.set_zlabel('Altura (cm)')
ax.set_title('Regresión polinómica cúbica 3D del crecimiento de una planta')
ax.legend()
plt.show()