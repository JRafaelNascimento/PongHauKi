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
