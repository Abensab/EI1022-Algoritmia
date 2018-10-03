from algoritmia.datastructures.digraphs import UndirectedGraph
from problema1 import create_labyrinth
from Utils.labyrinthviewer import LabyrinthViewer


def path(g: UndirectedGraph, source, target):
    la = recorredor_de_aristas_en_profundidad(g, source)
    bp = {}
    for (u, v) in la:
        bp[v] = u
    camino = []
    v = target
    camino.append(v)
    while bp[v] != v:
        v = bp[v]
        camino.append(v)

    return camino


def recorredor_de_aristas_en_profundidad(ug: UndirectedGraph, v_inicial):
    def recorrido_desde(u, v):
        seen.add(v)
        aristas.append((u, v))
        for suc in ug.succs(v):
            if suc not in seen:
                recorrido_desde(v, suc)

    aristas = []
    seen = set()
    recorrido_desde(v_inicial, v_inicial)
    return aristas


if __name__ == '__main__':
    rows = 40
    cols = 60
    graf = create_labyrinth(rows, cols)
    source = (0, 0)
    target = (rows - 1, cols - 1)
    camino = path(graf, source, target)
    viewer = LabyrinthViewer(graf, canvas_width=800, canvas_height=480, margin=10)
    viewer.add_path(camino, color='blue')
    viewer.run()
