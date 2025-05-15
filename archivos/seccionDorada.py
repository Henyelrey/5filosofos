import numpy as np
import math

def mi_funcion(x):
    """
    Calcula el valor de la función 2sen(x) - x^2 / 10.
    """
    return 2 * np.sin(x) - (x**2) / 10

def golden_section_search(f, x_l, x_u, tol=0.001, max_iter=9):
    """
    Minimiza una función f en el intervalo [x_l, x_u] usando el método de la sección dorada.
    """
    phi = (1+math.sqrt(5)) / 2
    resphi = 2 - phi  # ≈ 0.618

    x1 = x_u + resphi * (x_u - x_l)
    x2 = x_l - resphi * (x_u - x_l)
    f1 = f(x1)
    f2 = f(x2)

    iter_count = 0

    while abs(x_u - x_l) > tol and iter_count < max_iter:
        if f1 < f2:
            x_u = x2
            x2 = x1
            f2 = f1
            x1 = x_u + resphi * (x_u - x_l)
            f1 = f(x1)
        else:
            x_l = x1
            x1 = x2
            f1 = f2
            x2 = x_l - resphi * (x_u - x_l)
            f2 = f(x2)

        iter_count += 1

    x_min = (x_l + x_u) / 2
    return x_min, f(x_min), iter_count

# Ejecutar el método con xl = 0 y xu = 4
x_l = 0
x_u = 4

x_min, f_min, iteraciones = golden_section_search(mi_funcion, x_l, x_u)

print(f"Mínimo en x = {x_min:.5f}")
print(f"Valor mínimo f(x) = {f_min:.5f}")
print(f"Iteraciones: {iteraciones}")
