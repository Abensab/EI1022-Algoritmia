from typing import *


def mientras_quepa(W: List[int], C: int) -> List[int]:
    size = 0
    container = 0
    res = []
    for item in W:
        if size + item <= C:
            size += item
            res.append(container)
        else:
            container += 1
            size = item
            res.append(container)
    return res


def primero_que_quepa(W: List[int], C: int) -> List[int]:
    sizes = [0] * len(W)
    res = []
    for item in W:
        for i, size in enumerate(sizes):
            if size + item <= C:
                sizes[i] += item
                res.append(i)
                break
    return res


def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    indices_ordenados = sorted(range(len(W)), key=lambda i: -W[i])

    sizes = [0] * len(W)
    res = [-1] *len(W)
    for i in indices_ordenados:
        for j, size in enumerate(sizes):
            if sizes[j] + W[i] <= C:
                sizes[j] += W[i]
                res[i]=j
                break
    print(res)
    print(W)
    print(sizes)
    return res


def prueba_binpacking():
    W: List[int] = [1, 2, 8, 7, 8, 3]
    C: int = 10

    for solve in [mientras_quepa, primero_que_quepa, primero_que_quepa_ordenado]:
        sol = solve(W, C)
        print("-" * 40)
        print("Método:", solve.__name__)
        if len(sol) == 0:
            print("No implementado")
        else:
            print("Solución: {}, usados {} contenedores\n".format(sol, 1 + max(sol)))


if __name__ == "__main__":
    prueba_binpacking()
