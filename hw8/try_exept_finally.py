try:
    print('='*10)
    file = open('file.txt', encoding="utf-8")
    print(file.read())
    file.close()
except FileNotFoundError:
    print('File not found')
finally:
    print('='*10)


print('Continue')
