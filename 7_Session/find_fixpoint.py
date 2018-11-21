from typing import *


def busca_punto_fijo_rec(v):
    def rec(b: int, e: int):
        if e - b == 0:
            return None
        medio = (b + e) // 2
        if v[medio] < medio:
            return rec(medio, e)
        elif v[medio] > medio:
            return rec(b, medio)
        else:
            return medio

    return rec(0, len(v))


if __name__ == "__main__":
    lists= {
        'v1': [2, 3, 3, 4, 5, 10],
        'v2': [100, 101, 102, 103],
        'v3': [2, 3, 4, 5, 6, 7],
        'v4': [-10, -5, 1, 3, 6]
    }
    for k, v in lists.items():
        print(k,':', busca_punto_fijo_rec(v))
