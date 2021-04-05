import itertools
from views.buttons import *
from tkinter import *
from perceptron import *


class App(Tk):

    weight_file_path = "../mnist_weight.xlsx"

    def __init__(self):
        super().__init__()
        self.pixels = []
        self.title("Network")

        self.w = 28
        self.h = 28
        self.scale = 20
        self.colors = [[0 for j in range(self.w)] for i in range(self.h)]

        self.create_canvas()
        self.create_info()

        self.bind("c", self.press_c)

        self.layer_perceptron = []
        # sheets_weight = get_sheets_weight(weight_file_path=self.weight_file_path)
        for i in range(10):
            self.layer_perceptron.append(Perceptron(length=28 ** 2, id_perceptron=i))

        self.label_perceptron = []
        self.create_info_perceptron()

    def create_canvas(self):
        self.c = Canvas(self, width=self.w * self.scale, height=self.h * self.scale)
        self.createPixels()
        self.c.bind("<B1-Motion>", self.mouseMoveB1)
        self.c.bind("<B3-Motion>", self.mouseMoveB3)
        self.c.grid(column=0, row=2)

    def press_c(self, event):
        self.clearCanvas()

    def create_info(self):
        fr_info = Frame(self, highlightthickness=5)
        fr_info.grid(column=0, row=0)

        fr_text = Frame(fr_info)
        fr_text.grid(column=0, row=0)

        ''' Добавляем информацию о том, как рисовать '''
        Label(fr_text, text="Рисовать: ЛКМ").grid(column=0, row=0, padx=10, pady=5)
        Label(fr_text, text="Стирать: ПКМ").grid(column=0, row=1, padx=10, pady=5)

        ''' Добавляем кнопки '''
        ButtonView(fr_info, "C: Очистить", _callback=self.clearCanvas).grid(column=1, row=0, padx=10, pady=5)
        ButtonView(self, "Узнать", _callback=self.get_predict).grid(column=1, row=0, padx=10, pady=5)

    def create_info_perceptron(self):
        fr_perceptron = Frame(self)
        fr_perceptron.grid(column=1, row=2)
        for i, perceptron in enumerate(self.layer_perceptron):
            self.label_perceptron.append(Label(fr_perceptron, text="Перцептрон {}: ".format(perceptron.get_id())))
            self.label_perceptron[i].grid(column=0, row=i, padx=10, pady=5)

    def createPixels(self):
        for i in range(self.w):
            self.pixels.append([])
            for j in range(self.h):
                color = int(self.colors[i][j] * 255)
                color = (color << 16) | (color << 8) | color
                self.pixels[i].append(self.c.create_rectangle(
                    i * self.scale, j * self.scale,
                    i * self.scale + self.scale, j * self.scale + self.scale,
                    fill="#{0:06X}".format(color),
                    width=0
                ))

    def mouseMoveB1(self, event):
        self.paint(event)

    def mouseMoveB3(self, event):
        self.paint(event, "right")

    def paint(self, event, mouse_press="left"):
        mx = event.x / self.scale
        my = event.y / self.scale
        for i, j in itertools.product(range(self.w), range(self.h)):
            dist = (i - mx)**2 + (j - my)**2  # Высчитываем радиус от тоординаты мыши, то каждого пикселя в итерации
            if dist < 1:  # Задаем минимайный размер радиуса =1
                dist = 1
            dist *= dist
            if mouse_press == "left":
                self.colors[i][j] += 0.1 / dist
            elif mouse_press == "right":
                self.colors[i][j] -= 0.1 / dist
            if self.colors[i][j] > 1:
                self.colors[i][j] = 1
            if self.colors[i][j] < 0:
                self.colors[i][j] = 0
            color = int(self.colors[i][j] * 255)
            color = (color << 16) | (color << 8) | color
            self.c.itemconfigure(self.pixels[i][j], fill="#{0:06X}".format(color))

    def clearCanvas(self):
        for i, j in itertools.product(range(self.w), range(self.h)):
            self.colors[i][j] = 0
            color = (0 << 16) | (0 << 8) | 0
            self.c.itemconfigure(self.pixels[i][j], fill="#{0:06X}".format(color))

    def get_predict(self):
        predict_win = 0
        perceptron_win = 0
        for i, perceptron in enumerate(self.layer_perceptron):
            predict = perceptron.predict(self.colors)
            self.label_perceptron[i]['text'] = "Перцептрон {}: ".format(perceptron.get_id()) + str(round(predict, 2))
            if predict > predict_win:
                predict_win = predict
                perceptron_win = i
        print(perceptron_win)
        self.layer_perceptron[perceptron_win].train(self.colors, predict_win)
