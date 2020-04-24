# using the map() built-in python function
# handles the func_programming pure function more simply


def multiply_by_2(item):
    return item * 2


print(list(map(multiply_by_2, [1, 2, 3])))
