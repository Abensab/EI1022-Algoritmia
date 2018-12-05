from typing import *

# Versión recursiva directa
from Utils.bt_scheme import infinity


def mochila_rec(v: List[int], w: List[int], W: int) -> int:
    def B(n: int, c: int) -> int:
        if n == 0:
            return 0
        if w[n - 1] <= c:
            return max(B(n - 1, c), B(n - 1, c - w[n - 1]) + v[n - 1])
        else:
            return B(n - 1, c)

    N = len(v)
    return B(N, W)


# Versión recursiva con memoización
def mochila_rec_mem(v: List[int], w: List[int], W: int) -> int:
    def B(n: int, c: int) -> int:
        if n == 0:
            return 0
        if (n, c) not in mem:
            if w[n - 1] <= c:
                mem[n, c] = max(B(n - 1, c), B(n - 1, c - w[n - 1]) + v[n - 1])
            else:
                mem[n, c] = B(n - 1, c)

        return mem[n, c]

    N = len(v)
    mem = {}
    return B(N, W)


# Versión recursiva con memorización y recuperación de camino
def mochila_rec_mem_camino(v: List[int], w: List[int], W: int) -> Tuple[int, List[int]]:
    def B(n: int, c: int) -> int:
        if n == 0:
            return 0
        if (n, c) not in mem:
            if w[n - 1] <= c:
                mem[n, c] = max((B(n - 1, c), (n - 1, c, 0)),
                                (B(n - 1, c - w[n - 1]) + v[n - 1], (n - 1, c - w[n - 1], 1)))
            else:
                mem[n, c] = B(n - 1, c), (n - 1, c, 0)
        return mem[n, c][0]

    N = len(v)
    mem = {}
    score = B(N, W)
    sol = []
    n, q = N, W
    while n != 0:
        _, (nPrev, qPrev, i) = mem[n, q]
        sol.append(i)
        q, n = qPrev, nPrev
    sol.reverse()
    return score, sol


# Versión iterativa con recuperación de camino
def mochila_iter_camino(v: List[int], w: List[int], W: int) -> Tuple[int, List[int]]:
    mem = {}
    N = len(v)  # número de objetos

    for c in range(W + 1):
        mem[0, c] = 0, []

    for n in range(1, N + 1):
        for c in range(W + 1):
            if w[n - 1] <= c:
                mem[n, c] = max((mem[n - 1, c][0], (n - 1, c, 0)),
                                (mem[n - 1, c - w[n - 1]][0] + v[n - 1], (n - 1, c - w[n - 1], 1)))
            else:
                mem[n, c] = mem[n - 1, c][0], (n - 1, c, 0)

    score = mem[N, W][0]
    sol = []

    while n != 0:
        _, (nPrev, cPrev, i) = mem[n, c]
        sol.append(i)
        n, c = nPrev, cPrev
    sol.reverse()
    return score, sol


# Versión iterativa con reduccion del coste espacial

def mochila_iter_reduccion_coste(v: List[int], w: List[int], W: int) -> int:
    N = len(v)  # número de objetos
    current = [0] * (W + 1)
    previous = [0] * (W + 1)
    for n in range(1, N + 1):
        previous, current = current, previous
        for c in range(W + 1):
            if w[n - 1] <= c:
                current[c] = max(previous[c],
                                 previous[c - w[n - 1]] + v[n - 1])
            else:
                current[c] = previous[c]

    return current[W]


# PROGRAMA PRINCIPAL -------------------------------------------------------------------------
if __name__ == "__main__":
    values = [90, 75, 60, 20, 10]
    weights = [4, 3, 3, 2, 2]
    capacity = 6

    print("Versión recursiva:")
    print(mochila_rec(values, weights, capacity))
    print()
    print("Versión recursiva con memoización:")
    print(mochila_rec_mem(values, weights, capacity))
    print()
    print("Versión recursiva con memoización y recuperación de camino:")
    print(mochila_rec_mem_camino(values, weights, capacity))
    print()
    print("Versión iterativa con recuperación de camino:")
    print(mochila_iter_camino(values, weights, capacity))
    print()
    print("Versión iterativa con reduccion del coste espacial:")
    print(mochila_iter_reduccion_coste(values, weights, capacity))
