def soma_riemann(f, a, b, n=100):
    dx = (b - a) / n
    soma = 0.0

    print(f"Iniciando Soma de Riemann no intervalo de [{a}, {b}] com {n} subdivisões.")

    for i in range(n):
        x_i = a + (i + 0.5) * dx

        fx_i = f(x_i)
        area = fx_i * dx
        soma += area

        print(f"Subintervalo {i+1}: x = {x_i:.5f}, f(x) = {fx_i:.5f}, área = {area:.5f}")

    print(f"\nValor aproximado da integral: {soma:.6f}")
    return soma

f = lambda x: x**2
a = 0
b = 1
n = 10

soma_riemann(f, a, b, n)
