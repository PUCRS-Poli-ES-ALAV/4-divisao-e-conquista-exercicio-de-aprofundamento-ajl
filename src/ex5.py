import random
import time

iteracoes = 0

def multiply_bits(X, Y):
    # converte string binária pra inteiro
    x = int(X, 2)
    y = int(Y, 2)

    # número de bits
    n = max(len(X), len(Y))

    return multiply(x, y, n)


def multiply(x, y, n):
    global iteracoes
    iteracoes += 1

    if n == 1:
        iteracoes += 1
        return x * y
    else:
        m = (n + 1) // 2

        a = x // (2 ** m)
        b = x % (2 ** m)
        c = y // (2 ** m)
        d = y % (2 ** m)

        e = multiply(a, c, m)
        f = multiply(b, d, m)
        g = multiply(b, c, m)
        h = multiply(a, d, m)

        iteracoes += 1
        return (2 ** (2 * m)) * e + (2 ** m) * (g + h) + f


def reset_iteracoes():
    global iteracoes
    iteracoes = 0

def get_iteracoes():
    return iteracoes


def gerar_bits(n):
    return ''.join(random.choice('01') for _ in range(n))


# "Main"
if __name__ == "__main__":
    bits_teste = [4, 16, 64]

    for b in bits_teste:
        X = gerar_bits(b)
        Y = gerar_bits(b)

        reset_iteracoes()

        inicio = time.time()
        resultado = multiply_bits(X, Y)
        fim = time.time()

        tempo = (fim - inicio) * 1000

        print(f"{b} bits")
        print(f"X = {X}")
        print(f"Y = {Y}")
        print(f"Resultado: {resultado}")
        print(f"Iterações: {get_iteracoes()}")
        print(f"Tempo: {tempo:.2f} ms")
        print("---------------------------")