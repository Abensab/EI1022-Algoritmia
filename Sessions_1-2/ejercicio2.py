l = []
a = int(input())
while a > 0:
    l.append(a)
    a = int(input())
l.sort()
for item in l:
    print(item)
