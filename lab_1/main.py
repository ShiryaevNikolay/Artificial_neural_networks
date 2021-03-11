from read_data import *
from perceptron import *

n = 0.001  # Темп обучения
h = 0.7  # Сдвиг

X = read_number_train()  # Считываем тренеровочные данные

layer = []  # Слой персептронов
for i in range(10):  # По циклу заполняем слой персептронами для цифр от 0..9
    layer.append(Perceptron(length=len(X[0]), i=i, h=h))

for number in range(len(X)):  # Пробегаем по каждому тренеровочному числу
    print("For {} number".format(number))
    for i in range(10):  # Пробегаем по каждому персептрону
        layer[i].train(X=X[number], number=number, epochs=1000, n=n)  # Обучаем персептрон
        print("Perceptron #{}: {}".format(i, layer[i].get_answer(X[number])))

print("___________________Конец обучения___________________")

for i in range(len(layer)):  # Пробегаем по каждому персептрону
    X_data = read_number_data()  # Считываем число, которое хотим предсказать
    answer = layer[i].get_answer(X_data)  # Получаем ответ персептрона
    print("Perceptron #{}: {}".format(i, answer))
