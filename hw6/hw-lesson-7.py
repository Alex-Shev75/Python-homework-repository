"""
dict
"""

my_phone_book = {'Mom': '+1111111',
                 'Dad': '+2222222',
                 'Bro': '+3333333'
                 }
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
            if item == '5':
                print(f'\n====\nThere are {len(my_phone_book)} subscribers in your phone book\n====\n')
            elif item == '4':
                print('\nSubscriber list:\n====\n')
                for subscriber in my_phone_book:
                    print(subscriber)
            elif item == '3':
                while True:
                    sub_command_view = input('\n====\nChoose subscriber: - ')
                    command_view = sub_command_view
                    if command_view in my_phone_book:
                        command_view = my_phone_book[command_view]
                        print(f'\n====\n{sub_command_view}`s phone number: - {command_view}\n====\n')
                        break
                    else:
                        print('\n====\nSubscriber not found, select from the list:\n====\n')
                        for subscriber in my_phone_book:
                            print(subscriber)
            elif item == '2':
                while True:
                    sub_command_delete = input('\n====\nSelect the subscribers to be deleted: - ')
                    command_delete = sub_command_delete
                    if command_delete in my_phone_book:
                        accept = input('You are sure?  [Y] - Yes, [any symbol] - exit to main menu - ')
                        y = accept
                        if y == str('Y'):
                            del my_phone_book[command_delete]
                            print(f'\n===\n`{command_delete}` has been removed from your phone book\n===\n')
                        break
                    else:
                        print('\n====\nSubscriber not found, select from the list:\n====\n')
                        for subscriber in my_phone_book:
                            print(subscriber)
            elif item == '1':
                while True:
                    user_add = input('====\nEnter name - ')
                    if len(user_add) > 0:
                        if user_add not in my_phone_book.keys():
                            number_input = input('====\nEnter phone number - ')
                            if len(number_input) >= 3:
                                my_phone_book[user_add] = number_input
                                print(f'====\n{user_add} added in your phone book\n====')
                                break
                            else:
                                print('===\nNumber must contain min 3 symbols\n====')
                        else:
                            print(f'====\n{user_add} is already in your phone book\n====')
                            for subscriber in my_phone_book:
                                print(subscriber)
                    else:
                        print('===\nName must contain min 1 symbol\n====')
                    print('Repeat input')

            else:
                print('\n====\nCommand not found, please try again\n====')