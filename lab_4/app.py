from tkinter import *
from comparison import *
from recognition import *
from views.buttons import *


class App(Tk):

    def __init__(self):
        super().__init__()

        self.main_pixels = []
        self.title = "Network"

        self.w = 8
        self.h = 8
        self.main_scale = 50
        self.scale = 20
        self.main_colors = [[0 for i in range(self.w)] for j in range(self.h)]

        self.create_button()

        self.main_canvas = self.create_canvas(self, self.main_colors, self.main_pixels, self.main_scale)
        self.main_canvas.bind("<B1-Motion>", self.mouse_move_b1)
        self.main_canvas.bind("<B3-Motion>", self.mouse_move_b3)
        self.main_canvas.grid(column=0, row=2)

        # Слой распознавания
        self.layer_recognition = [Recognition()]
        # Слой сравнения
        self.layer_comparison = [Comparison() for i in range(self.w * self.h)]

    def create_button(self):
        fr_button = Frame(self, highlightthickness=5)
        fr_button.grid(column=0, row=0)
        ButtonView(fr_button, "Расчитать", _callback=self.click_button).grid(column=0, row=0)

    def click_button(self):
        print(self.main_colors)

    def create_canvas(self, root, colors, pixels, scale):
        canvas = Canvas(root, width=self.w * scale, height=self.h * scale)
        self.create_pixels(canvas, colors, pixels, scale)
        return canvas

    def create_pixels(self, canvas, colors, pixels, scale):
        for i in range(self.w):
            pixels.append([])
            for j in range(self.h):
                color = self.conver_color(colors[i][j])
                pixels[i].append(canvas.create_rectangle(
                    i * self.main_scale, j * scale,
                    i * self.main_scale + scale, j * scale + scale,
                    fill="#{0:06X}".format(color)
                ))

    def mouse_move_b1(self, event):
        self.paint(event)

    def mouse_move_b3(self, event):
        self.paint(event, "right")

    def paint(self, event, mouse_press="left"):
        mx = event.x // self.main_scale
        my = event.y // self.main_scale
        if mouse_press == "left":
            self.main_colors[my][mx] = 1
            color = self.conver_color(self.main_colors[my][mx])
            self.main_canvas.itemconfigure(self.main_pixels[mx][my], fill="#{0:06X}".format(color))
        if mouse_press == "right":
            self.main_colors[my][mx] = 0
            color = self.conver_color(self.main_colors[my][mx])
            self.main_canvas.itemconfigure(self.main_pixels[mx][my], fill="#{0:06X}".format(color))

    def conver_color(self, value):
        if value == 0:
            value = 1
        elif value == 1:
            value = 0
        color = int(value * 255)
        return (color << 16) | (color << 8) | color
