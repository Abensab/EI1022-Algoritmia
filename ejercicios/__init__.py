from typing import *

from Utils.bt_scheme import PartialSolution, Solution, BacktrackingSolver


def sumandos_solver(S, lista_numeros):
    class BuscaSumandosPS(PartialSolution):
        def __init__(self, solution, quedan):
            self.solution = solution
            self.quedan = quedan
            self.n = len(solution)

        def is_solution(self) -> bool:
            return self.quedan == S

        def get_solution(self) -> Solution:
            return self.solution

        def successors(self) -> Iterable["KnapsackPS"]:
            for item in lista_numeros[self.n]:
                if item + self.suma <= S:
                    yield BuscaSumandosPS(self.solution + (item,), self.quedan + item)

    initialPS = BuscaSumandosPS((), 0)  # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingSolver.solve(initialPS)
