import random
import time

# Variável global de iterações
iteracoes = 0

def max_val2(A, init, end):
    global iteracoes

    iteracoes += 1  # conta chamada

    # Caso base
    if end - init <= 1:
        iteracoes += 1
        return max(A[init], A[end])

    else:
        m = (init + end) // 2

        v1 = max_val2(A, init, m)
        v2 = max_val2(A, m + 1, end)

        iteracoes += 1
        return max(v1, v2)


def gerar_vetor(tamanho):
    return [random.randint(1, 100000) for _ in range(tamanho)]


# "Main"
tamanhos = [32, 2048, 1048576]

for tamanho in tamanhos:
    vetor = gerar_vetor(tamanho)

    iteracoes = 0

    inicio = time.time()

    maior = max_val2(vetor, 0, len(vetor) - 1)

    fim = time.time()

    tempo_ms = (fim - inicio) * 1000

    print(f"Tamanho: {tamanho}")
    print(f"Maior valor: {maior}")
    print(f"Iterações: {iteracoes}")
    print(f"Tempo: {tempo_ms:.2f} ms")
    print("---------------------------")