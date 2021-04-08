from tkinter import *


class ButtonView(Button):

    def __init__(self, root, text, _callback=None):
        super().__init__(
            root,
            text=text,
            borderwidth=0,
            bg="#3f51b5",
            fg="#ffffff",
            activeforeground="#FFFFFF",
            activebackground="#5c6bcd",
            highlightthickness=5,
            command=_callback
        )
