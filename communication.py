class Communication:
    def __init__(self, player):
        self.player = player

    def command_separator(self):
        return ";"

    def exit_command(self):
        return "exit"

    def chat_command(self):
        return "chat"

    def send_chat_message(self, message):
        self.send_message(self.chat_command(), message)

    def send_exit_message(self):
        self.send_message(self.exit_command(), "")

    def send_message(self, command, message):
        s = self.command_separator()
        join_message = s.join([command, message])
        if self.player.socket.send(join_message) == 0:
            exit()

    def handle_message(self, msg):
        splitted = msg.split(self.command_separator())

        msg_type = splitted[0]
        msg_text = splitted[1]

        if msg_type == self.exit_command():
            return False
        elif msg_type == self.chat_command():
            self.player.handle_chat_message(msg_text)
        return True

    def receive_message(self):
        check = True
        while check:
            data = self.player.socket.recv(1024)
            if data == b'':
                exit()
            check = self.handle_message(data)
