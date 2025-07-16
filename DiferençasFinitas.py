def diferenca_central(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def newton_iterativo(f, x0, epsilon=1e-6, max_iter=100):
    h = 1e-5
    x = x0
    k = 0

    for i in range(max_iter):
        fx = f(x)
        dfx = diferenca_central(f, x, h)

        if abs(dfx) < 1e-10:
            raise ZeroDivisionError("Derivada próxima de zero.")

        x_new = x - fx / dfx
        k = i + 1
        print(f"Iteração {k}: x = {x_new}")

        if abs(fx) < epsilon:
            break

        x = x_new

    return x, k

f = lambda x: x**2 - 2
chute_inicial = 1.0

raiz, iteracoes = newton_iterativo(f, chute_inicial)
print(f"\nRaiz aproximada: {raiz}")
print(f"Número de iterações: {iteracoes}")