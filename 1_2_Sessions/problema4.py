from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo
from Utils.graph2dviewer import Graph2dViewer
from Utils.printing import format_matrix


def horse_graph(rows, cols):
    edges = []
    jumps = [(1, -2), (2, -1), (2, 1), (1, 2)]
    for r in range(rows):
        for c in range(cols):
            for (ri, ci) in jumps:
                if r + ri < rows and 0 <= c + ci < cols:
                    edges.append(((r, c), (r + ri, c + ci)))

    return UndirectedGraph(E=edges)


def jump_matrix(grafo, num_rows, num_cols):
    m = []
    v_inicial = (0, 0)
    for r in range(num_rows):
        m.append([0] * num_cols)

    vertices = []
    queue = Fifo()
    seen = set()
    queue.push(v_inicial)
    seen.add(v_inicial)
    while len(queue) > 0:
        v = queue.pop()
        vertices.append(v)
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                m[suc[0]][suc[1]] = m[v[0]][v[1]] + 1
                queue.push(suc)
    return m


def travel_vertex_width(grafo, v_inicial):
    edges = []
    queue = Fifo()
    seen = set()
    queue.push(v_inicial)
    seen.add(v_inicial)
    while len(queue) > 0:
        v = queue.pop()
        edges.append(v)
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push(suc)
    return edges


def num_achievable_spaces(graph, v_initial):
    return len(travel_vertex_width(graph, v_initial))


if __name__ == '__main__':
    num_rows = 8
    num_cols = 8
    table_graph = horse_graph(num_rows, num_cols)

    source = (0, 3)
    print("Número de casillas alcanzable desde", source, ": ", num_achievable_spaces(table_graph, source))
    matrix = jump_matrix(table_graph, num_rows, num_cols)

    print(format_matrix(matrix))
    viewer = Graph2dViewer(table_graph, window_size=(400, 400), vertexmode=Graph2dViewer.ROW_COL)
    viewer.run()
