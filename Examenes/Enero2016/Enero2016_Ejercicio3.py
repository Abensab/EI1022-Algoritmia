from Utils.bt_scheme import PartialSolution, BacktrackingVCSolver, State, Solution
from typing import *


class BuscaSumandosPS(PartialSolution):

    def __init__(self, solucion, quedan, indice, lista):
        self.self = self
        self.solucion = solucion
        self.quedan = quedan
        self.indice = indice
        self.lista = lista

    def is_solution(self) -> bool:
        return self.quedan == 0 and self.indice == len(self.lista)

    def get_solution(self) -> Solution:
        return self.solucion

    def successors(self) -> Iterable["PartialSolution"]:
        if not self.is_solution() and self.indice < len(self.lista):
            for i in self.lista[self.indice]:
                if self.quedan - i >= 0:
                    self.solucion.append(i)
                    self.indice += 1
                    self.quedan -= i
                    yield BuscaSumandosPS(self.solucion, self.indice, self.quedan, self.lista)
