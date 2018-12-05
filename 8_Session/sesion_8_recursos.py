from typing import *
from random import randrange, seed


# Versión recursiva directa
def recursos_rec(v: Dict[Tuple[int, int], int], m: List[int], U: int) -> int:
    def P(n: int, u: int) -> int:
        # --------------------
        # TODO: IMPLEMENTAR
        return 0  # quitar
        # --------------------

    N = len(m)
    return P(N, U)


# Versión recursiva con memoización
def recursos_rec_mem(v: Dict[Tuple[int, int], int], m: List[int], U: int) -> int:
    def P(n: int, u: int) -> int:
        # --------------------
        # TODO: IMPLEMENTAR
        return 0  # quitar
        # --------------------

    N = len(m)
    mem = {}
    return P(N, U)


# Versión recursiva con memoización y recuperación de camino
def recursos_rec_mem_camino(v: Dict[Tuple[int, int], int], m: List[int], U: int) -> Tuple[int, List[int]]:
    def P(n: int, u: int) -> int:
        # --------------------
        # TODO: IMPLEMENTAR
        return 0  # quitar
        # --------------------

    N = len(m)
    mem = {}
    score = P(N, U)
    sol = []
    # --------------------
    # TODO: IMPLEMENTAR recuperación de camino en sol
    # --------------------
    return score, sol


# Versión iterativa con recuperación de camino
def recursos_iter_camino(v: Dict[Tuple[int, int], int], m: List[int], U: int) -> Tuple[int, List[int]]:
    mem = {}
    N = len(m)  # número de actividades
    # --------------------
    # TODO: IMPLEMENTAR rellenar tabla mem
    # --------------------

    score = 0  # TODO: cambiar por mem[N, U][0]
    sol = []
    # --------------------
    # TODO: IMPLEMENTAR recuperación de camino en sol
    # --------------------
    return score, sol


# Versión iterativa con reduccion del coste espacial
def recursos_iter_reduccion_coste(v: Dict[Tuple[int, int], int], m: List[int], U: int) -> int:
    N = len(m)
    # IMPLEMENTAR
    current = [0] * (U + 1)
    previous = [None] * (U + 1)
    # --------------------
    # TODO: IMPLEMENTAR usar dos columnas para rellenar la última de la tabla
    # --------------------
    return current[U]


# PROGRAMA PRINCIPAL -------------------------------------------------------------------------
if __name__ == "__main__":
    U = 12  # número de unidades de recurso disponibles
    m = [2, 4, 2, 4, 2]  # número máximo de recursos que podemos asignar a cada actividad
    # podemos obtener el número de actividades como len(m)
    seed(0)
    # dicionario/tabla con los beneficios que reportan asignar distintos recursos a cada actividad
    # ejemplo: v[1,3] es el beneficio que proporcionará la actividad 1 si se le asignan 3 unidades de recurso
    v = dict(((i, u), randrange(100)) for i in range(len(m)) for u in range(0, U + 1))

    print("Versión recursiva:")
    print(recursos_rec(v, m, U))
    print()
    print("Versión recursiva con memoización:")
    print(recursos_rec_mem(v, m, U))
    print()
    print("Versión recursiva con memoización y recuperación de camino:")
    print(recursos_rec_mem_camino(v, m, U))
    print()
    print("Versión iterativa con recuperación de camino:")
    print(recursos_iter_camino(v, m, U))
    print()
    print("Versión iterativa con reduccion del coste espacial:")
    print(recursos_iter_reduccion_coste(v, m, U))
