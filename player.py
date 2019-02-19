from socket import *
import threading
import time

from communication import *
from gui import *
from game import *


class Player:
    def __init__(self, address, port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.HOST = address
        self.PORT = port
        self.conn = Communication(self)
        self.game = Game()

    def setup_connection(self):
        try:
            self.socket.connect((self.HOST, self.PORT))
        except:
            s = socket(AF_INET, SOCK_STREAM)
            s.bind((self.HOST, self.PORT))
            s.listen(1)
            self.socket, addr = s.accept()

    def setup_gui(self, gui):
        self.gui = gui
        self.reset_game()

    def send_chat_message(self, message):
        self.conn.send_chat_message(message)

    def send_game_message(self, message):
        if self.is_running:
            if self.its_roll_time:
                number = self.game.roll_dice()
                self.gui.update_main_board(self.game.main_board)
                self.gui.update_action_button("SEND")
                self.gui.update_action_text_field("Rolled for: " + number +". Now write the word starting with " + message[0].upper())
                self.its_roll_time = False
                self.conn.send_move_message(number)
            else:
                if self.game.validate_word(message):
                    if self.game.is_over():
                        self.gui.update_action_text_field("You WON!!! Press Start to Play Again!")
                        self.reset_game()
                    else:
                        self.gui.update_action_text_field("Oponent's turn!")
                        self.gui.block_action()
                        self.gui.update_oponents_board(self.game.oponent_board)
                    self.conn.send_word_message(message)
                else:
                    self.gui.show_error_message("Word not valid!")
        else:
            self.gui.update_action_text_field(
                "Its your turn! Roll the Dice!")
            self.gui.update_action_button("ROLL")
            self.its_roll_time = True
            self.is_running = True
            self.conn.send_start_message()


    def giveup_button_pressed(self):
        self.gui.update_action_text_field(
                "You lost! Press Start to Play Again!")
        self.conn.send_giveup_message()
        self.reset_game()

    def close_button_pressed(self):
        self.conn.send_exit_message()
        self.stop()

    def handle_chat_message(self, message):
        self.gui.update_text_box(message)

    def handle_word_message(self, word):
        msg = "Oponent's word is: " + word
        if self.game.handle_word(word):
            msg.append(". Roll Dice to Play!")
            self.gui.update_action_button("ROLL")
            self.gui.update_players_board(self.game.player_board)
            self.gui.release_action()
            self.its_roll_time = True
        else:
            msg.append(". You lost! Press start to play!")
            self.reset_game()

        self.gui.update_action_text_field(msg)

    def handle_move_command(self, quantity):
        self.gui.update_action_text_field("Oponent rolled dice for: " + quantity)
        self.game.move_oponent_player(quantity)
        self.gui.update_main_boards(self.game.main_board)

    def handle_giveup_command(self):
        self.gui.update_action_text_field("You WON!!! Press Start to Play Again!")
        self.reset_game()

    def handle_start_command(self):
        self.gui.update_action_text_field("Oponent's turn!")
        self.gui.update_action_button("ROLL")
        self.gui.block_action()
        self.is_running = True
        self.its_roll_time = True

    def reset_game(self):
        self.game.reset_game()
        self.gui.update_action_button("START")
        self.gui.update_main_board(self.game.main_board)
        self.gui.update_player_board(self.game.player_board)
        self.gui.update_oponent_board(self.game.oponent_board)
        self.its_roll_time = False
        self.is_running = False

    def start(self):
        self.setup_connection()
        t_receive = threading.Thread(
            target=self.conn.receive_message)
        t_receive.start()

    def stop(self):
        self.socket.close()
        self.gui.window.destroy()
        exit()
