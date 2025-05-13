A = [
    [4, -1, 0, 0],
    [-1, 4, -1, 0],
    [0, -1, 4, -1],
    [0, 0, -1, 4]
]

b = [1, 1, 1, 1]
x0 = [0, 0, 0, 0]

def metodo_jacobi(A, b, x0, tolerancia=1e-4, iter_max=100):
    n, x = len(A), x0[:]

    for k in range(iter_max):
        x_nuevo = [
            (b[i] - sum(A[i][j] * x[j] for j in range(n) if j != i)) / A[i][i]
            for i in range(n)
        ]

        error = max(abs(x_nuevo[i] - x[i]) for i in range(n))
        print(f"Iteración {k+1}: x = {[round(val, 6) for val in x_nuevo]}, error = {error:.2e}")

        if error < tolerancia:
            print(f"\nConvergió en {k+1} iteraciones.")
            return x_nuevo

        x = x_nuevo

    print("\nNo convergió en el número máximo de iteraciones.")
    return x

# Ejemplo de uso


solucion = metodo_jacobi(A, b, x0)
print("\nSolución aproximada:", solucion)
