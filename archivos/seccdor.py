import numpy as np
import math

def f(x):
    """
    Calcula el valor de la función f(x) = 2sen(x) - x^2 / 10.
    """
    return 2 * np.sin(x) - (x**2) / 10

def golden_section_search_max_corrected(func, xl, xu, max_iter=8, tol=1e-6):
    """
    Encuentra el máximo de una función dentro de un intervalo usando la búsqueda de la sección dorada (versión corregida).

    Args:
        func (callable): La función objetivo.
        xl (float): El límite inferior del intervalo.
        xu (float): El límite superior del intervalo.
        max_iter (int): El número máximo de iteraciones.
        tol (float): La tolerancia para la convergencia.

    Returns:
        tuple: Una tupla conteniendo:
            - x_max (float): La estimación del valor de x donde ocurre el máximo.
            - f_max (float): El valor máximo de la función.
            - results (list): Una lista de diccionarios con los resultados de cada iteración.
    """
    phi = (math.sqrt(5) - 1) / 2
    results = []

    for i in range(1, max_iter + 1):
        d = phi * (xu - xl)
        x1 = xl + d
        x2 = xu - d
        fx1 = func(x1)
        fx2 = func(x2)

        results.append({
            'i': i,
            'xl': xl,
            'fxl': func(xl),
            'x2': x2,
            'fx2': fx2,
            'x1': x1,
            'fx1': fx1,
            'xu': xu,
            'fxu': func(xu),
            'd': d
        })

        if fx1 > fx2:
            xl = x2  # El máximo está en [x2, xu]
        else:
            xu = x1  # El máximo está en [xl, x1]







            

        if abs(xu - xl) < tol:
            break

    x_max = (xl + xu) / 2
    f_max = func(x_max)
    return x_max, f_max, results

# Intervalo inicial
xl_inicial = 0
xu_inicial = 4

# Ejecutar la búsqueda de la sección dorada para maximizar (versión corregida)
x_max_found, f_max_found, iter_results = golden_section_search_max_corrected(f, xl_inicial, xu_inicial, max_iter=8)

# Imprimir la tabla de resultados
print("-------------------------------------------------------------------------------------------------------------------")
print(f"{'i':<3} | {'xl':<8} | {'f(xl)':<10} | {'x2':<8} | {'f(x2)':<10} | {'x1':<8} | {'f(x1)':<10} | {'xu':<8} | {'f(xu)':<10} | {'d':<8}")
print("-------------------------------------------------------------------------------------------------------------------")
for result in iter_results:
    print(f"{result['i']:<3} | {result['xl']:<8.4f} | {result['fxl']:<10.4f} | {result['x2']:<8.4f} | {result['fx2']:<10.4f} | {result['x1']:<8.4f} | {result['fx1']:<10.4f} | {result['xu']:<8.4f} | {result['fxu']:<10.4f} | {result['d']:<8.4f}")
print("-------------------------------------------------------------------------------------------------------------------")

print(f"\nMáximo encontrado en x ≈ {x_max_found:.6f}")
print(f"Valor máximo f(x) ≈ {f_max_found:.6f}")