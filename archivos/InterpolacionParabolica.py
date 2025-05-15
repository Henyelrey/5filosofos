import numpy as np

def f(x):
    """Función a interpolar: f(x) = 2x·sin(x) - x²/10"""
    return 2 *  np.sin(x) - ((x ** 2) / 10)

def parabolic_interpolation(x0, fx0, x1, fx1, x2, fx2):
    """
    Realiza interpolación parabólica para estimar el máximo de una función cuadrática.
    """
    numerator = fx0 * (x1**2 - x2**2) + fx1 * (x2**2 - x0**2) + fx2 * (x0**2 - x1**2)
    denominator = 2 * (fx0 * (x1 - x2) + fx1 * (x2 - x0) + fx2 * (x0 - x1))

    if denominator == 0:
        return None  # Evita división entre cero

    return numerator / denominator

def iterative_parabolic_interpolation(x_points, iterations=5):
    """
    Interpolación parabólica iterativa fija para encontrar el máximo de una función.

    Args:
        x_points: Lista de 3 valores iniciales de x.
        iterations: Número de iteraciones fijas a realizar.

    Returns:
        x_max: Valor aproximado de x en el máximo.
        f_max: Valor de f(x_max).
        history: Historial de iteraciones.
    """
    if len(x_points) != 3:
        raise ValueError("Debe proporcionar exactamente 3 puntos iniciales.")

    # Ordenar puntos y calcular f(x)
    x_points = sorted(x_points)
    x0, x1, x2 = x_points
    fx0, fx1, fx2 = f(x0), f(x1), f(x2)

    history = []

    for i in range(iterations):
        x_max = parabolic_interpolation(x0, fx0, x1, fx1, x2, fx2)
        if x_max is None:
            break  # Fallo por división cero

        fx_max = f(x_max)
        history.append([i+1, x0, fx0, x1, fx1, x2, fx2, x_max, fx_max])

        # Reemplazar el punto con menor f(x) para acercarse al máximo
        points = [(x0, fx0), (x1, fx1), (x2, fx2), (x_max, fx_max)]
        points = sorted(points, key=lambda p: p[1], reverse=True)  # Ordenar por valor f(x)
        top3 = sorted(points[:3], key=lambda p: p[0])  # Tomar los mejores 3 y ordenarlos por x


        #asignar nuevos puntos
        x0, fx0 = top3[0]
        x1, fx1 = top3[1]
        x2, fx2 = top3[2]

    return x_max, fx_max, history


# ===========================
# EJECUCIÓN
# ===========================
x_iniciales = [0.5, 1.0, 2.0]  # Puntos iniciales mejor ajustados para convergencia rápida
x_max, fx_max, historial = iterative_parabolic_interpolation(x_iniciales, iterations=5)

# Mostrar resultados
print("\nInterpolación Parabólica Iterativa (5 Iteraciones)")
print("------------------------------------------------------")
print("{:<3} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format(
    "i", "x0", "f(x0)", "x1", "f(x1)", "x2", "f(x2)", "x_max", "f(x_max)"
))

for row in historial:
    print("{:<3} {:<8.4f} {:<8.4f} {:<8.4f} {:<8.4f} {:<8.4f} {:<8.4f} {:<10.4f} {:<10.4f}".format(*row))

print(f"\nResultado aproximado tras 5 iteraciones:\n  x ≈ {x_max:.4f}\n  f(x) ≈ {fx_max:.4f}")
