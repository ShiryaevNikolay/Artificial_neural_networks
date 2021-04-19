import numpy as np


# Нейрон для слоя распознавания
class Recognition:
    def __init__(self):
        self.m = 8**2
        self.t = []
        self.b = [np.random.uniform(0, 2 / (2 - 1 + self.m)) for i in range(8**2)]

    def get_t(self):
        return self.t

    def calculate_r(self, input_c):
        net = np.dot(self.b, input_c)
        return net

    def learn(self, input_c):
        sum_c = sum(input_c)
        # Обучаем вектор весов T
        self.t = input_c
        for i in range(len(input_c)):
            # Обучаем вектор весов B
            self.b[i] = (2 * input_c[i]) / (2 - 1 + sum_c)
