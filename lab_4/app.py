import itertools
from tkinter import *

class App(Tk):

    def __init__(self):
        super().__init__()
        self.pixels = []
        self.title = "Network"

        self.w = 8
        self.h = 8
        self.scale = 50
        self.colors = [[1 for j in range(self.w)] for i in range(self.h)]

        self.create_canvas()

    def create_canvas(self):
        self.c = Canvas(self, width=self.w * self.scale, height=self.h * self.scale)
        self.create_pixels()
        self.c.bind("<B1-Motion>", self.mouse_move_b1)
        self.c.bind("<B3-Motion>", self.mouse_move_b3)
        self.c.grid(column=0, row=2)

    def create_pixels(self):
        for i in range(self.w):
            self.pixels.append([])
            for j in range(self.h):
                color = self.conver_color(self.colors[i][j])
                self.pixels[i].append(self.c.create_rectangle(
                    i * self.scale, j * self.scale,
                    i * self.scale + self.scale, j * self.scale + self.scale,
                    fill="#{0:06X}".format(color),
                    width=0
                ))

    def mouse_move_b1(self, event):
        self.paint(event)

    def mouse_move_b3(self, event):
        self.paint(event, "right")

    def paint(self, event, mouse_press="left"):
        mx = event.x // self.scale
        my = event.y // self.scale
        if mouse_press == "left":
            self.colors[mx][my] = 0
            color = self.conver_color(self.colors[mx][my])
            self.c.itemconfigure(self.pixels[mx][my], fill="#{0:06X}".format(color))
        if mouse_press == "right":
            self.colors[mx][my] = 1
            color = self.conver_color(self.colors[mx][my])
            self.c.itemconfigure(self.pixels[mx][my], fill="#{0:06X}".format(color))

    def conver_color(self, value):
        color = int(value * 255)
        return (color << 16) | (color << 8) | color
