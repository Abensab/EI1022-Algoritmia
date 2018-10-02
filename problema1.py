from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from Utils.labyrinthviewer import LabyrinthViewer
import random


def create_labyrinth(rows: int, cols: int) -> UndirectedGraph:
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
    for (u, v) in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))

    return UndirectedGraph(E=corridors)


if __name__ == '__main__':
    rows = 40
    cols = 60
    graf = create_labyrinth(rows, cols)
    source = (0, 0)
    target = (rows - 1, cols - 1)
    viewer = LabyrinthViewer(graf, canvas_width=800, canvas_height=480, margin=10)
    viewer.run()
