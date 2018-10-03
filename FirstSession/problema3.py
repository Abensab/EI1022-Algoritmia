from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from FirstSession.problema2 import path
from Utils.labyrinthviewer import LabyrinthViewer
import random


def create_labyrinth_mod(rows: int, cols: int, n: int = 0) -> UndirectedGraph:
    vertex = [(r, c) for r in range(rows) for c in range(cols)]
    mfs = MergeFindSet()
    for v in vertex:
        mfs.add(v)

    edges = []
    for (i, j) in vertex:
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

    graph_wo_mod = UndirectedGraph(E=corridors)
    new_corridors = corridors[:]
    new_corridors.extend(discarded_edges[:n])
    graph_mod = UndirectedGraph(E=new_corridors)
    return graph_wo_mod, graph_mod


def traveler_edges_width(graph, v_initial):
    edges = []
    queue = Fifo()
    seen = set()
    queue.push((v_initial, v_initial))
    seen.add(v_initial)
    while len(queue) > 0:
        u, v = queue.pop()
        edges.append((u, v))
        for suc in graph.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    return edges


def road_recuperator(edges_list, v):
    # Create a dictionary of bakcpointers(bp)
    bp = {}
    for o, d in edges_list:
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
    num_wall_remove = 1600
    source = (0, 0)
    target = (num_rows - 1, num_cols - 1)

    graf, graf_mod = create_labyrinth_mod(num_rows, num_cols, n=num_wall_remove)

    way = path(graf, source, target)
    way_mod = road_recuperator(traveler_edges_width(graf_mod, source), target)

    print("Solución: \n\t- Sin tumbar paredes:", len(way), "\n\t-Tumbando paredes:", len(way_mod))
    viewer = LabyrinthViewer(graf_mod, canvas_width=800, canvas_height=480, margin=10)
    viewer.add_path(way, color="red")
    viewer.add_path(way_mod, color="blue")
    viewer.run()
