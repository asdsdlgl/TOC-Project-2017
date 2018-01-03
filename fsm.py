from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'calling to senior sister'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'calling to junior sister'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'hey younger'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'hello'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'why you just have read?'

    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'tt'

    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == 'i have some tickets,duo with me?'
    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == 'how about the next weekend?'
    def is_going_to_state9(self, update):
        text = update.message.text
        return text.lower() == 'how about the next week?'
    def is_going_to_state10(self, update):
        text = update.message.text
        return text.lower() == 'how could i have girlfriend?'
    def is_going_to_state11(self, update):
        text = update.message.text
        return text.lower() == 'external condition'
    def is_going_to_state12(self, update):
        text = update.message.text
        return text.lower() == 'internal condition'


    def on_enter_state1(self, update):
        update.message.reply_photo(open("img/1.png","rb"))
        update.message.reply_text("have read")
       # self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_photo(open("img/1.png","rb"))
        update.message.reply_text("what's wrong?")

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_photo(open("img/1.png","rb"))
        update.message.reply_text("???")


    def on_exit_state3(self, update):
        print('Leaving state3')
    
    def on_enter_state4(self, update):
        update.message.reply_text("have read")
       # self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_enter_state5(self, update):
        update.message.reply_text("have read")
       # self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')

    def on_enter_state6(self, update):
        update.message.reply_text("have read")
        self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6')

    def on_enter_state7(self, update):
        update.message.reply_text("Sorry,I have lots of things until weekend.")

    def on_exit_state7(self, update):
        print('Leaving state7')

    def on_enter_state8(self, update):
        update.message.reply_photo("https://i.imgur.com/VlMNcHM.gif")
        update.message.reply_text("LUL~Exactly Not!")
        self.go_back(update)

    def on_exit_state8(self, update):
        print('Leaving state8')

    def on_enter_state9(self, update):
        update.message.reply_text("have read")
        update.message.reply_photo("https://i.imgur.com/VlMNcHM.gif")
        self.go_back(update)

    def on_exit_state9(self, update):
        print('Leaving state9')

    def on_enter_state10(self, update):
        update.message.reply_text("External condition or Internal condition")

    def on_exit_state10(self, update):
        print('Leaving state10')

    def on_enter_state11(self, update):
        update.message.reply_text("$$$$$$$$$$$$$")
        update.message.reply_photo(open("img/2.jpg","rb"))
        self.go_back(update)

    def on_exit_state11(self, update):
        print('Leaving state11')

    def on_enter_state12(self, update):
        update.message.reply_text("face and U don't have it")
        update.message.reply_photo("https://media.istockphoto.com/photos/ugly-man-picture-id115907198?s=2048x2048.jpg")
        self.go_back(update)

    def on_exit_state12(self, update):
        print('Leaving state12')


