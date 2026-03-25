import random
import time

# Variável global de iterações
iteracoes = 0

def max_val1(A):
    global iteracoes

    max_val = A[0]

    for i in range(1, len(A)):
        iteracoes += 1  # conta cada comparação

        if A[i] > max_val:
            max_val = A[i]

    return max_val


def gerar_vetor(tamanho):
    return [random.randint(1, 100000) for _ in range(tamanho)]


# "Main"
tamanhos = [32, 2048, 1048576]

for tamanho in tamanhos:
    vetor = gerar_vetor(tamanho)

    iteracoes = 0

    inicio = time.time()

    maior = max_val1(vetor)

    fim = time.time()

    tempo_ms = (fim - inicio) * 1000

    print(f"Tamanho: {tamanho}")
    print(f"Maior valor: {maior}")
    print(f"Iterações: {iteracoes}")
    print(f"Tempo: {tempo_ms:.2f} ms")
    print("---------------------------")