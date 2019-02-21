from board import Board
import random

def main_board_color():
    return 'black'

def oponent_board_color():
    return 'red'

def player_board_color():
    return 'blue'

def left_board_color():
    return 'grey'

def both_board_color():
    return 'green'

class Game:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.main_board = Board(2, main_board_color(), True)

        self.left_oponent_board = Board(5, left_board_color(), False)
        self.left_oponent_board.clear_board()

        self.right_oponent_board = Board(5, oponent_board_color(), False)

        self.left_player_board = Board(5, left_board_color(), False)
        self.left_player_board.clear_board()

        self.right_player_board = Board(5, player_board_color(), False)

        self.player_position = 0
        self.oponent_position = 0

        self.update_main_board()

    def roll_dice(self):
        rand = random.randint(1,6)
        self.move_player(rand)
        return rand

    def update_player_board(self, word):
        for i in range(0, len(word)):
            letter = word[i]
            letter_id = self.right_player_board.get_letter_id(letter)
            if letter_id != -1:
                self.right_player_board.erase_letter(letter_id)
                self.left_player_board.set_letter(letter_id, letter)

    def update_oponent_board(self, message):
        for i in range(0, len(message)):
            letter = message[i]
            letter_id = self.right_oponent_board.get_letter_id(letter)
            if letter_id != -1:
                self.right_oponent_board.erase_letter(letter_id)
                self.left_oponent_board.set_letter(letter_id, letter)

    def update_main_board(self):
        self.main_board.reset_colors()
        if self.oponent_position == self.player_position:
            self.main_board.set_letter_color(self.player_position, both_board_color())
        else:
            self.main_board.set_letter_color(self.player_position, player_board_color())
            self.main_board.set_letter_color(self.oponent_position, oponent_board_color())

    def validate_word(self, message):
        if self.main_board.get_letter_by_id(self.player_position).upper() == message[0].upper():
            self.update_oponent_board(message)
            return True
        return False

    def handle_word(self, word):
        self.update_player_board(word)
        return self.right_player_board.is_empty()

    def is_over(self):
        return self.right_oponent_board.is_empty()

    def move_player(self,quantity):
        self.player_position += quantity
        board_size = self.main_board.get_size()
        if self.player_position >= board_size:
            self.player_position -= board_size
        self.update_main_board()

    def move_oponent(self, quantity):
        self.oponent_position += quantity
        board_size = self.main_board.get_size()
        if self.oponent_position >= board_size:
            self.oponent_position -= board_size
        self.update_main_board()

    def get_player_position_letter(self):
        return self.main_board.get_letter_by_id(self.player_position).upper()
