class MyCustomException:
    def __enter__(self):
        print('=' * 10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('=' * 10)
        if exc_type:
            print(f'{exc_val}')
        return True


with MyCustomException():
    a = 1
    b = 2
    # c = 3
    print(a ** b ** c)

print('End of program')
