from datetime import datetime


def decorator(func):
    def wrapper(*args, **kwargs):
        t = datetime.now()
        print(f'====\nFunction call time - {t.strftime("%H:%M:%S")}\n====')
        func(*args, **kwargs)
        print(f'====\nFunction ended\n====\n')

    return wrapper


@decorator
def any_func(a, b):
    print(f'Call - `any_func`\n{a} {b}!\n')


y = datetime.now()
any_func('Happy new year', y.year)
