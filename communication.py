import rpyc
import time
from rpyc.utils.server import ThreadedServer


class Server(rpyc.Service):

    def exposed_login(self, callback):
        print("Received login")
        self.conn.server = callback

    def exposed_message(self, text):
        self.conn.handle_message(text)

    def set_communication(self, conn):
        self.conn = conn


class Communication:

    def __init__(self, player):
        self.player = player
        self.server = None
        self.client = None
        self.should_run = True

    def start_connection(self):
        try:
            self.client = rpyc.connect(self.player.HOST, self.player.PORT)
            self.client.root.login(self.handle_message)
            self.main_loop()
        except:
            if not self.client:
                service = Server()
                service.set_communication(self)
                server = ThreadedServer(service, port=self.player.PORT)
                server.start()

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
        return "start"

    def giveup_command(self):
        return "giveup"

    def keepalive_command(self):
        return "keepalive"

    def send_chat_message(self, message):
        self.send_message(self.chat_command(), message)

    def send_exit_message(self):
        self.send_message(self.exit_command(), "")

    def send_word_message(self, word):
        self.send_message(self.word_command(), word)

    def send_move_message(self, quantity):
        self.send_message(self.move_command(), str(quantity))

    def send_giveup_message(self):
        self.send_message(self.giveup_command(), "")

    def send_start_message(self):
        self.send_message(self.start_command(), "")

    def send_keepalive_message(self):
        self.send_message(self.keepalive_command(), "")

    def send_message(self, command, message):
        s = self.command_separator()
        join_message = s.join([command, message])

        if command != self.keepalive_command():
            print("Sending Message")
            print(join_message)

        try:
            if self.client:
                self.client.root.message(join_message)
            elif self.server:
                self.server(join_message)
            else:
                print("Lack of communication")
                exit()
        except:
            exit()

    def handle_message(self, msg):
        splitted = msg.split(self.command_separator())

        msg_type = splitted[0]
        msg_body = splitted[1]

        if msg_type != self.keepalive_command():
            print("Receiving Message")
            print(splitted)

            if msg_type == self.exit_command():
                self.should_run = False
                self.player.stop()
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

    def main_loop(self):
        while(self.should_run):
            time.sleep(0.5)
            self.send_keepalive_message()
