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

    def send_action_message(self):
        self.conn.send_action_message()

    def action_button_pressed(self):
        if self.is_running:
            self.gui.update_action_text_field(
                "You lost! Press Start to Play Again!")
            self.reset_game()
        else:
            self.gui.update_action_text_field(
                "Its your turn!")
            self.gui.update_action_button("Give Up")
            self.is_my_turn = True
            self.is_running = True

        self.send_action_message()

    def game_button_pressed(self, button_number):
        if self.is_my_turn:
            if self.first_button == None:
                self.first_button = button_number
            elif self.second_button == None:
                self.second_button = button_number
                if self.game.move_button(self.first_button, self.second_button):
                    self.conn.send_move_message(
                        self.first_button, self.second_button, self.game.my_color)
                    if self.game.is_game_over():
                        self.gui.update_action_text_field(
                            "You WON!!! Press Start to Play Again!")
                        self.reset_game()
                    else:
                        self.gui.update_action_text_field("Oponents turn!")
                        self.is_my_turn = False
                        self.gui.update_game_buttons_color(self.game.positions)
                else:
                    self.gui.show_error_message("Invalid Moviment!")

                self.first_button = None
                self.second_button = None

    def close_button_pressed(self):
        self.conn.send_exit_message()
        self.stop()

    def handle_chat_message(self, message):
        self.gui.update_text_box(message)

    def handle_action_message(self):
        if self.is_running:
            self.gui.update_action_text_field(
                "You WON!!! Press Start to Play Again!")
            self.reset_game()
        else:
            self.gui.update_action_text_field("Oponents turn!")
            self.gui.update_action_button("Give Up")
            self.is_running = True
            self.is_my_turn = False

    def handle_move_command(self, position_one, position_two, color):
        self.game.switch_positions(position_one, position_two, color)
        if self.game.is_game_over():
            self.gui.update_action_text_field(
                "You lost! Press Start to Play Again!")
            self.reset_game()
        else:
            self.gui.update_action_text_field("Its your turn!")
            self.gui.update_game_buttons_color(self.game.positions)
            self.is_my_turn = True

    def reset_game(self):
        self.game.reset_game()
        # self.gui.update_action_button("Start")
        # self.gui.update_game_buttons_color(self.game.positions)
        self.first_button = None
        self.second_button = None
        self.is_my_turn = False
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
