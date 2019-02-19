from Tkinter import *
from ScrolledText import*
import tkMessageBox


class GUI():
    def __init__(self, player):
        self.window = Tk()
        self.window.title("Jogo das Letras")
        self.player = player

        self.main_frame = Frame(self.window)
        self.main_frame.pack()

        self.top_frame = Frame(self.main_frame)
        self.top_frame.pack()

        self.oponents_frame = Frame(self.main_frame)
        self.oponents_frame.pack()

        self.oponents_left_board_frame = Frame(self.oponents_frame)
        self.oponents_left_board_frame.pack(side=LEFT)

        self.oponents_board_text_field = Label(self.oponents_frame, text="Oponent's Board!", width=20)
        self.oponents_board_text_field.pack(side=LEFT)

        self.oponents_right_board_frame = Frame(self.oponents_frame)
        self.oponents_right_board_frame.pack(side=LEFT)

        self.board_frame = Frame(self.main_frame, height=300)
        self.board_frame.pack()

        self.player_frame = Frame(self.main_frame)
        self.player_frame.pack()

        self.player_left_board_frame = Frame(self.player_frame)
        self.player_left_board_frame.pack(side=LEFT)

        self.players_board_text_field = Label(self.player_frame, text="Player's Board!", width=20)
        self.players_board_text_field.pack(side=LEFT)

        self.player_right_board_frame = Frame(self.player_frame)
        self.player_right_board_frame.pack(side=LEFT)

        self.bottom_frame = Frame(self.main_frame)
        self.bottom_frame.pack()

        self.chat_frame = Frame(self.main_frame)
        self.chat_frame.pack(side=BOTTOM)

        self.setup_action_text_field()

        self.setup_left_oponents_board()
        self.setup_right_oponents_board()

        self.setup_board()

        self.setup_left_player_board()
        self.setup_right_player_board()

        self.setup_giveup_button()
        self.setup_action_button()
        self.setup_game_text_field()

        self.setup_text_box()
        self.setup_text_field()
        self.setup_send_button()

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.player.setup_gui(self)
        self.window.mainloop()

    def setup_left_oponents_board(self):
        board = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','x','y','w','z']]
        for i,row in enumerate(board):
            for j,column in enumerate(row):
                L = Label(self.oponents_left_board_frame, text=" " + column + " ", font=('Default', 15), fg='grey', width=3)
                L.grid(row=i,column=j)

    def setup_right_oponents_board(self):
        board = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','x','y','w','z']]
        for i,row in enumerate(board):
            for j,column in enumerate(row):
                L = Label(self.oponents_right_board_frame, text=" " + column + " ", font=('Default', 15), fg='red', width=3)
                L.grid(row=i,column=j)

    def setup_board(self):
        board = [['a','b','c','d','e','f','g','h','i','j','k','l','m'],['n','o','p','q','r','s','t','u','v','x','y','w','z']]
        for i,row in enumerate(board):
            for j,column in enumerate(row):
                L = Label(self.board_frame, text=" " + column + " ", font=('Default', 15), fg='green', width=3)
                L.grid(row=i,column=j)

    def setup_left_player_board(self):
        board = [['a','b','c','d','e'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','x','y','w','z']]
        for i,row in enumerate(board):
            for j,column in enumerate(row):
                L = Label(self.player_left_board_frame, text=" " + column + " ", font=('Default', 15), fg='grey', width=3)
                L.grid(row=i,column=j)

    def setup_right_player_board(self):
        board = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','x','y','w','z']]
        for i,row in enumerate(board):
            for j,column in enumerate(row):
                L = Label(self.player_right_board_frame, text=" " + column + " ", font=('Default', 15), fg='blue', width=3)
                L.grid(row=i,column=j)

    def setup_action_text_field(self):
        self.action_text_field = Label(self.top_frame, text="Press Start!", font=('Default', 20))
        self.action_text_field.pack()

    def setup_action_button(self):
        self.action_button = Button(self.bottom_frame, text="START",
                                    command=lambda: self.send_game_message([]))
        self.action_button.pack(side=RIGHT)

    def setup_game_text_field(self):
        self.game_text_field = Entry(self.bottom_frame, width=72)
        self.game_text_field.focus_set()
        self.game_text_field.bind(sequence="<Return>",
                             func=self.send_game_message)
        self.game_text_field.pack(side=LEFT)

    def setup_giveup_button(self):
        self.giveup_button = Button(self.bottom_frame, text="Give Up",
                                    command=self.send_giveup_message)
        self.giveup_button.pack(side=RIGHT)

    def setup_send_button(self):
        self.send_button = Button(self.chat_frame, text="Send",
                                  command=lambda: self.send_chat_message([]))
        self.send_button.pack(side=RIGHT)

    def setup_text_field(self):
        self.text_field = Entry(self.chat_frame, width=82)
        self.text_field.focus_set()
        self.text_field.bind(sequence="<Return>",
                             func=self.send_chat_message)
        self.text_field.pack(side=LEFT)

    def setup_text_box(self):
        self.text_box = ScrolledText(self.main_frame, height=10, width=101)
        self.text_box.configure(state='disabled')
        self.text_box.pack(side=TOP)

    def block_action(self):
        self.action_button['state'] = 'disable'

    def release_action(self):
        self.action_button['state'] = 'normal'

    def update_text_box(self, message):
        self.text_box.configure(state='normal')
        self.text_box.insert(END, 'Oponent >> %s\n' % message)
        self.text_box.configure(state='disabled')
        self.text_box.see(END)

    def update_action_button(self, message):
        self.action_button["text"] = message

    def update_action_text_field(self, message):
        self.action_text_field["text"] = message

    def show_error_message(self, message):
        tkMessageBox.showerror("Error", message)

    def send_chat_message(self, args):
        self.text_box.configure(state='normal')
        text = self.text_field.get()
        if text != "":
            self.text_box.insert(END, 'Me >> %s\n' % text)
            self.text_field.delete(0, END)
            self.player.send_chat_message(text)
            self.text_field.focus_set()
            self.text_box.configure(state='disabled')
            self.text_box.see(END)

    def send_game_message(self, args):
        text = self.game_text_field.get()
        self.game_text_field.delete(0, END)
        self.game_text_field.focus_set()
        self.player.send_game_message(text)

    def send_giveup_message(self):
        self.player.giveup_button_pressed()

    def on_closing(self):
        self.player.close_button_pressed()
