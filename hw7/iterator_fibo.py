class Fibo:
    def __init__(self, fibo_googol=pow(10, 1000)):
        self.a = 0
        self.b = 1
        self.c = 0
        self.fibo_googol = fibo_googol

    def __iter__(self):
        return self

    def __next__(self):
        if self.c < self.fibo_googol:
            self.c = self.a
            self.a = self.b
            self.b = self.c + self.a
            return self.c
        else:
            raise StopIteration


sq = Fibo()
lst_sq = list(sq)
max_index = (lst_sq.index(lst_sq[-1]))
print(f'====\nThis sequence consists of {max_index} numbers')
while True:
    index = int(input('====\nEnter index - '))
    if index <= max_index:
        print(f'====\nIndex `{index}` corresponds number {lst_sq[index]}')
        print(f'===\nThis number has {len(str(lst_sq[index]))} digits')
        break
    else:
        print('====\nIndex out of sequence')
