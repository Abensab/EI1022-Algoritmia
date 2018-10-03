from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo

from Utils.labyrinthviewer import LabyrinthViewer
import random

from problema1 import create_labyrinth
from problema2 import path


def create_labyrinth_modi(rows: int, cols: int, n: int = 0) -> UndirectedGraph:
    vertices = [(r, c) for r in range(rows) for c in range(cols)]
    mfs = MergeFindSet()
    for v in vertices:
        mfs.add(v)

    edges = []
    for (i, j) in vertices:
        edges.append(((i, j), (i, j + 1))) if j + 1 < cols else ""
        edges.append(((i, j), (i + 1, j))) if i + 1 < rows else ""

    random.shuffle(edges)
    corridors = []
    discarded_edges = []
    for (u, v) in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))
        else:
            discarded_edges.append((u, v))
    corridors.extend(discarded_edges[:n])
    return UndirectedGraph(E=corridors)


def recorredor_aristas_anchura(grafo, v_inicial):
    edges = []
    queue = Fifo()
    seen = set()
    queue.push((v_inicial, v_inicial))
    seen.add(v_inicial)
    while len(queue) > 0:
        u, v = queue.pop()
        edges.append((u, v))
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    return edges


def recuperador_camino(lista_aristas, v):
    # Create a dictionary of bakcpointers(bp)
    bp = {}
    for o, d in lista_aristas:
        bp[d] = o
    # Rebuilding the way going back
    way = [v]
    while v != bp[v]:
        v = bp[v]
        way.append(v)
    # Reverse the way because we have just obteined on te contrary
    way.reverse()
    return way


if __name__ == '__main__':
    random.seed(42)
    num_rows = 80
    num_cols = 140
    num_paredes_quitadas = 20
    source = (0, 0)
    target = (num_rows - 1, num_cols - 1)

    graf = create_labyrinth(num_rows, num_cols)
    graf_modi = create_labyrinth_modi(num_rows, num_cols, n=num_paredes_quitadas)

    camino = path(graf, source, target)
    camino_modi = recuperador_camino(recorredor_aristas_anchura(graf_modi, source), target)

    viewer = LabyrinthViewer(graf_modi, canvas_width=800, canvas_height=480, margin=10)
    viewer.add_path(camino, color="red")
    viewer.add_path(camino_modi, color="blue")
    viewer.run()
