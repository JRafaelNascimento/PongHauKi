
def red_color():
    return 'red'


def blue_color():
    return 'blue'


def white_color():
    return 'white'


def is_white(button):
    if button == white_color():
        return True
    return False


def is_red(button):
    if button == red_color():
        return True
    return False


def is_blue(button):
    if button == blue_color():
        return True
    return False


class Game:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.my_color = None
        self.positions = [red_color(), red_color(), white_color(),
                          blue_color(), blue_color()]

    def move_button(self, position_one, position_two):
        if position_one == 0 and position_two == 1:
            print "Invalid Line"
            return False

        if position_one == 1 and position_two == 0:
            print "Invalid Line"
            return False

        if is_white(self.positions[position_one]):
            print "First White"
            return False

        if not is_white(self.positions[position_two]):
            print "Second Not White"
            return False

        if not self.is_move_valid(position_one):
            return False

        if self.my_color == None:
            self.my_color = self.positions[position_one]
            print "My Color"
            print self.my_color

        if is_blue(self.my_color):
            if is_blue(self.positions[position_one]):
                self.switch_positions(position_one, position_two)
                return True

        if is_red(self.my_color):
            if is_red(self.positions[position_one]):
                self.switch_positions(position_one, position_two)
                return True

        return False

    def is_move_valid(self, switch_position):
        white_position = self.find_white()
        if white_position == 0:
            if switch_position == 2 or switch_position == 3:
                return True
            else:
                return False
        elif white_position == 1:
            if switch_position == 2 or switch_position == 4:
                return True
            else:
                return False
        elif white_position == 2:
                return True
        elif white_position == 3:
            if switch_position != 1:
                return True
            else:
                return False
        elif white_position == 4:
            if switch_position != 0:
                return True
            else:
                return False
        else:
            return False


    def find_white(self):
        for position, color in enumerate(self.positions):
            if is_white(color):
                return position
        return -1

    def switch_positions(self, position_one, position_two, color=None):
        if color != None and self.my_color == None:
            if is_blue(color):
                self.my_color = red_color()
            elif is_red(color):
                self.my_color = blue_color()
        old_position = self.positions[position_one]
        self.positions[position_one] = self.positions[position_two]
        self.positions[position_two] = old_position

    def is_game_over(self):
        if is_white(self.positions[0]):
            if is_red(self.positions[2]) and is_red(self.positions[3]):
                return True

            if is_blue(self.positions[2]) and is_blue(self.positions[3]):
                return True

        if is_white(self.positions[1]):
            if is_red(self.positions[2]) and is_red(self.positions[4]):
                return True

            if is_blue(self.positions[2]) and is_blue(self.positions[4]):
                return True

        return False
