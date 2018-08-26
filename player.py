from socket import *
import threading
import time

from communication import *
from gui import *


class Player:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.HOST = 'localhost'
        # self.PORT = 8000
        self.PORT = 8001
        self.conn = Communication(self)

    def setup_connection(self):
        print "Error: setup_connection MUST be overwritten"

    def setup_gui(self, gui):
        self.gui = gui

    def send_chat_message(self, message):
        self.conn.send_chat_message(message)

    def handle_chat_message(self, message):
        self.gui.text_box.configure(state='normal')
        self.gui.text_box.insert(END, 'Server >> %s\n' % message)
        self.gui.text_box.configure(state='disabled')
        self.gui.text_box.see(END)

    def start(self):
        self.setup_connection()
        t_receive = threading.Thread(
            target=self.conn.receive_message)
        t_receive.start()

    def __del__(self):
        self.socket.close()
