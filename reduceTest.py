from functools import reduce
import operator

print(reduce(operator.add, [1, 2, 3, 4, 5]))

numbers = [1, 2, 3, 4, 5]
accumulator = operator.add(numbers[0], numbers[1])
for item in numbers[2:]:
    accumulator = operator.add(accumulator, item)

print(accumulator)

def mul(x, y):
    print('mul {} {}'.format(x, y))
    return x * y
print(reduce(mul, range(1, 10)))