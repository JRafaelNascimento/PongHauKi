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
        base_board = Board(1, '', True)
        self.base_letters = base_board.letters

        self.main_board = Board(2, main_board_color(), True)

        self.left_oponent_board = Board(5, left_board_color(), False)
        self.left_oponent_board.clear_board()

        self.right_oponent_board = Board(5, oponent_board_color(), False)

        self.left_player_board = Board(5, left_board_color(), False)
        self.left_player_board.clear_board()

        self.right_player_board = Board(5, player_board_color(), False)

        self.player_position = 0
        self.oponent_position = 0

    def roll_dice(self):
        rand = random.randint(1,6)
        self.move_player(rand)
        self.update_main_board()
        return rand

    def update_player_board(self, word):
        pass

    def update_oponent_board(self, message):
        pass

    def update_main_board():
        pass

    def validate_word(self, message):
        if self.base_letters[self.player_position] == message[0].upper():
            self.update_oponent_board(message)
            return True
        return False

    def handle_word(self, word):
        self.update_player_board(word)
        return self.is_over()

    def is_over(self):
        return True

    def move_player(self,quantity):
        pass

    def move_oponent(self, quantity):
        pass
