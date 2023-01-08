def fibo_gen(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        c = a
        a = b
        b = c + a


while True: 
    sq_max = int(input('\n====\nEnter sequence length - '))
    lst_sq = list(fibo_gen(sq_max))
    index = int(input('\n=====\nEnter index number - '))
    if index >= sq_max:
        print(f'====\nIndex {index} is greater than the length of the sequence\n'
              f'chose another number')
    else:
        print(f'====\nIndex `{index}` in the "Fibonacci sequence"'
              f'\ncorresponds to the number `{lst_sq[index]}`')
        break