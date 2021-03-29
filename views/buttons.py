from tkinter import *


def button(root, text, _callback=None):
    return Button(
        root,
        text=text,
        borderwidth=0,
        bg="#3f51b5",
        fg="#ffffff",
        highlightcolor="#29b6f6",
        activeforeground="#FFFFFF",
        activebackground="#5c6bcd",
        highlightthickness=5,
        # highlightbackground="#37d3ff"
        command=callback_btn(_callback)
    )


def callback_btn(_callback=None):
    if _callback:
        _callback()
