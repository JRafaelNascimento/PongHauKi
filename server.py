from socket import *

from player import *
from gui import *


class Server(Player):
    def setup_connection(self):
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((self.HOST, self.PORT))
        s.listen(1)
        self.socket, addr = s.accept()


player = Server()
player.start()

gui = GUI(player)
