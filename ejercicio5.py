def myfunction(a, b):
    a = 2* a
    b[0] = 10
    b.append(0)
    b = list(range(3))
    return b*a

x = 1
y = list(range(6))
print(x, y)
print(myfunction(x, y))
print(x, y)
