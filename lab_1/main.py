from read_data import read_number
from neuron import *

# Темп обучения
n = 0.001
h = 0.75

X = read_number()

number = 2

layer = []
for i in range(9):
    layer.append(Neuron(X=X[number], i=i, h=h, number=number))
    layer[i].train(1000, n)
    print("Answer: {}".format(layer[i].get_answer()))

print("-----------------------------------------")

for i in range(len(layer)):
    answer = layer[i].analysis(X[2])
    print("Neuron #{}: {}".format(i, answer))
