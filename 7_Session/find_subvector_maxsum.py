def find_subvector_maxsum(v):
    def rec(b: int, e: int):
        if e-b==1:
            return b
        h=(b+e)//2
        m_izq = rec(b, h)
        m_der = rec(h, e)
        m_mitad = whiles ricos

    return rec(0, len(v))

def get_beter_half(b,e):

if __name__=="__main__":
    lists= {
        'v1': [2, 3, 3, 4, 5, 10],
        'v2': [100, 101, 102, 103],
        'v3': [2, 3, 4, 5, 6, 7],
        'v4': [-10, -5, 1, 3, 6]
    }
    for k, v in lists.items():
        print(k,':', find_subvector_maxsum(v))
