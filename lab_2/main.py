import os
import matplotlib.pyplot as plt
from perceptron import *

speed_train = 0.001  # Темп обучения
h = 0.7  # Сдвиг

X = read_number_train()  # Считываем тренеровочные данные

weight_file_path = "../number_weight"
h_file_path = "../number_h"
if not os.path.exists(h_file_path + ".xlsx"):
    create_h_file(h_file_path=h_file_path + ".xlsx")
if not os.path.exists(weight_file_path + ".xlsx"):
    create_weight_file(weight_file_path=weight_file_path + ".xlsx")

layer = []  # Слой персептронов
errors_perceptron = []
for i in range(10):  # По циклу заполняем слой персептронами для цифр от 0..9
    errors_perceptron.append(0)
    layer.append(Perceptron(length=len(X[0]), id_perceptron=i, h=h, h_file_path=h_file_path))

# # Тренеровка
# for number in range(len(X)):  # Пробегаем по каждому тренеровочному числу
#     print("Для цифры {}".format(number))
#     for i in range(10):  # Пробегаем по каждому персептрону
#         layer[i].train(X=X[number], number=number, epochs=1000, speed_train=speed_train)  # Обучаем персептрон
#         print("Персептрон #{}: {}".format(i, round(layer[i].get_answer(X[number]), 4)))
# print("___________________Конец обучения___________________")

noises = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]  # Шумы
chance_noise = []  # Массив для хранения вероятности ошибки для каждого шума

count_step = 1000  # Количство проходов для каждого шума

X_data = read_number_data()  # Считываем число, которое хотим предсказать
for noise in range(len(noises)):  # Проходим по каждому шуму
    chance_noise.append([])  # Для текущего шума добвляем массив, который хранит вер. ошибки для каждого персептрона

    for i in range(count_step):  # На каждом проходе добавляем рандомно шум
        X_with_noise = add_noise(X_data, noises[noise])  # Добавляем шум

        for id_perceptron in range(len(layer)):  # Пробегаем по каждому персептрону
            answer = layer[id_perceptron].get_answer(X_with_noise)  # Получаем ответ персептрона
            if answer == 0:
                errors_perceptron[id_perceptron] += 1  # Считаем кол-во ошибок для текущего персептрона
            elif answer == 1:
                print("Шум {}, Шаг: {}, Отреагировал персептрон #{}: {}".format(noises[noise], i, id_perceptron, answer))

    # После прохода по всем шагам, вычисляем вер. ошибки для каждого шума и для каждого персептрона
    for id_perceptron in range(len(layer)):
        chance_noise[noise].append(errors_perceptron[id_perceptron] / count_step)
        errors_perceptron[id_perceptron] = 0  # Зануляем кол-во ошибок, чтобы на следующем шуме начать отчет заново

# Строим график вер. ошибки от кол-ва шума для каждого персептрона
for perceptron in range(len(layer)):
    plt.grid(True)
    plt.ylim(0, 1)
    plt.title("Персептрон {}".format(perceptron))
    plt.ylabel("Вероятность ошибки")
    plt.xlabel("Кол-во шума")

    chance = []  # Массив вер. ошибки (координата Y)
    for i in range(len(chance_noise)):
        chance.append(chance_noise[i][perceptron])  # Добавляем вер. ошибки текущего персептрона для i-го шума
    print("Вероятности для {} персептрона: {}".format(perceptron, chance))
    plt.scatter(noises, chance)
    plt.show()
