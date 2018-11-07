from Utils.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution
from typing import *
from random import random, seed
import time


def knapsack_solve(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self, solution, weight, value, index):
            self.solution = solution
            self.weight = weight
            self.value = value
            self.index = index

        def is_solution(self) -> bool:
            return self.index == len(values)


        def get_solution(self) -> Solution:
            return self.value, self.weight, self.solution

        def successors(self) -> Iterable["KnapsackPS"]:
            if not self.is_solution():
                if (self.weight + weights[self.index]) <= capacity:
                    yield KnapsackPS(self.solution + (self.index,), self.weight + weights[self.index], self.value + values[self.index], self.index+1)
                yield KnapsackPS(self.solution, self.weight, self.value, self.index+1)

        def state(self) -> State:  # IMPLEMENTAR
            # return self # No utilzar
            return self.index, self.weight

        def f(self) -> Union[int, float]:  # IMPLEMENTAR
            return -self.value

    initialPS = KnapsackPS((), 0, 0, 0)  # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)


def create_knapsack_problem(num_objects: int) -> Tuple[Tuple[int, ...], Tuple[int, ...], int]:
    seed(42)
    weights = [int(random() * 1000 + 1) for _ in range(num_objects)]
    values = [int(random() * 1000 + 1) for _ in range(num_objects)]
    capacity = sum(weights) // 2
    return weights, values, capacity


# Programa principal ------------------------------------------
if __name__ == "__main__":
    #Best solution = (1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1)
    #Best solution advanced = (11824, 6313, (0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 19, 22, 23, 24, 25, 26, 27, 29))
    start = time.time()
    #W, V, C = [1, 4, 2, 3], [2, 3, 4, 2], 7  # SOLUCIÓN: Weight=7,    Value=9
    W, V, C = create_knapsack_problem(30)     # SOLUCIÓN: Weight=6313, Value=11824
    for sol in knapsack_solve(W, V, C):
        print(sol)
    print("\n<TERMINADO EN", time.time()-start,"s>")

