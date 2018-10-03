def first(n, iter):
    for elem in iter:
        if n==0: break
        yield elem
        n-=1


def filter(cond, iter):
    for elem in iter:
        if cond(elem):
            yield elem

def take_while(cond, iter):
    for elem in iter:
        if not cond(elem): break
        yield elem


def squares():
    i=0
    while True:
        yield i**2
        i+=1


cuadrados = squares()
a=first(100, squares())
b=take_while(lambda n: n<100,squares())
c=first(20, filter(lambda n: str(n)[::-1]==str(n), squares()))
print(list(a))
print(list(b))
print(list(c))
