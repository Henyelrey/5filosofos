A = [
    [4, -1, 0, 0],
    [-1, 4, -1, 0],
    [0, -1, 4, -1],
    [0, 0, -1, 4]
]

b = [1, 1, 1, 1]
x0 = [0, 0, 0, 0]


def metodo_gauss_seidel(A, b, x0, tolerancia=1e-4, iter_max=100):
    x = x0[:]

    for k in range(iter_max):
        x_anterior = x[:]
        
        for i in range(len(A)):
            x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(len(A)) if j != i)) / A[i][i]

        error = max(abs(x[i] - x_anterior[i]) for i in range(len(A)))
        print(f"Iteración {k+1}: x = {[round(val, 6) for val in x]}, error = {error:.2e}")

        if error < tolerancia:
            print(f"\nConvergió en {k+1} iteraciones.")
            return x

    print("\nNo convergió en el número máximo de iteraciones.")
    return x



solucion = metodo_gauss_seidel(A, b, x0)
print("\nSolución aproximada:", solucion)
