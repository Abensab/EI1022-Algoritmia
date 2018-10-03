from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo

from Utils.graph2dviewer import Graph2dViewer


def horse_graph(rows, cols):
    edges = []
    saltos = [(1, -2), (2, -1), (2, 1), (1, 2)]
    for r in range(rows):
        for c in range(cols):
            for (ri, ci) in saltos:
                if r + ri < rows and 0 <= c + ci < cols:
                    edges.append(((r, c), (r + ri, c + ci)))

    return UndirectedGraph(E=edges)


def matriz_saltos(grafo, num_rows, num_cols):
    m = []
    v_inicial = (0, 0)
    for r in range(num_rows):
        m.append([0] * num_cols)

    # TODO: añadir matriz de saltos
    vertices = []
    queue = Fifo()
    seen = set()
    queue.push(v_inicial)
    seen.add(v_inicial)
    salto = 1
    while len(queue) > 0:
        v = queue.pop()
        vertices.append(v)
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                m[suc[0]][suc[1]] = salto
                queue.push(suc)
        salto += 1
    # ---------------

    return m


def recorredor_vertices_anchura(grafo, v_inicial):
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
                queue.push(suc)
    return vertices


def num_casillas_alcanzables(grafo, v_inicial):
    return len(recorredor_vertices_anchura(grafo_tablero, v_inicial))


if __name__ == '__main__':
    num_rows = 8
    num_cols = 8
    grafo_tablero = horse_graph(num_rows, num_cols)

    source = (0, 3)
    print("Número de casillas alcanzable desde", source, ": ", num_casillas_alcanzables(grafo_tablero, source))
    matriz = matriz_saltos(grafo_tablero, num_rows, num_cols)

    [print(i) for i in matriz]
    viewer = Graph2dViewer(grafo_tablero, window_size=(400, 400), vertexmode=Graph2dViewer.ROW_COL)
    viewer.run()
