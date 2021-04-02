import itertools

import matplotlib.pyplot as plt
from func import *
from functions.sigmoid import *
from read_data import *
from write_data import *


class Perceptron:

    def __init__(self, length, id_perceptron=0, lr=0.1, weight_file_path="../mnist_weight.xlsx", activ_fun=sigmoid):
        self.b = np.random.random()
        self.id_perceptron = id_perceptron
        self.learning_rate = lr
        self.weight_file_path = weight_file_path
        self.activation = activ_fun
        """ Инициализируем веса, если нет данных для текущего персептрона """
        if not weight_sheet_exist(id_perceptron=self.id_perceptron, weight_file_path=self.weight_file_path):
            init_weight_and_save_to_file(id_perceptron=self.id_perceptron, count=length, weight_file_path=self.weight_file_path)
        self.weight = read_weight(id_perceptron=self.id_perceptron, count=length, weight_file_path=self.weight_file_path)

    def get_id(self):
        return self.id_perceptron

    """ Предсказание сети """
    def predict(self, input_data):
        return self.activation(np.sum(np.multiply(input_data, self.weight)) + self.b)

    """ Обучение персептрона """
    def train(self, input_data, predict):
        u = np.array(input_data) - np.array(self.weight)
        for i, j in itertools.product(range(len(input_data)), range(len(self.weight))):
            self.weight[i][j] += u[i][j] * self.learning_rate * predict

    def save_weight(self):
        write_weight(id_perceptron=self.id_perceptron, weights=self.weight, weight_file_path=self.weight_file_path)

    def answer(self):
        pass
