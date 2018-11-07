from algoritmia.datastructures.digraphs import UndirectedGraph
from FirstSession.problema1 import create_labyrinth
from Utils.labyrinthviewer import LabyrinthViewer


def path(g: UndirectedGraph, source: "T", target: "T") -> "List<T>":
    la = traveler_edges_depth(g, source)
    bp = {}
    for (u, v) in la:
        bp[v] = u
    road = []
    v = target
    road.append(v)
    while bp[v] != v:
        v = bp[v]
        road.append(v)

    return road


def traveler_edges_depth(ug: UndirectedGraph, v_initial):
    def travel_from(u, v):
        seen.add(v)
        edges.append((u, v))
        for suc in ug.succs(v):
            if suc not in seen:
                travel_from(v, suc)

    edges = []
    seen = set()
    travel_from(v_initial, v_initial)
    return edges


if __name__ == '__main__':
    rows = 40
    cols = 60
    graf = create_labyrinth(rows, cols)
    source = (0, 0)
    target = (rows - 1, cols - 1)
    road = path(graf, source, target)
    viewer = LabyrinthViewer(graf, canvas_width=800, canvas_height=480, margin=10)
    viewer.add_path(road, color='blue')
    viewer.run()
