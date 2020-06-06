from typing import Iterable

from Utils.bt_scheme import PartialSolutionWithVisitedControl, BacktrackingSolver, BacktrackingVCSolver, Solution, State
from algoritmia.datastructures.digraphs import UndirectedGraph


def hamiltonian_cycle(g : UndirectedGraph, vertex : int):
    class Hamyltonian_cycle_PS(PartialSolutionWithVisitedControl):
        def __init__(self,):


        def is_solution(self) -> bool:
            return

        def get_solution(self) -> Solution:
            pass

        def successors(self) -> Iterable["PartialSolutionWithVisitedControl"]:
            pass

        def state(self) -> State:
            pass


if __name__ == "__main__":
    g = UndirectedGraph(V=[1,2,3,4], E=[(1,1)])
