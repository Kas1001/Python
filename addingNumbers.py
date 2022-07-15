from itertools import count

x = []
i = 1
for i in count():
    if i > 3:
        break
    x.append(i)

print(x)
print(sum(x))