import sys
from typing import *

from Utils.bt_scheme import PartialSolution, BacktrackingSolver, Solution  ##ARREGLAR PARA QUITAR UTILS?


def distribucion_solve(almacenA, almacenB, fabricas, costeA, costeB, componentes):
    class DistribucionPS(PartialSolution):
        def __init__(self, coste, solucion, almacenA, almacenB, fabricas, costeA, costeB, componentes):
            self.coste = coste
            self.solucion = solucion
            self.almacenA = almacenA
            self.almacenB = almacenB
            self.fabricas = fabricas
            self.costeA = costeA
            self.costeB = costeB
            self.componentes = componentes

        def is_solution(self) -> bool:
            return len(self.solucion) == self.fabricas

        def get_solution(self) -> Solution: #Tuple[int, List[Tuple[int, int]]]:
            return (self.coste, self.solucion)

        def successors(self) -> Iterable["DistribucionPS"]:
            if not self.is_solution():
                fabrica = len(self.solucion)
                if self.componentes[fabrica] < self.almacenA:
                    if self.componentes[fabrica] < self.almacenB:
                        n_comp = 0
                        while n_comp <= componentes[fabrica]:
                            coste_transporte = (self.costeA[fabrica] * n_comp) + self.costeB[fabrica] * (self.componentes[fabrica]-n_comp)
                            s = self.solucion[:]
                            s.append((n_comp, self.componentes[fabrica]-n_comp))
                            yield DistribucionPS(
                                self.coste + coste_transporte,
                                s,
                                self.almacenA-n_comp,
                                self.almacenB-(self.componentes[fabrica]-n_comp),
                                self.fabricas,
                                self.costeA,
                                self.costeB,
                                self.componentes
                            )
                            n_comp += 1

                    else:
                        n_comp = 0
                        #         for hasta almacenB
                        while n_comp <= self.almacenB:
                            coste_transporte = (self.costeA[fabrica] * (self.componentes[fabrica]-(self.almacenB-n_comp))) + \
                                               self.costeB[fabrica] * (self.almacenB-n_comp)
                            s = self.solucion[:]
                            s.append(((self.componentes[fabrica]-(self.almacenB-n_comp), (self.almacenB-n_comp))))
                            yield DistribucionPS(
                                self.coste + coste_transporte,
                                s,
                                self.almacenA-(self.componentes[fabrica]-(self.almacenB-n_comp)),
                                self.almacenB-(self.almacenB-n_comp),
                                self.fabricas,
                                self.costeA,
                                self.costeB,
                                self.componentes
                            )
                            n_comp += 1
                else:
                    n_comp = 0
                    #     for hasta almacenA
                    while n_comp <= self.almacenA:
                        coste_transporte = (self.costeA[fabrica] * (self.almacenA-n_comp)) + \
                                           self.costeB[fabrica] * (self.componentes[fabrica]-(self.almacenA-n_comp))
                        s = self.solucion[:]
                        s.append(((self.almacenA-n_comp), (self.componentes[fabrica]-(self.almacenA-n_comp))))
                        yield DistribucionPS(
                            self.coste + coste_transporte,
                            s,
                            self.almacenA-(self.almacenA-n_comp),
                            self.almacenB-(self.componentes[fabrica]-(self.almacenB-n_comp)),
                            self.fabricas,
                            self.costeA,
                            self.costeB,
                            self.componentes
                        )
                        n_comp += 1

    initialPS = DistribucionPS(0, [], almacenA, almacenB, fabricas, costeA, costeB, componentes)
    print("hi")
    return BacktrackingSolver.solve(initialPS)

def read_file(fichero: str):
    """Dado el nombre del fichero se leen los datos y se almacenan en las variables"""
    componentes, costeA, costeB = [], [], []
    file = open(fichero, 'r')
    almacenA = int(file.readline().replace('﻿', ''))  # dudas
    almacenB = int(file.readline())
    fabricas = int(file.readline())
    for linea in file:
        var = linea.split(' ')
        for i in var:
            costeA.append(int(i))
        break
    for linea in file:
        var = linea.split(' ')
        for i in var:
            costeB.append(int(i))
        break
    for linea in file:
        var = linea.split(' ')
        for i in var:
            componentes.append(int(i))

    return almacenA, almacenB, fabricas, costeA, costeB, componentes


# ---------PROGRAMA PRINCIPAL---------
if __name__ == '__main__':
    # Comprueba que el número de parámetros leídos es válido
    if len(sys.argv) == 2:
        fichero = sys.argv[1]
        almacenA, almacenB, fabricas, costeA, costeB, componentes = read_file(fichero)
        print(almacenA, almacenB, fabricas, costeA, costeB, componentes)
        min, list, cont = None, None, 0
        for coste, lista in distribucion_solve(almacenA, almacenB, fabricas, costeA, costeB, componentes):
            cont +=1
            if min is None:
                min, list = coste, lista
            else:
                if min > coste:
                    min = coste
                    list = lista
            print(coste, lista)

        print("HEMOS ENCONTRADO ", cont, " SOLUCIONES")
        print('\n', min, list)

    else:
        print("Invalid number of parameters.")
        exit(1)
