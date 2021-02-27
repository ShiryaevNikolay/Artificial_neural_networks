from read_data import read_number
from neuron import *

# Темп обучения
n = 0.001
h = 0.7

X = read_number()

layer = []
for i in range(10):
    layer.append(Neuron(length=len(X[0]), i=i, h=h))

for number in range(len(X)):
    print("For {} number".format(number))
    for i in range(10):
        layer[i].train(X=X[number], number=number, epochs=1000, n=n)
        print("Neuron #{}: {}".format(i, layer[i].get_answer(X[number])))

print("-----------------------------------------")

for i in range(len(layer)):
    answer = layer[i].analysis(X[7])
    print("Neuron #{}: {}".format(i, answer))
