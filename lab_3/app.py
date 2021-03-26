from pynput import mouse
from tkinter import *
import threading


class App(Tk):

    def __init__(self):
        super().__init__()
        self.mouse_press_left = False
        self.mouse_press_right = False
        self.mx = 0
        self.my = 0

        self.title("Network")

        self.w = 28
        self.h = 28
        self.scale = 20
        self.colors = [[0 for j in range(self.w)] for i in range(self.h)]

        self.c = Canvas(self, width=self.w * self.scale, height=self.h * self.scale, bg='white')
        self.c.bind("<Motion>", self.moveMouse)
        self.c.grid(column=0, row=0)

        self.lbl = Label(self, text="Номер персептрона")
        self.lbl.grid(column=1, row=0)

        thread_ = threading.Thread(target=self.mouseListener)
        thread_.start()

    def moveMouse(self, event):
        self.mx = event.x / self.scale
        self.my = event.y / self.scale
        if self.mouse_press_left:
            # self.paint(event)
        elif self.mouse_press_right:
            position = "(x={}, y={})".format(event.x, event.y)
            print(event.type, "event", position)

    def mouseListener(self):
        with mouse.Listener(on_click=self.onClick) as listener:
            listener.join()

    def onClick(self, x, y, button, pressed):
        if button.name == 'left':
            self.mouse_press_left = pressed
            print("left")
        elif button.name == 'right':
            self.mouse_press_right = pressed
            print("right")

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
