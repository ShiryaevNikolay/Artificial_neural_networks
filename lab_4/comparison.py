# Нейрон для слоя сравнения
class Comparison:

    def result(self, receiver, recognition, input_x):
        if receiver == recognition == 1 or receiver == input_x == 1 or recognition == input_x == 1:
            return 1
        return 0
