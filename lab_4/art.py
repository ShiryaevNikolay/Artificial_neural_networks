from lab_4.comparison import Comparison
from lab_4.receiver_1 import Receiver1
from lab_4.recognition import Recognition
from lab_4.reset_block import ResetBlock


class ART:
    def __init__(self):

        # Слой распознавания
        self.layer_recognition = []

        # Слой сравнения
        self.layer_comparison = [Comparison() for i in range(8**2)]

        # Блок сброса
        self.reset_bloc = ResetBlock()

        # Приемник 1
        self.receiver_1 = Receiver1()

    def work(self, input_x):
        pass
        # # Инициализация: если слой распознавания пустой, то вектор весов T=1
        # if len(self.layer_recognition) == 0:
        #     t = [0 for i in range(8**2)]
        # else:
        #     for i, neuron in enumerate(self.layer_recognition):
        #
        # # Вычисляем результаты нейронов слоя сравнения, получаем C
        # output_c = []
        # for i, neuron in enumerate(self.layer_comparison):
        #     output_c.append(neuron.result(self.receiver_1.get_g1(), t[i], input_x))


