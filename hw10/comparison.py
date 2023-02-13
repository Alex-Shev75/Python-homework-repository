class User:
    def __init__(self, user):
        self.user = user

    def __eq__(self, other):
        return self.user.lower() == other.user.lower()


first_user = User('joker')
second_user = User('JOKER')
print(first_user == second_user)
