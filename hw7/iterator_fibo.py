class Fibo:
    def __init__(self, fibo_max=0):
        self.a = 0
        self.b = 1
        self.c = 0
        self.fibo_max = fibo_max

    def __iter__(self):
        return self

    def __next__(self):
        if self.c < self.fibo_max:
            self.c = self.a
            self.a = self.b
            self.b = self.c + self.a
            return self.c
        else:
            raise StopIteration


sq = Fibo(int(input('====\nEnter the maximum value for sequence - ')))
lst_sq = list(sq)
lst_sq.pop()
print(*lst_sq, sep=', ')
while True:
    sel = int(input('====\nEnter command:\n'
                    '1 - to get the value by index\n'
                    '2 - to get the index by value\n'
                    '- '))
    if sel == 1:
        index = int(input('====\nEnter index - '))
        if index < len(lst_sq):
            print(f'Index `{index}` corresponds number `{lst_sq[index]}`')
            break
        else:
            print('Index out of sequence')
    elif sel == 2:
        number = int(input('====\nEnter value - '))
        if number in lst_sq:
            print(f'Number `{number} corresponds index `{lst_sq.index(number)}`')
            break
        else:
            print('The number is not in the sequence')
    else:
        print(False)