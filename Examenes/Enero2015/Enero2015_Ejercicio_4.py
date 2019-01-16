from typing import *


def coloca_seguratas(pos_cuadros: List[float], D : float, L : float) -> List[float]:
    res = []
    indices_ordenados = sorted(range(len(pos_cuadros)), key=lambda i: pos_cuadros[i])

    for x in indices_ordenados:
        if len(res) == 0:
            if pos_cuadros[x] + D < L:
                res.append(pos_cuadros[x] + D)
            else:
                res.append(pos_cuadros[x])
        elif res[-1] + D < pos_cuadros[x]:
            if pos_cuadros[x] + D < L:
                res.append(pos_cuadros[x]+D)
            else:
                res.append(pos_cuadros[x])
    return res


if __name__ =="__main__":
    cuadros = [0.5, 1.25, 3.5, 4.78, 6, 6.9, 10, 13, 18.30]
    vision = 2.25
    pared = 19.33

    print(coloca_seguratas(cuadros, vision, pared))
