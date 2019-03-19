from player import *
from gui import *
import sys

if len(sys.argv) == 3:
    player = Player(sys.argv[1], int(sys.argv[2]))
    player.start()

    gui = GUI(player)
else:
    print("ERROR: Need to call on format: launcher.py <address> <port>")
