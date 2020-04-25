# printing duplicates from a list

some_list = ['a', 'b', 'c', 'b', 'n', 'n']


# converts list to set then back to list
new_list = list(set([x for x in some_list if some_list.count(x) > 1]))

print(new_list)
