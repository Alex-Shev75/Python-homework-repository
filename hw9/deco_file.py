from datetime import datetime


def decorator(func):
    def wrapper(*args, **kwargs):
        t = datetime.now()
        print(f'====\nFunction call time - {t.strftime("%H:%M:%S")}\n====')
        with open('deco.txt', 'a+') as deco_file:
            deco_file.write(f'\nI decorate {str(func)}')
        print(f'====\nFunction ended\n====\n')
        return func(*args, **kwargs)
    return wrapper


@decorator
def any_func(a, b):
    print(f'Call - `any_func`\n{a} {b}!\n')


y = datetime.now()
any_func('Happy new year', y.year)
