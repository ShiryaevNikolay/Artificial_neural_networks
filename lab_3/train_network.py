import os
import itertools
import zipfile
from PIL import Image
from perceptron import *

""" Если файла с весами не существует, то создаем его """
weight_file_path = "../mnist_weight.xlsx"
if not os.path.exists(weight_file_path):
    create_weight_file(weight_file_path=weight_file_path)

layer = []  # Слой персептронов

for i in range(10):
    layer.append(Perceptron(length=28*28, id_perceptron=i))

""" Тренеруем сеть """
with zipfile.ZipFile("../mnist_train.zip", "r") as archive:
    img_i = 0
    for filename in archive.namelist():
        img_i += 1
        training_data = []
        with archive.open(filename) as file:
            img = Image.open(file)
            pixels = img.load()
            for x, y in itertools.product(range(img.size[0]), range(img.size[1])):
                training_data.append(pixels[x, y])
        print("Картинка {}".format(img_i))
        predict_win = 0
        perceptron_win = 0

        for i, perceptron in enumerate(layer):
            predict = perceptron.predict(training_data)
            if predict > predict_win:
                predict_win = predict
                perceptron_win = i
        # for id_perceptron in range(len(layer)):
        #     predict = layer[id_perceptron].predict(training_data)
        #     # print("{} ".format(predict), end="")
        #     if predict > predict_win:
        #         predict_win = predict
        #         perceptron_win = id_perceptron
        layer[perceptron_win].train(training_data, predict_win)

for perceptron in layer:
    perceptron.save_weight()
