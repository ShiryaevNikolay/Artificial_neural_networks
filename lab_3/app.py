from pynput import mouse
from tkinter import *


class App(Tk):

    def __init__(self):
        super().__init__()
        self.mouse_press_left = False
        self.mouse_press_right = False

        self.title("Network")

        self.w = 28
        self.h = 28
        self.scale = 20
        self.colors = [[0 for j in range(self.w)] for i in range(self.h)]

        self.c = Canvas(self, width=self.w * self.scale, height=self.h * self.scale)
        self.createPixels()
        self.c.bind("<B1-Motion>", self.mouseMoveB1)
        self.c.bind("<B3-Motion>", self.mouseMoveB3)
        self.c.grid(column=0, row=0)

        Label(self, text="Номер персептрона").grid(column=1, row=0)

    def createPixels(self):
        for i in range(self.w):
            for j in range(self.h):
                tag = "{}x{}".format(i, j)
                print(tag)
                self.c.create_rectangle(
                    i * self.scale, j * self.scale,
                    i * self.scale + self.scale, j * self.scale + self.scale,
                    fill="white",
                    tags=("pixel", tag)
                )

    def mouseMoveB1(self, event):
        self.paint(int(event.x / self.scale), int(event.y / self.scale))

    def mouseMoveB3(self, event):
        self.paint(int(event.x / self.scale), int(event.y / self.scale))

    def mouseListener(self):
        with mouse.Listener(
            on_click=self.onClick
        ) as listener:
            listener.join()

    def paint(self, x, y):
        # print(self.c.find_overlapping(event.x - 0.5, event.y - 0.5, event.x + 0.5, event.y + 0.5)[-1])

        main_rec_tag = "{}x{}".format(x, y)
        print(main_rec_tag)
        self.c.itemconfigure(main_rec_tag, fill="blue")

    # def paint(self, event):
    #     inputs = [0 for i in range(784)]
    #     # print(event.x, event.y)
    #     for i in range(self.w):
    #         for j in range(self.h):
    #             if self.mouse_press_left:
    #                 dist = (i - self.mx)**2 + (j - self.my)**2
    #                 if dist < 1:
    #                     dist = 1
    #                 self.colors[i][j] += 0.1 / dist
    #                 if self.colors[i][j] > 1:
    #                     self.colors[i][j] = 1
    #             color = int(self.colors[i][j] * 255)
    #             color = (color << 16) or (color << 8) or color
    #
