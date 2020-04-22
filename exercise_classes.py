# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
kitty = Cat('kitty', 5)
momo = Cat('momo', 7)
tuna = Cat('tuna', 2)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    oldest = args[0]
    for cat in args:
        if cat.age > oldest.age:
            oldest = cat

    return f'The oldest cat is {oldest.age} years old.'


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(oldest_cat(kitty, momo, tuna))
