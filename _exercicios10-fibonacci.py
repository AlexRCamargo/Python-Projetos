def fibo(n):
    resultado = []
    a, b, = 0, 1
    while b <= n:
        resultado.append(b)
        a, b = b, a + b
    return resultado