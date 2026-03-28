import random
import time

import ex1
import ex2
import ex3
import ex4
import ex5


def gerar_vetor(tamanho):
    return [random.randint(1, 100000) for _ in range(tamanho)]

def gerar_numero(bits):
    return random.getrandbits(bits)


tamanhos = [32, 2048, 1048576]
bits = [4, 16, 64]


def formatar(it, tempo):
    return f"{it} / {tempo:.2f}"


# Tabela 1 -> Vetores
print("\nTabela de Resultados 1: Algoritmos sobre Vetores\n")

print("Algoritmo".ljust(25), end="")
for t in tamanhos:
    print(f"{t} (it/ms)".ljust(20), end="")
print()

print("-" * 85)

# MERGE SORT
print("Merge Sort".ljust(25), end="")

for t in tamanhos:
    v = gerar_vetor(t)

    ex1.reset_iteracoes()

    inicio = time.time()
    ex1.merge_sort(v)
    fim = time.time()

    tempo = (fim - inicio) * 1000
    it = ex1.get_iteracoes()

    print(formatar(it, tempo).ljust(20), end="")

print()

# MAX VAL 1
print("Max Val Iterativo".ljust(25), end="")

for t in tamanhos:
    v = gerar_vetor(t)

    ex2.reset_iteracoes()

    inicio = time.time()
    ex2.max_val1(v)
    fim = time.time()

    tempo = (fim - inicio) * 1000
    it = ex2.get_iteracoes()

    print(formatar(it, tempo).ljust(20), end="")

print()

# MAX VAL 2
print("Max Val Recursivo".ljust(25), end="")

for t in tamanhos:
    v = gerar_vetor(t)

    ex3.reset_iteracoes()

    inicio = time.time()
    ex3.max_val2(v, 0, len(v) - 1)
    fim = time.time()

    tempo = (fim - inicio) * 1000
    it = ex3.get_iteracoes()

    print(formatar(it, tempo).ljust(20), end="")

print()

# Tabela 2 -> Multiplicações
print("\nTabela de Resultados 2: Multiplicações\n")

print("Algoritmo".ljust(25), end="")
for b in bits:
    print(f"{b} bits (it/ms)".ljust(20), end="")
print()

print("-" * 85)

def formatar(it, tempo):
    return f"{it} / {tempo:.2f}"


# Multiplicação (int)
print("Multiplicação (int)".ljust(25), end="")

for b in bits:
    x = gerar_numero(b)
    y = gerar_numero(b)

    ex4.reset_iteracoes()

    inicio = time.time()
    ex4.multiply(x, y, b)
    fim = time.time()

    tempo = (fim - inicio) * 1000
    it = ex4.get_iteracoes()

    print(formatar(it, tempo).ljust(20), end="")

print()  


# Multiplicação (bits string)
print("Multiplicação (bits str)".ljust(25), end="")

for b in bits:
    X = ex5.gerar_bits(b)
    Y = ex5.gerar_bits(b)

    ex5.reset_iteracoes()

    inicio = time.time()
    ex5.multiply_bits(X, Y)
    fim = time.time()

    tempo = (fim - inicio) * 1000
    it = ex5.get_iteracoes()

    print(formatar(it, tempo).ljust(20), end="")

print("\n")