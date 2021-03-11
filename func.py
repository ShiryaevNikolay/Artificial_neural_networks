from openpyxl import load_workbook
import numpy as np

table_file = '../number_weight.xlsx'
table_target_file = '../number_target.xlsx'


# Активационная функция (ступенчатая функция)
def activation_fun(net_y, h):
    if net_y > h:
        return 1
    elif net_y <= h:
        return 0


# функция NET
def net(x, w):
    net_y = 0
    for i in range(len(x)):
        net_y += x[i] * w[i]
    return net_y


def init_weight(length):
    weight = []
    for i in range(length):
        weight.append(np.random.randint(-1, 1))
    return weight


def read_target(number):
    table = load_workbook(table_target_file)
    target = []
    for i in range(10):
        target.append(table.get_sheet_by_name(str(1)).cell(row=i+1, column=number+1).value)
    return target
