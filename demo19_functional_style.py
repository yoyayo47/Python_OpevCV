import math

x1 = [1, 2, 3, 4, 5]

for r in map(math.sqrt, x1):
    print(r)
print([x for x in map(math.sqrt, x1)])
print(list(map(math.sqrt, x1)))


def morph(p):
    return p ** 2 + 2 * p + 5


print(list(map(morph, x1)))
print(list(map(lambda x: x ** x, x1)))

x2 = [[1, 2, 3, 1], [2, 3, 4, 4], [3, 4, 5, 5], [4, 5, 6, 6]]
print(list(map(tuple, x2)))
print(list(map(set, x2)))
