"""
Homework-4: text type, even/odd, length
"""
text = input('Please enter a word or a number - ')
a = text
if text.isdigit():
    text = int(text)
    if text % 2 == 0:
        print(f'You entered the even number - {text}')
    else:
        print(f'You entered the odd number - {text}')
else:
    print(f'You entered the word \'{a}\' consisting of {len(text)} letters')
