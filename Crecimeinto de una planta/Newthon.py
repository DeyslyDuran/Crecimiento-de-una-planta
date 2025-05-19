import numpy as np

def metodo_newton():
    x_data = np.array([1, 180, 360, 540, 720], dtype=float)
    y_data = np.array([0.05, 0.08, 0.17, 0.25, 0.33], dtype=float)

    x_val = float(input("Ingrese el día a estimar (Newton): "))
    print(f"\nInterpolación de Newton para x = {x_val}:")

    for n in range(2, len(x_data) + 1):
        coef = np.copy(y_data[:n])
        for j in range(1, n):
            coef[j:n] = (coef[j:n] - coef[j - 1:n - 1]) / (x_data[j:n] - x_data[0:n - j])

        result = coef[0]
        product_term = 1.0
        for i in range(1, n):
            product_term *= (x_val - x_data[i - 1])
            result += coef[i] * product_term

        error = abs((result - y_data[-1]) / y_data[-1]) * 100
        print(f"Iteración {n-1}: Resultado = {result:.5f}, Error relativo ≈ {error:.2f}%")

metodo_newton()
