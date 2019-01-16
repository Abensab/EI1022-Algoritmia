from Utils.bt_scheme import PartialSolutionWithVisitedControl, BacktrackingVCSolver, State, Solution
from typing import *


def problema(C: List[int], A: int, B: int):
    class SumaDosEnteros(PartialSolutionWithVisitedControl):
        def __init__(self, quedan_a: int, quedan_b: int, sa: List[int], sb: List[int], index):
            self.quedan_a = quedan_a
            self.quedan_b = quedan_b
            self.sa = sa
            self.sb = sb
            self.index = index

        def is_solution(self) -> bool:
            return self.quedan_a == 0 and self.quedan_b == 0

        def get_solution(self) -> Solution:
            return self.sa, self.sb

        def successors(self) -> Iterable["PartialSolution"]:
            print(self.index)
            print("A:", self.quedan_a)
            print("B:", self.quedan_b)
            if not self.is_solution() and self.index < len(C):
                if self.quedan_a - C[self.index] >= 0:
                    self.quedan_a -= C[self.index]
                    self.sa.append(C[self.index])
                elif self.quedan_b - C[self.index] >= 0:
                    self.quedan_b -= C[self.index]
                    self.sb.append(C[self.index])

                yield SumaDosEnteros(self.quedan_a, self.quedan_b, self.sa, self.sb, self.index + 1)

        def state(self) -> State:
            return self.quedan_a, self.quedan_b, self.index

    return BacktrackingVCSolver.solve(SumaDosEnteros(A, B, [], [], 0))


if __name__ == "__main__":
    C = [3, 1, 15, 18, 14, 23, 11, 10, 17]
    A = 3
    B = 1
    for sol in problema(C, A, B):
        print(sol)

