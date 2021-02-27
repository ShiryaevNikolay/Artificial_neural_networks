import numpy as np
from func import *


class Neuron:

    def __init__(self, X, i=0, h=0.75, number=1):
        # self.weights = 2 * np.random.rand(inputs).T - 1  # Веса, -1 > w < 1
        self.X = X
        self.h = h
        self.i = i
        self.target = read_target(number)
        self.weight = init_weight(len(self.X))

    def train(self, epochs=1, n=1):
        for epoch in range(epochs):
            net_y = net(self.X, self.weight) + ((-1) * self.h)
            z = activation_fun(net_y, self.h)
            err = self.target[self.i] - z
            for i in range(len(self.X)):
                self.weight[i] = self.weight[i] + (err * self.X[i] * n)
            self.h = self.h + (err * (-1) * n)

            # print("Эпоха #{} - error: {}".format(epoch + 1, err))

    def get_answer(self):
        net_y = net(self.X, self.weight) - self.h
        z = activation_fun(net_y, self.h)
        return z

    def analysis(self, X):
        net_y = net(X, self.weight) - self.h
        z = activation_fun(net_y, self.h)
        return z
