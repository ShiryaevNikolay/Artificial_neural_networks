from openpyxl import load_workbook
import numpy as np

table_file = '../number_weight.xlsx'
table_target_file = '../number_target.xlsx'


# Активационная функция
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
    # table = load_workbook(table_file)
    # for i in range(35):
    #     table.get_sheet_by_name(str(number)).cell(row=i+1, column=1).value = np.random.random()
    # table.save(filename=table_file)
    weight = 2 * np.random.rand(length).T - 1
    return weight


def read_weight(number):
    wights = []
    table = load_workbook(table_file)
    for i in range(35):
        wights.append(table.get_sheet_by_name(str(number)).cell(row=i+1, column=1).value)
    return wights


def write_weight(number, weight):
    table = load_workbook(table_file)
    for i in range(35):
        table.get_sheet_by_name(str(number)).cell(row=i+1, column=1).value = weight[i]


def read_target(number):
    table = load_workbook(table_target_file)
    target = []
    for i in range(9):
        target.append(table.get_sheet_by_name(str(1)).cell(row=i+1, column=number+1).value)
    return target
