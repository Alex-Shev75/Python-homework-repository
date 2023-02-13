class MyStr(str):

    def __str__(self):
        text = self.upper()
        return text


capital_letters = MyStr('pupsik')
print(capital_letters)
