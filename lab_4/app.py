from lab_4.art import ART
from views.buttons import *
import numpy as np


class App(Tk):

    def __init__(self):
        super().__init__()

        self.main_pixels = []
        self.title = "Network"

        self.w = 8
        self.h = 8
        self.main_scale = 50
        self.scale = 10
        self.main_colors = [[0 for i in range(self.w)] for j in range(self.h)]

        self.create_button()

        main_colors_1d = np.array(self.main_colors).flatten()
        main_canvas_fr = Frame(self, highlightthickness=5)
        main_canvas_fr.grid(column=0, row=1)
        self.main_canvas = self.create_canvas(main_canvas_fr, main_colors_1d, self.main_pixels, self.main_scale)
        self.main_canvas.bind("<B1-Motion>", self.mouse_move_b1)
        self.main_canvas.bind("<B3-Motion>", self.mouse_move_b3)
        self.main_canvas.grid(column=0, row=0)

        self.images_pos_col = 0
        self.images_pos_row = 0

        self.images_fr = Frame(self, highlightthickness=5)
        self.images_fr.grid(column=0, row=2)

        self.canvas_images = []

        self.art = ART()

    def create_button(self):
        fr_button = Frame(self, highlightthickness=5)
        fr_button.grid(column=0, row=0)
        ButtonView(fr_button, "Расчитать", _callback=self.click_button).grid(column=0, row=0)

    def click_button(self):
        input_x = np.array(self.main_colors).flatten()
        create_image, new_image, neuron_index = self.art.work(input_x)

        pixels_im = []

        if create_image:
            new_canvas = self.create_canvas(self.images_fr, new_image, pixels_im, self.scale)
            new_canvas.grid(column=self.images_pos_col, row=self.images_pos_row)

            self.canvas_images.append(new_canvas)

            if self.images_pos_col == 5:
                self.images_pos_col = 0
                self.images_pos_row += 1
            else:
                self.images_pos_col += 1
        else:
            self.update_canvas(self.canvas_images[neuron_index], new_image, pixels_im, self.scale)

    def create_canvas(self, root, colors, pixels, scale):
        canvas = Canvas(root, width=self.w * scale, height=self.h * scale)
        self.create_pixels(canvas, colors, pixels, scale)
        return canvas

    def update_canvas(self, canvas, colors, pixels, scale):
        self.create_pixels(canvas, colors, pixels, scale)
        return canvas

    def create_pixels(self, canvas, colors, pixels, scale):
        index = 0
        for i in range(self.w):
            pixels.append([])
            for j in range(self.h):
                color = self.conver_color(colors[index])
                pixels[i].append(canvas.create_rectangle(
                    i * scale, j * scale,
                    i * scale + scale, j * scale + scale,
                    fill="#{0:06X}".format(color)
                ))
                index += 1

    def mouse_move_b1(self, event):
        self.paint(event)

    def mouse_move_b3(self, event):
        self.paint(event, "right")

    def paint(self, event, mouse_press="left"):
        mx = event.x // self.main_scale
        my = event.y // self.main_scale
        if mouse_press == "left":
            self.main_colors[mx][my] = 1
            color = self.conver_color(self.main_colors[mx][my])
            self.main_canvas.itemconfigure(self.main_pixels[mx][my], fill="#{0:06X}".format(color))
        if mouse_press == "right":
            self.main_colors[mx][my] = 0
            color = self.conver_color(self.main_colors[mx][my])
            self.main_canvas.itemconfigure(self.main_pixels[mx][my], fill="#{0:06X}".format(color))

    def conver_color(self, value):
        if value == 0:
            value = 1
        elif value == 1:
            value = 0
        color = int(value * 255)
        return (color << 16) | (color << 8) | color
