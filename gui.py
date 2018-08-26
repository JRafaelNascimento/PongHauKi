from Tkinter import *
from ScrolledText import*


class GUI():
    window = Tk()

    def __init__(self, player):
        self.window.title("Chat")
        self.player = player
        self.player.setup_gui(self)

        frame = Frame(self.window)
        frame.pack()

        self.text_box = ScrolledText(frame, height=10, width=100)
        self.text_box.pack()
        self.text_box.insert(END, 'Welcome to Chat\n')
        self.text_box.configure(state='disabled')

        sframe = Frame(frame)
        sframe.pack(anchor='w')

        self.text_field = Entry(sframe, width=80)
        self.text_field.focus_set()
        self.text_field.bind(sequence="<Return>",
                             func=self.send_chat_message)
        self.text_field.pack(side=LEFT)

        self.button = Button(sframe, text="Send", command=self.send_button)
        self.button.pack(side=RIGHT)

        self.window.mainloop()

    def send_button(self):
        self.send_chat_message([])

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
