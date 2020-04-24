# writing pure functions for functional programming
def multiply_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)

    return new_list


print(multiply_by_2([1, 2, 3, 4]))
