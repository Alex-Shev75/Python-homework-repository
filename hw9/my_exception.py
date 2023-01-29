from _datetime import datetime


def exception():
    print("=" * 10)
    try:
        a = int(input('Enter any number - '))
        b = int(input('Enter any number - '))
        return print(a / b)
    except ZeroDivisionError as err_1:
        t = datetime.now()
        print(f'Error - {err_1} - occurred at {t.strftime("%H:%M:%S")}')
        log_1 = str(f'Error - {err_1} - occurred at {t.strftime("%H:%M:%S")}')
        try:
            with open('file.txt', 'x+') as save_err:
                save_err.write(log_1)
        except FileExistsError:
            with open('file.txt', 'a+') as save_err:
                save_err.write(f'\n{log_1}')
    except ValueError as err_2:
        t = datetime.now()
        print(f'Error - {err_2} - occurred at {t.strftime("%H:%M:%S")}')
        log_2 = str(f'Error - {err_2} - occurred at {t.strftime("%H:%M:%S")}')
        with open('file.txt', 'a+') as save_err:
            save_err.write(f'\n{log_2}')
    finally:
        print("=" * 10)


exception()
print('Program completed')
