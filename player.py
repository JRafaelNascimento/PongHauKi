import threading
import time

from communication import *
from gui import *
from game import *


class Player:
    def __init__(self, address, port):
        self.HOST = address
        self.PORT = port
        self.conn = Communication(self)
        self.game = Game()

    def setup_gui(self, gui):
        self.gui = gui
        self.reset_game()

    def send_chat_message(self, message):
        self.conn.send_chat_message(message)

    def send_game_message(self, message):
        if self.is_running:
            if self.its_roll_time:
                number = self.game.roll_dice()
                self.gui.update_board(self.game.main_board)
                self.gui.update_action_button("SEND")
                self.gui.update_action_text_field("Rolled for: " + str(number) +". Now write the word starting with " + self.game.get_player_position_letter())
                self.its_roll_time = False
                self.conn.send_move_message(number)
            else:
                if message != '' and self.game.validate_word(message):
                    if self.game.is_over():
                        self.gui.update_action_text_field("You WON!!! Press Start to Play Again!")
                        self.reset_game()
                    else:
                        self.gui.update_action_text_field("Oponent's turn!")
                        self.gui.block_action()
                        self.gui.update_left_oponents_board(self.game.left_oponent_board)
                        self.gui.update_right_oponents_board(self.game.right_oponent_board)
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
            msg += ". You lost! Press start to play!"
            self.reset_game()
        else:
            msg += ". Roll Dice to Play!"
            self.gui.update_action_button("ROLL")
            self.gui.update_left_player_board(self.game.left_player_board)
            self.gui.update_right_player_board(self.game.right_player_board)
            self.gui.release_action()
            self.its_roll_time = True

        self.gui.update_action_text_field(msg)

    def handle_move_command(self, quantity):
        self.gui.update_action_text_field("Oponent rolled dice for: " + str(quantity))
        self.game.move_oponent(quantity)
        self.gui.update_board(self.game.main_board)

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
        self.gui.release_action()
        self.gui.update_left_oponents_board(self.game.left_oponent_board)
        self.gui.update_right_oponents_board(self.game.right_oponent_board)
        self.gui.update_board(self.game.main_board)
        self.gui.update_left_player_board(self.game.left_player_board)
        self.gui.update_right_player_board(self.game.right_player_board)

        self.its_roll_time = False
        self.is_running = False

    def start(self):
        t_receive = threading.Thread(
            target=self.conn.start_connection)
        t_receive.start()

    def stop(self):
        self.gui.window.destroy()
        exit()
