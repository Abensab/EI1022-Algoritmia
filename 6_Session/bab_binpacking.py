import time
from math import ceil

from Utils.bab_scheme import BabPartialSolution, BabSolver, Solution
from random import seed, randint
from itertools import groupby
from typing import *


def binpacking_solve(objects: List[int], capacity: int):
    class BinPackingBabPS(BabPartialSolution):
        def __init__(self, decisions: Tuple[int, ...], container_weights: Tuple[int, ...]):
            self.decisions = decisions
            self.container_weights = container_weights
            self.n = len(decisions)
            self._opt = self.calc_opt_bound()
            self._pes = self.calc_pes_bound()

        # TODO: IMPLEMENTAR - Relaja el problema. Trata los objetos que quedan como si fueran un líquido
        def calc_opt_bound(self) -> Union[int, float]:
            max_hueco = 0
            if len(self.container_weights) > 0:
                max_hueco = capacity - min(self.container_weights)
            suma_objs_caben = suma_objs_nocaben = 0
            for i in range(self.n, len(objects)):
                if objects[i] <= max_hueco:
                    suma_objs_caben += objects[i]
                else:
                    suma_objs_nocaben += objects[i]

            for p in self.container_weights:
                espacio_libre_contenedor = capacity - p
                if espacio_libre_contenedor >= objects[-1]:
                    suma_objs_caben -= min(suma_objs_caben, espacio_libre_contenedor)
            return len(self.container_weights) + ceil((suma_objs_caben + suma_objs_nocaben) / capacity)

            # return len(self.container_weights)  # AHORA ES DEMASIADO OPTIMISTA

        # TODO: IMPLEMENTAR - Algoritmo voraz. Completa la solución parcial actual con "En el primero en el que quepa"
        def calc_pes_bound(self) -> Union[int, float]:
            container_weigths = list(self.container_weights[:]) + [0]*(len(objects)-self.n)
            for i in range(self.n, len(objects)):
                for j, size in enumerate(container_weigths):
                    if container_weigths[j] + objects[i] <= capacity:
                        container_weigths[j] += objects[i]
                        break
            return len(container_weigths)
            #return len(self.container_weights) + (len(objects) - self.n)  # AHORA ES DEMASIADO PESIMISTA

        def is_solution(self) -> bool:
            return self.n == len(objects)

        def get_solution(self) -> Solution:
            return self.decisions

        def successors(self) -> Iterable["BinPackingBabPS"]:
            if self.n < len(objects):
                object_weight = objects[self.n]
                for num_container, container_weight in enumerate(self.container_weights):
                    if container_weight + object_weight <= capacity:
                        list_cw = list(self.container_weights)  # copia tupla a lista
                        list_cw[num_container] += object_weight
                        yield BinPackingBabPS(self.decisions + (num_container,), tuple(list_cw))
                num_container = len(self.container_weights)
                yield BinPackingBabPS(self.decisions + (num_container,), self.container_weights + (object_weight,))

    initial_ps = BinPackingBabPS((), ())
    return BabSolver.solve_minimization(initial_ps)


def show_solution_grouped_by_containers(sol):
    print("\nSOLUTION GROUPED BY CONTAINERS (shows the weights of objects in each container):")
    for pos, g in groupby(sorted([o, i] for i, o in enumerate(sol)), lambda e: e[0]):
        print("\t{}: {}".format(pos, [objs[e[1]] for e in g]))


def create_exact_binpacking_problem(num_containers, objects_per_container):
    seed(5)
    objects = []
    num_c = num_containers
    num_e_c = objects_per_container
    min_v = 25
    max_v = 35
    capacity = max_v * num_e_c + 0
    for ic in range(num_c):
        s = 0
        for ie in range(num_e_c - 1):
            o = randint(min_v, max_v)
            objects.append(o)
            s += o
        objects.append(capacity - s)
    return capacity, sorted(objects, reverse=True)


# PROGRAMA PRINCIPAL -------------------------------------------------------
if __name__ == "__main__":
    start = time.time()
    # Descomenta la instancia del problema que quieras resolver:
    # C, objs = 10, [6, 6, 3, 3, 2, 2, 2, 2, 2, 2]  # SOLUCIÓN ÓPTIMA: 3 contenedores
    # C, objs = create_exact_binpacking_problem(6, 3)  # SOLUCIÓN ÓPTIMA: 6 contenedores
    C, objs = create_exact_binpacking_problem(12, 3) # SOLUCIÓN ÓPTIMA: 12 contenedores

    print("PROBLEM TO SOLVE:")
    print("\tContainer capacity:", C)
    print("\tObjects (weights):", objs)

    solution = binpacking_solve(objs, C)

    print("\nBEST SOLUTION:")
    print("\tB&B solution: {0} containers. Details: {1}".format(max(solution) + 1, solution))
    print("Time: ", time.time() -start)

    show_solution_grouped_by_containers(solution)
