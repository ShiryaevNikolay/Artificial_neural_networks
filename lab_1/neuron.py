import numpy as np
from func import *


class Neuron:
    def __init__(self, length, i=0, h=0.75):
        self.h = h
        self.i = i
        self.weight = init_weight(length)

    def train(self, X, number, epochs=1, n=1):
        target = read_target(number)
        for epoch in range(epochs):
            net_y = net(X, self.weight) + ((-1) * self.h)
            z = activation_fun(net_y, self.h)
            err = target[self.i] - z
            for i in range(len(self.weight)):
                self.weight[i] += err * X[i] * n
            self.h += err * (-1) * n

    def get_answer(self, X):
        net_y = net(X, self.weight) - self.h
        z = activation_fun(net_y, self.h)
        return z

    def analysis(self, X):
        net_y = net(X, self.weight) + ((-1) * self.h)
        z = activation_fun(net_y, self.h)
        return z
