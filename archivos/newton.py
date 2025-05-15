import numpy as np

def f(x):
    """Función original."""
    return 2 * np.sin(x) - ((x ** 2) / 10)

def df(x):
    """Primera derivada de f(x): f'(x) = 2·sin(x) + 2x·cos(x) - x/5"""
    return 2 * np.cos(x) - x / 5

def ddf(x):
    """Segunda derivada de f(x): f''(x) = 4·cos(x) - 2x·sin(x) - 1/5"""
    return - 2 * np.sin(x) - 1 / 5

def newton_maximization(x0, iterations=4):
    """
    Método de Newton para encontrar un máximo local de la función f(x).
    
    Args:
        x0: Valor inicial.
        iterations: Número de iteraciones a realizar.
    
    Returns:
        x: Valor aproximado del máximo.
        f(x): Valor de la función en el máximo.
        history: Lista con historial de iteraciones.
    """
    history = []

    x = x0
    for i in range(iterations):
        f1 = df(x) #primera derivada
        f2 = ddf(x) #segunda derivada

        if f2 == 0:
            print("Derivada segunda cero. No se puede continuar.")
            break

        x_new = x - f1 / f2 # formula de newton 
        fx_new = f(x_new) #evaluamos la funcion en el nuevo valor 

        history.append([i+1, x, f(x), f1, f2, x_new, fx_new])
        x = x_new #actualizamos

    return x, f(x), history

# =====================
# EJECUCIÓN
# =====================
x_inicial = 2.5
x_max, fx_max, historial = newton_maximization(x_inicial, iterations=4)

# Mostrar resultados
print("\nMétodo de Newton para encontrar el máximo (4 Iteraciones)")
print("------------------------------------------------------------")
print("{:<3} {:<8} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
    
    "i", "x", "f(x)", "f'(x)", "f''(x)", "x_new", "f(x_new)"
))

for row in historial:
    print("{:<3} {:<8.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f}".format(*row))

print(f"\nResultado aproximado tras 5 iteraciones:\n  x ≈ {x_max:.4f}\n  f(x) ≈ {fx_max:.4f}")
