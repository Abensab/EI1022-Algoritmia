from algoritmia.datastructures.mergefindsets import MergeFindSet
from easycanvas import EasyCanvas
from random import shuffle


def vecinos(v1, v2):
    if(v1[0]==v2[0]):
        return 0
    elif(v1[1]==v2[1]):
        return 1
    return None

def create_labyrinth(rows, cols):
    vertices = list((i, j) for i in range(0, rows) for j in range(0, cols))
    mfs = MergeFindSet()
    for v in vertices:
        mfs.add(v)

    edges=[]
    for i in range(rows):
        for j in range (cols):
            edges.append(((i,j),(i,j+1))) if j+1<cols else ""
            edges.append(((i,j),(i+1,j))) if i+1<cols else ""
    shuffle(edges)
    corridors=[]
    #for a in edges:

    print(edges)
    print(set)


create_labyrinth(10, 10)
