# inheritance in classes
class User:
    def __init__(self, email):
        print('Player')
        self._email = email

    def get_email(self):
        return self._email


class Wizard(User):
    def __init__(self, email):
        print(super())
        super().__init__(email)
        print('Wizard')

    def attack(self, power):
        return f'You have only {power} energy left.'


wizard_1 = Wizard('s.manan3')
print(wizard_1.get_email())
