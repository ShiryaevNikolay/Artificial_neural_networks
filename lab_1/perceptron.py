from func import *


class Perceptron:
    def __init__(self, length, i=0, h=0.75):
        self.h = h  # Сдвиг
        self.i = i  # Храним порядковый номер персептрона
        self.weight = init_weight(length)  # Инициализируем веса для текущего персептрона

    # Функция обучения
    def train(self, X, number, epochs=1, n=1):
        target = read_target(number)  # Читаем данные, которые мы хотим получить от текущего персептрона
        for epoch in range(epochs):  # Пробегаем по каждой эпохе
            net_y = net(X, self.weight) + ((-1) * self.h)  # Суммируем произведения Xi*Wi
            z = activation_fun(net_y, self.h)  # Предсказание персептрона (ступенчатая функция)
            err = target[self.i] - z  # Получаем ошибку
            for i in range(len(self.weight)):  # Пробегаем по всем весам и подстраиваем их
                self.weight[i] += err * X[i] * n
            self.h += err * (-1) * n  # Также подстроим сдвиг

    # Функция получаения ответа
    def get_answer(self, X):
        net_y = net(X, self.weight) - self.h  # Суммируем произведения Xi*Wi
        z = activation_fun(net_y, self.h)  # Предсказание персептрона (ступенчатая функция)
        return z
