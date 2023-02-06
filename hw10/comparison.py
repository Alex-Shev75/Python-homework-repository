class User:
    def __init__(self, user):
        self.user = user.lower()
        self.user = user.upper()

    def __eq__(self, other):
        return self.user == other


first_user = User('joker')
second_user = User('JOKER')
print(first_user == second_user)
