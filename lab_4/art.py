from lab_4.comparison import Comparison
from lab_4.receiver_1 import Receiver1
from lab_4.recognition import Recognition
from lab_4.reset_block import ResetBlock


class ART:
    def __init__(self):

        # Слой распознавания
        self.layer_recognition = [Recognition()]

        # Слой сравнения
        self.layer_comparison = [Comparison() for i in range(8**2)]

        # Блок сброса
        self.reset_bloc = ResetBlock()

        # Приемник 1
        self.receiver_1 = Receiver1()

        self.init_state = True

    def work(self, input_x):

        # Если фаза инициализации
        if self.init_state:
            t = [0 for i in range(8**2)]

            # Получаем выходной вектор C
            output_c = []
            for i, neuron in enumerate(self.layer_comparison):
                output_c.append(neuron.result(self.receiver_1.get_g1(), t[i], input_x[i]))

            # Распознавание
            net_win = 0
            recognition_win = 0
            for i, neuron in enumerate(self.layer_recognition):
                net = neuron.calculate_r(output_c)
                if net > net_win:
                    net_win = net
                    recognition_win = i

            # Устанавливаем выход Приемника 1 G1 равным 1
            self.receiver_1.calculate_g1(input_x, [0])

            # Получаем выходной вектор C
            output_c = []
            for i, neuron in enumerate(self.layer_comparison):
                output_c.append(neuron.result(self.receiver_1.get_g1(), t[i], input_x[i]))

            # Сравнение
            reset = self.reset_bloc.reset_result(input_x, output_c)

            if reset:
                self.layer_recognition[recognition_win].learn(output_c)

            self.init_state = False
            return self.layer_recognition[recognition_win].get_t()

