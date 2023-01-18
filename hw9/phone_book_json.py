import json

with open('json_pb.json', 'r+') as file_open:
    my_phone_book = json.loads(file_open.read())


def user_add(user):
    if user not in my_phone_book.keys():
        if len(user) > 0:
            user_number = input(f'pls enter phone number for {user} - ')
            if len(user_number) > 3:
                my_phone_book[user] = user_number
                with open('json_pb.json', 'w') as file_add:
                    file_add.write(json.dumps(my_phone_book))
                print(f'{user} added to your phone book')
            else:
                print('Number must contain min 3 symbols')
        else:
            print('Name must contain min 1 symbol')
    else:
        print(f'{user} already exist,choose another name')


def user_del(user):
    if user in my_phone_book:
        del my_phone_book[user]
        with open('json_pb.json', 'w') as file_del:
            file_del.write(json.dumps(my_phone_book))
        print(f'{user} removed from your phone book')
    else:
        print(f'{user} not in the your phone book')


def user_information(user):
    if user in my_phone_book:
        value = my_phone_book.get(user)
        print(f'{user}`s phone number -  {value}')
    else:
        print('Subscriber not found')


def show_subscribers_list():
    for subscriber in my_phone_book:
        print(subscriber)
    if len(my_phone_book) == 0:
        print('No subscribers')


while True:
    user_command = input('\nWhat do you want to do?\n====\n'
                         '1 - Add new subscriber\n'
                         '2 - Delete subscriber\n'
                         '3 - View subscriber information\n'
                         '4 - See list of subscribers\n'
                         '5 - See the number of subscribes\n===='
                         '\nEnter command number - ')
    for item in user_command:
        if item.isalnum():
            item = str(item)
            if user_command == '1':
                user_add(input('pls enter name - '))
            elif user_command == '2':
                user_del(input('pls enter name - '))
            elif user_command == '3':
                user_information(input('pls enter name - '))
            elif user_command == '4':
                show_subscribers_list()
            elif user_command == '5':
                print(len(my_phone_book))
            else:
                print('Command not found try again')
                break
