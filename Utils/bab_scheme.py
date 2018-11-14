"""
Created on Nov 2, 2018

@author: David Llorens (dllorens@uji.es)
         (c) Universitat Jaume I 2018
@license: GPL2
"""
from Utils.bt_scheme import PartialSolution  # Importamos PartialSolution del backtracking
from algoritmia.datastructures.priorityqueues import MaxHeap, MinHeap
from functools import total_ordering
from typing import *

Solution = TypeVar('Solution')


@total_ordering
class BabPartialSolution(PartialSolution):
    # 
    # Nota: Para no repetir cálculos, y dado que son inmutables, las cotas se deberían calcular 
    #       sólo una vez (en el constructor de la PS) y almacenarse (atributos self._opt y self._pes). 
    #       Los métodos opt() y pes() sólo devuelven el valor de estos atributos.
    #

    # Optimistic bound. Must be iqual to f() for full solutions
    def opt(self) -> Union[int, float]:
        return self._opt

    # Pessimistic bound. Must be iqual to f() for full solutions
    def pes(self) -> Union[int, float]:
        return self._pes

    def __lt__(self, other) -> bool:
        return self.opt() < other.opt()

    def __eq__(self, other) -> bool:
        return self.opt() == other.opt()


class BabSolver:
    @staticmethod
    def solve_maximization(initial_ps: BabPartialSolution) -> Solution:
        heap = MaxHeap()
        heap.add(initial_ps)
        bps = initial_ps.pes()
        while len(heap) > 0:
            best_ps = heap.extract_opt()
            if best_ps.is_solution():
                return best_ps.get_solution()
            for new_ps in best_ps.successors():
                bps = max(bps, new_ps.pes())
                if new_ps.opt() >= bps:
                    heap.add(new_ps)

    @staticmethod
    def solve_minimization(initial_ps: BabPartialSolution) -> Solution:
        heap = MinHeap()
        heap.add(initial_ps)
        bps = initial_ps.pes()
        while len(heap) > 0:
            best_ps = heap.extract_opt()
            if best_ps.is_solution():
                return best_ps.get_solution()
            for new_ps in best_ps.successors():
                bps = min(bps, new_ps.pes())
                if new_ps.opt() <= bps:
                    heap.add(new_ps)
