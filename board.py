from letter import Letter

RAW_LETTERS = ['a','b','c','d','e', '','f','g','h','i','j', '','k','l','m','n','o', '','p','q','r','s','t', '','u','v','x','y','w','z']

class Board:
    letters = []
    def __init__(self, rows, color, ignore_clear):
        self.rows = rows
        self.color = color
        self.ignore_clear = ignore_clear
        self.reset_board()

    def build_letter(self, id, letter):
        return Letter(id, letter.upper(), self.color)

    def get_letter_id(self, letter):
        for i,row in enumerate(self.letters):
            for j,column in enumerate(row):
                if column.letter.upper() == letter.upper():
                    return column.id

        return -1

    def get_letter_by_id(self, id):
        for i,row in enumerate(self.letters):
            for j,column in enumerate(row):
                if column.id == id:
                    return column.letter

        return ''

    def get_size(self):
        return self.rows * len(self.letters[0])

    def reset_colors(self):
        for i,row in enumerate(self.letters):
            for j,column in enumerate(row):
                column.color = self.color

    def is_empty(self):
        for i,row in enumerate(self.letters):
            for j,column in enumerate(row):
                if column.letter != '':
                    return False
        return True

    def erase_letter(self, id):
        for i,row in enumerate(self.letters):
            for j,column in enumerate(row):
                if column.id == id:
                    column.letter = ''

    def set_letter_color(self, id, color):
        for i,row in enumerate(self.letters):
            for j,column in enumerate(row):
                if column.id == id:
                    column.color = color

    def set_letter(self, id, letter):
        for i,row in enumerate(self.letters):
            for j,column in enumerate(row):
                if column.id == id:
                    column.letter = letter[0].upper()

    def clear_board(self):
        self.letters = []
        for i in range(self.rows):
            self.letters.append([])
            for j, letter in enumerate(RAW_LETTERS):
                if j < len(RAW_LETTERS)/self.rows:
                    index = j+(i*len(RAW_LETTERS)/self.rows)
                    raw_letter = ''
                    obj_letter = self.build_letter(index, raw_letter)
                    self.letters[i].append(obj_letter)
                else:
                    break

    def reset_board(self):
        self.letters = []
        for i in range(self.rows):
            self.letters.append([])
            for j, letter in enumerate(RAW_LETTERS):
                if j < len(RAW_LETTERS)/self.rows:
                    index = j+(i*len(RAW_LETTERS)/self.rows)
                    raw_letter = RAW_LETTERS[index]
                    if raw_letter != '' or (raw_letter == ''  and not self.ignore_clear):
                        obj_letter = self.build_letter(index, raw_letter)
                        self.letters[i].append(obj_letter)
                    else:
                        pass
                else:
                    break
