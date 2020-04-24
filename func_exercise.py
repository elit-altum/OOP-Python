# complex functions exercise
from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize_word(word):
    return word.upper()


print(list(map(capitalize_word, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

sorted_numbers = sorted(my_numbers)

print(list(zip(sorted_numbers, my_strings)))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over_50(score):
    return score > 50


print(list(filter(over_50, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item


def list_sum(li):
    return reduce(accumulator, li, 0)


print(list_sum(my_numbers + scores))
