def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v

print(hypervolume(3))
print(hypervolume(3, 4))
print(hypervolume(3, 4, 5))
print(hypervolume(3, 4, 5, 6))
print(hypervolume())