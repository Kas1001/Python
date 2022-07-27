data1 = [(x, y) for x in range(5) for y in range(5)]
print(data1)

data2 = []
for x in range(5):
    for y in range(5):
        data2.append((x,y))
print(data2)

data3 = [(x, y) for x in range(10) for y in range(x)]
print(data3)

data4 = []
for x in range(10):
    for y in range(x):
        data4.append((x, y))
print(data4)