# works with lambda expressions!

# squaring a list
my_list = [5, 4, 3, 2, 1]

print(list(map(lambda item: item * item, my_list)))

# sorting lists with lambda
tuple_list = [(0, 2), (4, 3), (9, 9), (10, -1)]

tuple_list.sort(key=lambda x: x[1])
print(tuple_list)
