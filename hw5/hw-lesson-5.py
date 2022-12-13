"""
loops
"""
import time

text = input('Please enter some text: ')
for i in text:
    if i.isdigit():
        i = int(i)
        if i % 2 == 0:
            print(f'You entered even number - "{i}"')
        else:
            print(f'You entered odd number  - "{i}"')
    elif i.isalpha():
        i = str(i)
        if i.istitle():
            print(f'You entered capital letter - "{i}"')
        else:
            print(f'You entered small letter   - "{i}"')
    else:
        print(f'You entered symbol - "{i}"')

print('\n')
print('== If you want to stop the next program - pres Ctrl+F2 ==\n')
a = 'I love Python'
while a:
    time.sleep(4.2)
    print(a)

