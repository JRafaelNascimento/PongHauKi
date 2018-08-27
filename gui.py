from Tkinter import *
from ScrolledText import*
import tkMessageBox


class GUI():
    def __init__(self, player):
        self.window = Tk()
        self.window.title("Pong-Hau-Ki")
        self.player = player

        self.main_frame = Frame(self.window)
        self.main_frame.pack()

        self.game_frame = Frame(self.main_frame, width=400, height=400)
        self.game_frame.pack()

        self.action_frame = Frame(self.main_frame)
        self.action_frame.pack()

        self.chat_frame = Frame(self.main_frame)
        self.chat_frame.pack(side=BOTTOM)

        self.setup_game_lines()
        self.setup_game_buttons()

        self.setup_action_text_field()
        self.setup_action_button()

        self.setup_text_box()
        self.setup_text_field()
        self.setup_send_button()

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.player.setup_gui(self)
        self.window.mainloop()

    def setup_game_buttons(self):
        self.left_up_button = Button(self.game_frame, text="",
                                     command=lambda: self.send_button_click(0))
        self.left_up_button.place(x = 25, y = 25, height=50, width=50)

        self.right_up_button = Button(self.game_frame, text="",
                                      command=lambda: self.send_button_click(1))
        self.right_up_button.place(x = 300, y = 25, height=50, width=50)

        self.center_button = Button(self.game_frame, text="",
                                    command=lambda: self.send_button_click(2))
        self.center_button.place(x = 162, y = 113, height=50, width=50)

        self.left_bottom_button = Button(self.game_frame, text="",
                                         command=lambda: self.send_button_click(3))
        self.left_bottom_button.place(x = 25, y = 200, height=50, width=50)

        self.right_bottom_button = Button(self.game_frame, text="",
                                          command=lambda: self.send_button_click(4))
        self.right_bottom_button.place(x = 300, y = 200, height=50, width=50)

    def setup_game_lines(self):
        self.canvas = Canvas(self.game_frame)
        self.canvas.create_line(75, 75, 300, 200)
        self.canvas.create_line(300, 75, 75, 200)
        self.canvas.create_line(50, 50, 50, 225)
        self.canvas.create_line(325, 50, 325, 225)
        self.canvas.create_line(50, 225, 325, 225)

        self.canvas.pack()

    def setup_action_text_field(self):
        self.action_text_field = Label(self.action_frame, text="Press Start!")
        self.action_text_field.pack(side=TOP)

    def setup_action_button(self):
        self.action_button = Button(self.action_frame, text="Start",
                                    command=self.send_action_message)
        self.action_button.pack(side=BOTTOM)

    def setup_send_button(self):
        self.send_button = Button(self.chat_frame, text="Send",
                                  command=lambda: self.send_chat_message([]))
        self.send_button.pack(side=RIGHT)

    def setup_text_field(self):
        self.text_field = Entry(self.chat_frame, width=80)
        self.text_field.focus_set()
        self.text_field.bind(sequence="<Return>",
                             func=self.send_chat_message)
        self.text_field.pack(side=LEFT)

    def setup_text_box(self):
        self.text_box = ScrolledText(self.main_frame, height=10, width=100)
        self.text_box.configure(state='disabled')
        self.text_box.pack(side=TOP)

    def disable_game_buttons(self):
        self.left_up_button['state'] = 'disable'
        self.right_up_button['state'] = 'disable'
        self.center_button['state'] = 'disable'
        self.left_bottom_button['state'] = 'disable'
        self.right_bottom_button['state'] = 'disable'

    def enable_game_buttons(self):
        self.left_up_button['state'] = 'normal'
        self.right_up_button['state'] = 'normal'
        self.center_button['state'] = 'normal'
        self.left_bottom_button['state'] = 'normal'
        self.right_bottom_button['state'] = 'normal'

    def update_text_box(self, message):
        self.text_box.configure(state='normal')
        self.text_box.insert(END, 'Oponent >> %s\n' % message)
        self.text_box.configure(state='disabled')
        self.text_box.see(END)

    def update_game_buttons_color(self, colors):
        self.left_up_button['bg'] = colors[0]
        self.right_up_button['bg'] = colors[1]
        self.center_button['bg'] = colors[2]
        self.left_bottom_button['bg'] = colors[3]
        self.right_bottom_button['bg'] = colors[4]

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

    def send_action_message(self):
        self.player.action_button_pressed()

    def send_button_click(self, button_number):
        self.player.game_button_pressed(button_number)

    def on_closing(self):
        self.player.close_button_pressed()
