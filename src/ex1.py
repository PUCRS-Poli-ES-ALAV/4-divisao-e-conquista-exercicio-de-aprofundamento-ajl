import random
import time

iteracoes = 0

def merge_sort(L):
    global iteracoes
    iteracoes += 1

    if len(L) <= 1:
        return L

    meio = len(L) // 2

    esquerda = L[:meio]
    direita = L[meio:]

    # Recursão
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    return merge(esquerda, direita)


def merge(esquerda, direita):
    global iteracoes

    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        iteracoes += 1

        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    while i < len(esquerda):
        iteracoes += 1
        resultado.append(esquerda[i])
        i += 1

    while j < len(direita):
        iteracoes += 1
        resultado.append(direita[j])
        j += 1

    return resultado


def reset_iteracoes():
    global iteracoes
    iteracoes = 0

def get_iteracoes():
    return iteracoes

def gerar_vetor(tamanho):
    return [random.randint(1, 100000) for _ in range(tamanho)]


# "Main"
if __name__ == "__main__":
    tamanhos = [32, 2048, 1048576]

    for tamanho in tamanhos:
        vetor = gerar_vetor(tamanho)

        reset_iteracoes()

        inicio = time.time()
        vetor = merge_sort(vetor)
        fim = time.time()

        tempo_ms = (fim - inicio) * 1000

        print(f"Tamanho: {tamanho}")
        print(f"Iterações: {iteracoes}")
        print(f"Tempo: {tempo_ms:.2f} ms")
        print("---------------------------")