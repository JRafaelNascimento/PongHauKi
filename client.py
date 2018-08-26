from socket import *

from player import *
from gui import *


class Client(Player):
    def setup_connection(self):
        self.socket.connect((self.HOST, self.PORT))


player = Client()
player.start()

gui = GUI(player)
