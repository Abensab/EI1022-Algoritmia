import time
from random import randint, seed
from typing import *
from Utils.bab_scheme import BabPartialSolution, BabSolver, Solution


#  IMPORTANTE:
# Para facilitar la implementación y no tener que trabajar con un nivel adicional de índices, 
# asumiremos que los objetos (listas W y V) están ordenados de mayor a menor ratio valor/peso.

def knapsack_bab_solve(weights, values, capacity):
    class KnapsackBabPS(BabPartialSolution):
        def __init__(self, decisions: Tuple[int, ...], current_weight: int, current_value: int):
            self.decisions = decisions
            self.current_weight = current_weight
            self.current_value = current_value
            self.n = len(decisions)
            self._pes = self.calc_pes_bound()
            self._opt = self.calc_opt_bound()

        # TODO: IMPLEMENTAR - relajar problema (resolver mochila continua para los objetos que quedan)
        def calc_opt_bound(self) -> Union[int, float]:
            weight = self.current_weight
            value = self.current_value
            for i in range(self.n, len(weights)):
                if weight+weights[i] <= capacity:
                    weight += weights[i]
                    value += values[i]
                else:
                    value += (values[i]*(capacity-weight))/weights[i]
                    break
            return value
            # return self.current_value + sum(values[self.n:])

        # TODO: IMPLEMENTAR - utilizar algoritmo voraz (visto en el tema de voraces)
        def calc_pes_bound(self) -> Union[int, float]:
            weight = self.current_weight
            value = self.current_value
            for i in range(self.n, len(weights)):
                if weight + weights[i] <= capacity:
                    weight += weights[i]
                    value += values[i]
            return self.current_value  # AHORA ES DEMASIADO PESIMISTA (asume que no puede coger nada más de lo que queda)
            # return self.current_value
        def is_solution(self) -> bool:
            return self.n == len(values)

        def get_solution(self) -> Solution:
            return self.current_value, self.current_weight, self.decisions

        def successors(self) -> Iterable["KnapsackBabPS"]:
            if self.n < len(values):
                if weights[self.n] <= capacity - self.current_weight:
                    yield KnapsackBabPS(self.decisions + (1,), self.current_weight + weights[self.n],
                                        self.current_value + values[self.n])
                yield KnapsackBabPS(self.decisions + (0,), self.current_weight, self.current_value)

    initial_decisions = ()
    initial_weight = 0
    initial_value = 0
    initial_ps = KnapsackBabPS(initial_decisions, initial_weight, initial_value)
    return BabSolver.solve_maximization(initial_ps)


def sorted_by_dec_ratio(w_old, v_old):
    idxs = sorted(range(len(w_old)), key=lambda i: -v_old[i] / w_old[i])
    w_new = [w_old[i] for i in idxs]
    v_new = [v_old[i] for i in idxs]
    return w_new, v_new


def create_knapsack_problem(num_objects):
    seed(5)
    w_new = [randint(10, 100) for _ in range(num_objects)]
    v_new = [w_new[i] * randint(1, 4) for i in range(num_objects)]
    capacity = int(sum(w_new) * 0.3)
    weights, values = sorted_by_dec_ratio(w_new, v_new)
    return weights, values, capacity


# PROGRAMA PRINCIPAL -------------------------------------------------------
if __name__ == "__main__":
    start = time.time()
    # Tres instancias del problema. Descomenta la que quieras resolver:
    # W, V, C = [2, 1, 6, 5, 6], [4, 1, 3, 2, 2], 10  # Solution: value = 8, weight = 9, decisions = (1, 1, 1, 0, 0)
    # W, V, C = create_knapsack_problem(20)          # Solution: value = 1118, weight = 344, decisions = (1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0)
    W, V, C = create_knapsack_problem(5000)          # Solution: value = 1830, weight = 543, decisions = (1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    print("PROBLEM:")
    print("\tNum. objects:", len(W))
    print("\tKnapsack capacity:", C)

    print("\nStart B&B...")
    solution_value, solution_weight, solution_decisions = knapsack_bab_solve(W, V, C) #Could be return none, it generates a exception bc pretends assign none to 3 params

    print("\tSolution: value = {0}, weight = {1}, decisions = {2}".format(solution_value, solution_weight,
                                                                          solution_decisions))
    print("...END.", time.time()-start)
