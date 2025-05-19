import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Datos
dias = np.array([0, 1, 180, 360, 540, 720])
altura = np.array([0.0, 0.05, 0.08, 0.17, 0.25, 0.33])

# Ajuste polinomial (grado 2 o 3)
coef = Polynomial.fit(dias, altura, deg=3)
dias_fit = np.linspace(0, 14, 200)
altura_fit = coef(dias_fit)

# Gráfica
plt.plot(dias, altura, 'o', label='Datos')
plt.plot(dias_fit, altura_fit, label='Regresión Polinómica (grado 3)')
plt.xlabel('Días')
plt.ylabel('Altura (cm)')
plt.title('Regresión Polinómica del Crecimiento')
plt.legend()
plt.grid(True)
plt.show()
