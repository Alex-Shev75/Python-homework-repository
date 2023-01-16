class MyCtxMngr:
    def __enter__(self):
        print('=' * 10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'{exc_val}')
        print('=' * 10)
        return True


with MyCtxMngr():
    file = open('file.txt', "x")
    file.write('Hello World')
    file = open('file.txt', encoding="utf-8")
    print(file.read())

print('Continue')
