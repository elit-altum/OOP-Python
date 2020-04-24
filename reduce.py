# reduce function in python
# importing reduce()

from functools import reduce

my_list = [5, 6, 7, 8]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
