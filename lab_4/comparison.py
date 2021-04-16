# Нейрон для слоя сравнения
class Comparison:
    def __init__(self):
        pass

    def result(self, receiver, recognition, input_x):
        if (receiver == 1 and recognition == 1) \
                or (receiver == 1 and input_x == 1) \
                or (recognition == 1 and input_x == 1):
            return 1
        return 0
