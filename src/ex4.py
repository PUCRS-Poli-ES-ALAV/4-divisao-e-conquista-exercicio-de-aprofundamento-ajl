import random
import time

iteracoes = 0

def multiply(x, y, n):
    global iteracoes
    iteracoes += 1  # conta chamada

    # Caso base
    if n == 1:
        iteracoes += 1
        return x * y

    else:
        m = (n + 1) // 2  # ceil(n/2)

        # divisão dos números
        a = x // (2 ** m)
        b = x % (2 ** m)
        c = y // (2 ** m)
        d = y % (2 ** m)

        # chamadas recursivas
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


def gerar_numero(bits):
    return random.getrandbits(bits)


# "Main"
if __name__ == "__main__":
    bits_teste = [4, 16, 64]

    for bits in bits_teste:
        x = gerar_numero(bits)
        y = gerar_numero(bits)

        reset_iteracoes()

        inicio = time.time()

        resultado = multiply(x, y, bits)

        fim = time.time()

        tempo_ms = (fim - inicio) * 1000

        print(f"{bits} bits")
        print(f"x = {x}")
        print(f"y = {y}")
        print(f"Resultado: {resultado}")
        print(f"Iterações: {iteracoes}")
        print(f"Tempo: {tempo_ms:.4f} ms")
        print("---------------------------")