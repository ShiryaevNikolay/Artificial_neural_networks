import os
from perceptron import *

n = 0.001  # Темп обучения
h = 0.7  # Сдвиг

X = read_number_train()  # Считываем тренеровочные данные

weight_file_path = "../number_weight"
h_file_path = "../number_h"
if not os.path.exists(h_file_path + ".xlsx"):
    create_h_file(h_file_path=h_file_path + ".xlsx")
if not os.path.exists(weight_file_path + ".xlsx"):
    create_weight_file(weight_file_path=weight_file_path + ".xlsx")

layer = []  # Слой персептронов
for i in range(10):  # По циклу заполняем слой персептронами для цифр от 0..9
    layer.append(Perceptron(length=len(X[0]), id_perceptron=i, h=h, h_file_path=h_file_path))

# # Тренеровка
# for number in range(len(X)):  # Пробегаем по каждому тренеровочному числу
#     print("Для цифры {}".format(number))
#     for i in range(10):  # Пробегаем по каждому персептрону
#         layer[i].train(X=X[number], number=number, epochs=1000, n=n)  # Обучаем персептрон
#         print("Персептрон #{}: {}".format(i, round(layer[i].get_answer(X[number]), 4)))

print("___________________Конец обучения___________________")

for i in range(len(layer)):  # Пробегаем по каждому персептрону
    X_data = read_number_data()  # Считываем число, которое хотим предсказать
    answer = layer[i].get_answer(X_data)  # Получаем ответ персептрона
    print("Персептрон #{}: {}".format(i, round(answer, 4)))
