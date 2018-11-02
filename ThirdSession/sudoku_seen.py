from algoritmia.utils import argmin

from Utils.bt_scheme import PartialSolution, BacktrackingSolver
from typing import *
from copy import deepcopy
import time

Position = Tuple[int, int]
Sudoku = List[List[int]]


def vacias(s: Sudoku) -> List[Position]:
    lista_vacios = []
    for fila in range(9):
        for col in range(9):
            if s[fila][col] == 0:
                lista_vacios.append((fila, col))
    return lista_vacios  # si el Sudoku ya está completo


def posibles_en(s: Sudoku, fila: int, col: int) -> Set[int]:
    used = set(s[fila][c] for c in range(9))
    used = used.union(s[f][col] for f in range(9))
    fc, cc = fila // 3 * 3, col // 3 * 3
    used = used.union(s[fc + f][cc + c] for f in range(3) for c in range(3))
    return set(range(1, 10)) - used


def pretty_print(s: Sudoku):
    for i, fila in enumerate(s):
        for j, columna in enumerate(fila):
            print(columna if columna != 0 else ' ', end="")
            if j in [2, 5]:
                print("|", end="")
        print()
        if i in [2, 5]:
            print("---+---+---")


class SudokuPS(PartialSolution):
    def __init__(self, sudoku: Sudoku, lista: List[Position]):
        self.s = sudoku
        self.lv = lista

    # Indica si la sol. parcial es ya una solución factible (completa)
    def is_solution(self) -> bool:
        return len(vacias(self.s)) == 0

    # Si es sol. factible, la devuelve. Si no lanza excepción
    def get_solution(self) -> Sudoku:
        if not self.is_solution(): raise RuntimeError("No tiene solución")
        return self.s

    # Devuelve la lista de sus sol. parciales sucesoras
    def successors(self) -> Iterable["SudokuPS"]:
        v = vacias(self.s)
        posible = argmin(self.lv, lambda pos: len(posibles_en(self.s, pos[0], pos[1])))
        f, c = posible
        new_lv = deepcopy(self.lv)
        new_lv.remove(posible)
        for item in posibles_en(self.s, f, c):
            new_sudoku = deepcopy(self.s)
            new_sudoku[f][c] = item
            yield SudokuPS(new_sudoku, new_lv)


# PROGRAMA PRINCIPAL -------------------------------------------------------
if __name__ == "__main__":
    init = time.time()
    # m_sudoku = [[0, 0, 0, 3, 1, 6, 0, 5, 9], [0, 0, 6, 0, 0, 0, 8, 0, 7], [0, 0, 0, 0, 0, 0, 2, 0, 0],
    #             [0, 5, 0, 0, 3, 0, 0, 9, 0], [7, 9, 0, 6, 0, 2, 0, 1, 8], [0, 1, 0, 0, 8, 0, 0, 4, 0],
    #             [0, 0, 8, 0, 0, 0, 0, 0, 0], [3, 0, 9, 0, 0, 0, 6, 0, 0], [5, 6, 0, 8, 4, 7, 0, 0, 0]]

    # El sudoku más difícil del mundo
    m_sudoku = [[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0],
                [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0],
                [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]]

    print("Original:")
    pretty_print(m_sudoku)
    print("\nSoluciones:")
    # Mostrar todas las soluciones
    # IMPLEMENTAR utilizando SudokuPS y BacktrackingSolver
    for solution in BacktrackingSolver.solve(SudokuPS(m_sudoku, vacias(m_sudoku))):
        pretty_print(solution)
        print("Solution found at: ", time.time() - init, "seconds.")
    print("<TERMINDADO>")  # Espera a ver este mensaje para saber que el programa ha terminado
    print("Program ended asudoku_easy.pyt: ", time.time() - init, "seconds.")
