import numpy as np

def metodo_lagrange():
    x_data = np.array([1, 180, 360, 540, 720], dtype=float)
    y_data = np.array([0.05, 0.08, 0.17, 0.25, 0.33], dtype=float)

    x_val = float(input("Ingrese el día a estimar (Lagrange): "))
    print(f"\nInterpolación de Lagrange para x = {x_val}:")

    for n in range(2, len(x_data) + 1):
        estimate = 0
        for i in range(n):
            term = y_data[i]
            for j in range(n):
                if i != j:
                    term *= (x_val - x_data[j]) / (x_data[i] - x_data[j])
            estimate += term

        error = abs((estimate - y_data[-1]) / y_data[-1]) * 100
        print(f"Iteración {n-1}: Resultado = {estimate:.5f}, Error relativo ≈ {error:.2f}%")

metodo_lagrange()
