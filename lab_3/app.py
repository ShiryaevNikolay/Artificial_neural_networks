from tkinter import *
import math


class App(Tk):

    def __init__(self):
        super().__init__()
        self.pixels = []
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
            self.pixels.append([])
            for j in range(self.h):
                self.pixels[i].append(self.c.create_rectangle(
                    i * self.scale, j * self.scale,
                    i * self.scale + self.scale, j * self.scale + self.scale,
                    fill="white"
                ))

    def mouseMoveB1(self, event):
        # self.paint(math.floor(event.x / self.scale), math.floor(event.y / self.scale))
        self.paint(event)

    def mouseMoveB3(self, event):
        # self.paint(math.floor(event.x / self.scale), math.floor(event.y / self.scale), "white")
        self.paint(event, "right")

    def paint(self, event, mouse_press="left"):
        # self.c.itemconfigure(self.pixels[x][y], fill=color)
        # inputs = [0 for i in range(self.w * self.h)]
        mx = event.x / self.scale
        my = event.y / self.scale
        for i in range(self.w):
            for j in range(self.h):
                dist = (i - mx)**2 + (j - my)**2  # Высчитываем радиус от тоординаты мыши, то каждого пикселя в итерации
                if dist < 1:  # Задаем минимайный размер радиуса =1
                    dist = 1
                dist *= dist
                if mouse_press == "left":
                    self.colors[i][j] -= 0.1 / dist
                elif mouse_press == "right":
                    self.colors[i][j] += 0.1 / dist
                if self.colors[i][j] > 1:
                    self.colors[i][j] = 1
                if self.colors[i][j] < 0:
                    self.colors[i][j] = 0
                print(self.colors[i][j])
                color = int(self.colors[i][j] * 255)
                color = (color << 16) | (color << 8) | color
                self.c.itemconfigure(self.pixels[i][j], fill="#{0:06X}".format(color))


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
