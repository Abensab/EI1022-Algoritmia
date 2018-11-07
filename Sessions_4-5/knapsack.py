from Utils.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution
from typing import *
from random import random, seed
import time

def knapsack_solve(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self, solution, weight, value):
            self.solution = solution
            self.weight = weight
            self.value = value
            self.n = len(self.solution)

        def is_solution(self) -> bool:
            return self.n == len(values)

        def get_solution(self) -> Solution:
            return self.solution

        def successors(self) -> Iterable["KnapsackPS"]:
            if not self.is_solution():
                if (self.weight + weights[self.n]) <= capacity:
                    yield KnapsackPS(self.solution + (1,), self.weight + weights[self.n], self.value + values[self.n])
                yield KnapsackPS(self.solution + (0,), self.weight, self.value)

        def state(self) -> State:  # IMPLEMENTAR
            return self.n, self.weight

        def f(self) -> Union[int, float]:  # IMPLEMENTAR
            return -self.value

    initialPS = KnapsackPS((), 0, 0)  # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)


def create_knapsack_problem(num_objects: int) -> Tuple[Tuple[int, ...], Tuple[int, ...], int]:
    seed(42)
    weights = [int(random() * 1000 + 1) for _ in range(num_objects)]
    values = [int(random() * 1000 + 1) for _ in range(num_objects)]
    capacity = sum(weights) // 2
    return weights, values, capacity


# Programa principal ------------------------------------------
if __name__ == "__main__":
    start = time.time()
    #W, V, C = [1, 4, 2, 3], [2, 3, 4, 2], 7  # SOLUCIÓN: Weight=7,    Value=9
    W, V, C = create_knapsack_problem(30)     # SOLUCIÓN: Weight=6313, Value=11824
    for sol in knapsack_solve(W, V, C):
        print(sol)
    print("\n<TERMINADO EN", time.time()-start,"s>")
