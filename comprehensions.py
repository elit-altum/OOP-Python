# list comprehensions

# squaring numbers
my_list = [num**2 for num in range(1, 10)]
print(my_list)

# squaring and only using odd numbers
my_list2 = [num**2 for num in [1, 2, 3] if num % 2]
print(my_list2)


# set comprehensions
my_set = {num*2 for num in [1, 2, 3, 4, 1, 2] if num > 1}
print(my_set)  # duplicate values are removed in a set

# dictionary comprehension
dict_1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

my_dict = {k: v*2 for k, v in dict_1.items() if v > 2}
print(my_dict)
