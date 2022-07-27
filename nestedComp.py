vals = [[y * 3 for y in range(x)] for x in range(10)]
print(vals)

outer = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y * 3)
    outer.append(inner)
print(outer)

data1 = {x * y for x in range(10) for y in range(10)}
print(data1)

data2 = ((x, y) for x in range(10) for y in range(x))
print(list(data2))