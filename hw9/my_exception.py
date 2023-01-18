from _datetime import datetime


class MyException:
    def __enter__(self):
        print("=" * 10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = datetime.now()
        if exc_type:
            print(f'Error - \"{exc_val}\" a occurred at {t.strftime("%H:%M:%S")}')
            log = str(f'Error - \"{exc_val}\" occurred at {t.strftime("%H:%M:%S")}')
            with open('file.txt', 'x') as exc_file:
                exc_file.write(log)
        print('=' * 10)
        return True


with MyException():
    a = 1
    b = 2
    # c = 3
    print(a ** b ** c)

print('\nEnd of program')
