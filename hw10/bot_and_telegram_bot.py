class Bot:

    def __init__(self, name):
        self.name = name
        self.message = None

    def say_name(self):
        print(f'====\n{self.name}')

    def send_message(self, message):
        self.message = message
        print(self.message)


some_bot = Bot('Mykola')
some_bot.say_name()
some_bot.send_message('Zdorovenki buly')


class TelegramBot(Bot):
    def __init__(self, name):
        super().__init__(name)
        self.url = None
        self.chat_id = None

    def set_url(self, url):
        self.url = url
        print(self.url)

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        name = self.name
        url = self.url
        chat_id = self.chat_id
        print(f'====\n{name} says - {message}, Kume, to chat {chat_id} using {url}')


telegram_bot = TelegramBot('Vasyl')
# telegram_bot.say_name()
telegram_bot.set_chat_id(1)
telegram_bot.send_message('vitayu')
