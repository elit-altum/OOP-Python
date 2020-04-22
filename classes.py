# works with classes and OOP
class Player:
    membership = True  # class object attributes (not dynamic)

    def __init__(self, name='Anonymous', age=0):  # constructor / initializer
        self.name = name  # class attributes
        self.age = age

    def run(self):  # class methods
        return f'Hey there, {self.name}!'

    # class and static methods can be used directly on the class
    @classmethod
    def age_initaliser(cls, name, birth_year, current_year):
        age = current_year - birth_year
        # returns an instance of Player [cls refers to Player]
        return cls(name, age)

    @staticmethod
    # similar to @classmethod but does not get 'cls' as a parameter [can't refer to class]
    def age_calculate(birth_year, current_year):
        return current_year - birth_year


player_1 = Player('Manan', 19)
print(player_1.membership)

player_1.membership = False
print(player_1.membership)

print(player_1.run())
print(player_1.age_calculate(2000, 2019))

# initializing an object using classmethod
# class and static methods can be used directly on the class
player_2 = Player.age_initaliser('Rajesh', 2000, 2020)
print(player_2.name)
