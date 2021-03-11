from func import *
from read_data import *
from write_data import *


class Perceptron:
    def __init__(self, length, id_perceptron=0, h=0.5, weight_file_path="../number_weight", h_file_path="../number_h"):
        self.id_perceptron = id_perceptron  # Храним порядковый номер персептрона
        self.weight_file_path = weight_file_path + ".xlsx"
        self.h_file_path = h_file_path + ".xlsx"
        if cell_empty(id_perceptron=self.id_perceptron, h_file_path=self.h_file_path):
            init_h(id_perceptron=self.id_perceptron, h=h, h_file_path=self.h_file_path)
        self.h = read_h(id_perceptron=self.id_perceptron, h_file_path=self.h_file_path)
        if not weight_sheet_exist(id_perceptron=self.id_perceptron, weight_file_path=self.weight_file_path):
            print("Инициализируем веса")
            init_weight(id_perceptron=self.id_perceptron, count=length, weight_file_path=self.weight_file_path)
        self.weight = read_weight(id_perceptron=self.id_perceptron, count=length, weight_file_path=self.weight_file_path)  # Инициализируем веса для текущего персептрона

    # Функция обучения
    def train(self, X, number, epochs=1, n=1):
        target = read_target(number)  # Читаем данные, которые мы хотим получить от текущего персептрона
        for epoch in range(epochs):  # Пробегаем по каждой эпохе
            net_y = net(X, self.weight) + ((-1) * self.h)  # Суммируем произведения Xi*Wi
            z = activation_fun(net_y, self.h)  # Предсказание персептрона (ступенчатая функция)
            err = target[self.id_perceptron] - z  # Получаем ошибку
            for i in range(len(self.weight)):  # Пробегаем по всем весам и подстраиваем их
                self.weight[i] += err * X[i] * n
            self.h += err * (-1) * n  # Также подстроим сдвиг
        write_weight(id_perceptron=self.id_perceptron, weights=self.weight, weight_file_path=self.weight_file_path)
        write_h(id_perceptron=self.id_perceptron, h=self.h, h_file_path=self.h_file_path)

    # Функция получаения ответа
    def get_answer(self, X):
        weight = read_weight(self.id_perceptron, count=len(self.weight), weight_file_path=self.weight_file_path)
        net_y = net(X, weight) - self.h  # Суммируем произведения Xi*Wi
        z = activation_fun(net_y, self.h)  # Предсказание персептрона (ступенчатая функция)
        return z
