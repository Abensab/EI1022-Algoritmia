def find_peek(v):
    def rec(b: int, e: int):
        if e - b == 1:
            return b, v[b]
        h = (b + e) // 2
        if (v[h] >= v[h - 1]):
            return rec(h, e)
        return rec(b, h)

    return rec(0, len(v))


if __name__ == "__main__":
    lists = {
        'v1': [10, 20, 15, 2, 23, 90, 67],
        'v2': [7, 7, 7, 7, 7, 7, 7, 7],
        'v3': [5, 4, 3, 2, 1, 0],
        'v4': [0, 1, 2, 3, 4, 5, 6, 7]
    }
    for k, v in lists.items():
        print(k, ':', find_peek(v))
