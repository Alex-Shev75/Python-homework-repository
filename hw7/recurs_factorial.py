def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


res = int(input('====\nEnter number - '))
print(f'====\n{res}! = {factorial(res)}')