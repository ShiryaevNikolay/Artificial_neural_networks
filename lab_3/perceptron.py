from func import *
from functions.sigmoid import *
from functions.relu import *
from read_data import *
from write_data import *


class Perceptron:

    def __init__(self, length, id_perceptron=0, lr=0.1, weight_file_path="../mnist_weight.xlsx", activ_fun=sigmoid):
        self.id_perceptron = id_perceptron
        self.learning_rate = lr
        self.weight_file_path = weight_file_path
        self.activation = activ_fun
        """ Инициализируем веса, если нет данных для текущего персептрона """
        if not weight_sheet_exist(id_perceptron=self.id_perceptron, weight_file_path=self.weight_file_path):
            init_weight_and_save_to_file(id_perceptron=self.id_perceptron, count=length, weight_file_path=self.weight_file_path)
        self.weight = read_weight(id_perceptron=self.id_perceptron, count=length, weight_file_path=self.weight_file_path)

    """ Предсказание сети """
    def predict(self, input_data):
        return self.activation(np.inner([i / 255 for i in input_data], self.weight))

    """ Обучение персептрона """
    def train(self, input_data, predict):
        u = [x - w for x, w in zip(input_data, self.weight)]
        for i in range(len(self.weight)):
            self.weight[i] += u[i] * self.learning_rate * predict

    def save_weight(self):
        write_weight(id_perceptron=self.id_perceptron, weights=self.weight, weight_file_path=self.weight_file_path)

    def answer(self):
        pass
