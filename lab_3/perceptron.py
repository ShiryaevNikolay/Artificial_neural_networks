import itertools

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
        # sqrt_sum_weight = self.sqrt_sum(input_data)
        # for i in range(len(input_data)):
        #     for j in range(len(input_data[i])):
        #         input_data[i][j] /= sqrt_sum_weight
        return self.activation(np.sum(np.multiply(input_data, self.weight)) + self.b)

    """ Обучение персептрона """
    def train(self, input_data, predict):
        # sqrt_sum_weight = self.sqrt_sum(input_data)
        # for i in range(len(input_data)):
        #     for j in range(len(input_data[i])):
        #         input_data[i][j] /= sqrt_sum_weight
        u = np.array(input_data) - np.array(self.weight)
        for i, j in itertools.product(range(len(input_data)), range(len(self.weight))):
            self.weight[i][j] += u[i][j] * self.learning_rate * predict
        # sqrt_sum_weight = self.sqrt_sum(self.weight)
        # for i, j in itertools.product(range(28), range(28)):
        #     self.weight[i][j] /= sqrt_sum_weight

    def save_weight(self):
        write_weight(id_perceptron=self.id_perceptron, weights=self.weight, weight_file_path=self.weight_file_path)

    def sqrt_sum(self, input_data):
        sum = 0
        for row in input_data:
            for data in row:
                sum += data**2
        return np.sqrt(sum)
