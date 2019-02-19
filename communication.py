class Communication:
    def __init__(self, player):
        self.player = player

    def command_separator(self):
        return ";"

    def exit_command(self):
        return "exit"

    def chat_command(self):
        return "chat"

    def word_command(self):
        return "word"

    def move_command(self):
        return "move"

    def start_command(self):
        return "giveup"

    def giveup_command(self):
        return "giveup"

    def send_chat_message(self, message):
        self.send_message(self.chat_command(), message)

    def send_exit_message(self):
        self.send_message(self.exit_command(), "")

    def send_word_message(self, word):
        self.send_message(self.word_command(), word)

    def send_move_message(self, quantity):
        self.send_message(self.move_command(), quantity)

    def send_giveup_message(self, quantity):
        self.send_message(self.giveup_command(), "")

    def send_start_message(self, quantity):
        self.send_message(self.giveup_command(), "")

    def send_message(self, command, message):
        s = self.command_separator()
        join_message = s.join([command, message])
        print("Sending Message")
        print(join_message)
        if self.player.socket.send(join_message) == 0:
            exit()

    def handle_message(self, msg):
        splitted = msg.split(self.command_separator())

        msg_type = splitted[0]
        msg_body = splitted[1]

        print("Receiving Message")
        print(splitted)

        if msg_type == self.exit_command():
            return False
        elif msg_type == self.chat_command():
            self.player.handle_chat_message(msg_body)
        elif msg_type == self.word_command():
            self.player.handle_word_message(msg_body)
        elif msg_type == self.move_command():
            self.player.handle_move_command(int(msg_body))
        elif msg_type == self.giveup_command():
            self.player.handle_giveup_command()
        elif msg_type == self.start_command():
            self.player.handle_start_command()
        return True

    def receive_message(self):
        check = True
        while check:
            data = self.player.socket.recv(1024)
            if data == b'':
                exit()
            check = self.handle_message(data)
        self.player.stop()
        exit()
